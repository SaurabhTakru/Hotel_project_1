class Hotel:

    def Menu(Self,out):

        
            if (out=='curry'):
                curry = {1:{'name':'panner','price':140},
                         2:{'name':'kofta','price':80},
                         3:{'name':'Mix Veg','price':90},
                         4:{'name':'Gatte','price':100},
                         5:{'name':'Kadhi','price':110}}
                
                for x in curry:
                     print(x," ",curry[x]["name"]," ",curry[x]["price"])

                item = int(input())  
                return curry[item]["price"]
                
            



            if(out=='non veg'):
                 
                non_veg={
                        1:{'name':'Butter Masla Chiken','price':290,},
                        2:{'name':'Fish','price':230,},
                        3:{'name':'Frog','price':500}
                        }
                for x in non_veg:
                     print(x," ",non_veg[x]["name"]," ",non_veg[x]["price"])
                item = int(input())  
                return non_veg[item]["price"]

            if(out=='sweet'):
                 
                sweet={
                        1:{'name':'Gulab Jamun','price':30,},
                        2:{'name':'Rasgoola','price':40,},
                        3:{'name':'Laddoo','price':50}
                        }
                for x in sweet:
                     print(x," ",sweet[x]["name"]," ",sweet[x]["price"])

                item = int(input("Please select item to eats: "))  
                return sweet [item]["price"]
       
        

print("Welcome to the Hotel")

cat = {
     1:{'cat1':'curry'},
     2:{'cat1':"sweet"},
     3:{'cat1':"non veg"}}
for x in cat:
    print(x,cat[x]['cat1'])

out = int (input("What would you like to have: "))
select = cat[out]["cat1"]
out = select.lower()

obj = Hotel()
amount = obj.Menu(out)
print(amount)
cgst= ((18 * amount)/100)
sgst= ((9 * amount)/100)
Total_bill =  amount + (cgst)+(sgst)
print("Food is getting prepared")
print("Your total bill is: ",round(Total_bill,2))
   
    

    

       

