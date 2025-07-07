#this program is for marks analyzer of student
list1=[]
for i in range(5):
    i=int(input("enter marks of 5 subject"))
    if i<0 or i>100:
        print("Invalid marks,enter valid marks")
        continue
    list1.append(i)
print(list1)
totalmarks=sum(list1)
print("total marks of student is:",totalmarks)
totalsubject=len(list1)
print("total subject are:",totalsubject)
average=totalmarks/totalsubject
print("average marks of student is:",average)
percentage=(totalmarks/(5 *100))*100
print(f"percentage of student is:{percentage:.2f}%",)
if percentage>=90:
    print("student grade is A")
elif percentage>=75 and percentage<=89:
    print("student grade is B")
elif percentage>=60 and percentage<=74:
    print("student grade is C")
elif percentage>=40 and percentage<=59:
    print("student grade is D")
else:
    print("student is failed")
