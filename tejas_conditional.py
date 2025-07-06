'''this is a even odd program'''

num=int(input("enter the number to check even or odd"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

'''this is program for finding greater number'''

num1=int(input("enter the first number "))
num2=int(input("enter the second number "))

if num1>num2:
    print("num1 is greater")
elif num2>num1:
    print("num2 is greater")
else:
    print("both number are equal")

'''this program is for displaying grade of student'''

marks=int(input("enter the marks of student"))

if marks>=90:
    print("grade is A+")
elif marks>=75 and marks<=89:
    print("grade is A")
elif marks>=60 and marks<=74:
    print("grade is B")
elif marks>=40 and marks<=59:
    print("grade is C")
else:
    print("sadly......student is fail")    