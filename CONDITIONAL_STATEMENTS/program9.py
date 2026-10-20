shopping_amount = int(input("enter shopping amount: "))

if(shopping_amount >= 5000):
    discount = shopping_amount *  20 / 100
    print(discount)
elif(shopping_amount >= 3000):
    discount = shopping_amount * 10 / 100
    print(discount)
else:
    discount = 0 

    
    final_amount = shopping_amount - discount
print("final amount: ",final_amount)