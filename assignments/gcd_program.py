n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
gcd = 1
for i in range (1,min(n1,n2)+1):
    if n1 % i == 0 and n2 % i == 0:
        gcd  = i
print("Greatest common divisor is : ",gcd)
       
