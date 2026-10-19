n1 = int(input("Enter any number : "))
n2 = int(input("Enter any number : "))
LCM = 1
for i in range(max(n1,n2),n1*n2 + 1):
    if i % n1 == 0 and i % n2 == 0:
        LCM = i
        break
print("Lowest common multiple is : ",LCM)
