#checking username and password

UserName = "SakshiBhakne"
Password = "Sakshi@123"

username = (input("enter your username : "))
password = (input("enter password : "))

if(username == UserName and password == Password):
    print("Login successfully")
else:
    print("Invalid username or password")