class Hotel:

    def Menu(Self,out):

        if(out=='curry'):
            Curry = {
            'panner':140,
            'kofta':80,
            'Mix veg':90,
            'Gatte':100,
            'Kadhi':110
            }
            for x in Curry:
                print(x)
            item=input("Enter the item: ")
            for x in Curry:
                 if(item==x):
                     return(Curry[x])
                     
                
            



        elif(out=='non_veg'):
    
            Non_veg= {
            'Butter Masla Chiken':290,
            'Fish':230,
            'Frog':500,
            }
            for x in Non_veg:
                print(x)
            item=input("Enter the item: ")
            for x in Non_veg:
                 if(item==x):
                     return(Non_veg[x])
            
        elif(out=='sweet'):
            sweet={
            'Gulab Jamun':30,
            'Rasgoola':40,
            'Laddoo':50,
            }
            for x in sweet:
                print(x)
            item=input("Enter the item: ")
            for x in sweet:
                 if(item==x):
                     return(sweet[x])
        

print("Welcome to the Hotel")

cat = {1:'curry',2:"sweet",3:"Non_veg"}
for x in cat:
    print(cat[x])
out = input("What would you like to have: ")
out = out.lower()
print(out)

# obj = Hotel()
# amount = obj.Menu(out)
# cgst= ((18 * amount)/100)
# sgst= ((9 * amount)/100)
# Total_bill =  amount + (cgst)+(sgst)
# print("Food is getting prepared")
# print("Your total bill is: ",round(Total_bill,2))
   
    

    

       

