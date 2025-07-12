#printing numbers from 1 to 10
for i in range(1,11):
    print("number are",i)

#printing even numbers between 1 to 50 using loop
for num in range(1,51):
    if num%2==0:
        print("this is the even number",num)

#multiplication table of any number
num=int(input("enter number for multiplication table of that number"))
for t in range(1,11):
    print("multiplication table of the number is",num*t)

#printing numbers from 10 to 1 using while loop
j=11
while j>1:
    j-=1
    print("number are",j)

#finding sum of digit using while loop
i=int(input("enter the number to find its sum of digit"))
sum=0
while i>0:
    num=i%10
    sum+=num
    i=i // 10
print(sum)

#prime number or not
num=int(input("enter the number to find its prime or not"))
for i in range(2,num):
    if num%i==0:
        print("this is not a prime number")
        break
else:
    print("this is the prime number",num)