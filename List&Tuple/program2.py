#Program to check if palindrome or not:

# list1 = ["apple","mango","apple"]
list2 = [1,2,3]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Is palindrome.")
else:
    print("Not a palindrome.")

print(copy_list2)
print(list2)