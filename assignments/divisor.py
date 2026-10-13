n = int(input("Enter any number : "))
arr = []
for i in range(1,n+1):
    if n % i == 0:
        arr.append(i)
print (arr)