#this program is for password checker.
name=input("enter your name")
password=input("enter password")

if name.isalpha():
    if len(password)>=8:
        print("welcome",name,"your account created successfully")
    else:
        print("password too short,minimum 8 character required")
else:
    print("invalid name,only alphabets allowed")