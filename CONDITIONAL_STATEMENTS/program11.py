
income = int(input("Enter your annual income: "))

if income <= 300000:
    tax = 0

elif income <= 700000:
    tax = (income - 300000) * 0.05

else:
    tax = 20000 + (income - 700000) * 0.10

print("Income tax =", tax)
