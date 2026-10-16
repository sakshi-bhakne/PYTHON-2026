#prime factor :
n = int(input("Enter a number: "))

for i in range(2, n + 1):
    while n % i == 0:
        print(i)
        n = n // i