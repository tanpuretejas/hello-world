#this is a age classifier program

try:
    age=float(input("enter your age age"))
except ValueError:
    print("invalid input: please enter valid age")  
    exit()

if age<0:
    print("age cannot be negative")   
elif age==1:
    print("you are a infant")
elif age>=2 and age<=12:
    print("you are a child")
elif age>=13 and age<=17:
    print("you are a teenager")
elif age>=18 and age<=59:
    print("you are adult")
elif age>=60:
    print("you are a senior citizen")
