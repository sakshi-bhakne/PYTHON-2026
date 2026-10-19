n = int(input())
count = 0

for i in range(2, n + 1):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        count += 1

print(count)