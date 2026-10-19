n = int(input("Enter a number: "))
original = n
total = 0

while n > 0:
    digit = n % 10
    total = total + digit ** 3
    n = n // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")