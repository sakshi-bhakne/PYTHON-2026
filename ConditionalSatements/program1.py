#Grade student based on marks:

#First way:
marks = 85

if(marks >= 90):
    print("grade = A")
elif( marks >= 80 and marks < 90):
    print("grade = B")
elif( marks >= 70 and marks < 80):
    print("grade = C")
elif( marks < 70):
    print("grade = D")

#By taking input from user:

marks = int(input("enter the marks of student : "))
if(marks >= 90):
    Grade = "A"
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"
print("Grade of student is : ",Grade)