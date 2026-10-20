# numbers = [1,2,3,4,5,6]
# print(numbers[0])
# print(numbers[-1])

# Add the value in list:
names = ["sampada","sujal","resham","sujal","sai","tejas","rashi"]
names.insert(0,"sakshi")
print(names)

# change the value:
names = ["sakshi","sam","sujal","sujal","sai","teju","rashi","resham"]
names[5] = "tejas"
print(names)

# remove the element:
names = ["sakshi","sam","sujal","sujal","sai","teju","rashi","resham"]
names.pop(0)
print(names)

# to find the length:
names = ["sakshi","sam","sujal","sujal","sai","teju","rashi","resham"]
print(len(names))

# sort a list:
names = ["sakshi","sam","sujal","sujal","sai","teju","rashi","resham"]
names.sort()
print(names)