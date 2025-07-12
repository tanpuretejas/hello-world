def add_numbers():
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    c=a+b
    print("addition of two numbers:",c)
#add_numbers()

def factorial_num():
    fact=1
    i=int(input("enter the number to find its factorial:"))
    if i==0:
        print("please enter valid number,because zero does not have factorial")
    elif i<0:
        print("Invalid input,enter positive number")
    else:
        for f in range(1,i+1):
            fact=fact*f
        print("factorial of the number you entered is:",fact)      
#factorial_num()

def is_even():
    a=int(input("enter the to find number is even or not:"))
    if a%2==0:
        print("number is even:",a)
    else:
        print("number is not even")
#is_even()

def table():
    n=int(input("enter the number for the table of that number:"))
    for j in range(1,11):
        t=j*n
        print("table of this number is:",t)
#table()

def student_grade():
    percentage=int(input("enter the percentage of student:"))
    if percentage>=90:
        print("student grade is:A")
    if percentage>=75 and percentage<=89:
        print("student grade is:B")
    if percentage>=60 and percentage<=75:
        print("student grade is:C")
    if percentage>=40 and percentage<=59:
        print("student grade is:D")
    if percentage<40:
        print("student is failed!!!")
#student_grade()
while True:
    def main_fun():
        print("1 for addition of two numbers\n2 for finding a factorial of number\n3 for checking the number is even or odd\n4 for multiplication tabel\n5 for calculating the grade of student")
        try:
            option=int(input("enter a following options for specific operation:"))
            if option==1:
                add_numbers()
            elif option==2:
                factorial_num()
            elif option==3:
                is_even()
            elif option==4:
                table()
            elif option==5:
                student_grade()
            else:
                print("this is not a valid input,please enter valid input")
        except ValueError:
            print("INVALID INPUT")

    main_fun()