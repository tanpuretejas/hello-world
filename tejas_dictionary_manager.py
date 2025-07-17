student={}
for i in range(3):
    name=input(f"enter name of student{i+1}")
    try:
        marks=float(input(f"enter marks of{name}:"))
        student[name]=marks
    except ValueError:
        print("Invalid marks entered,please enter valid marks")
print("student details:\n",student)
length=len(student)
print("number of students:",length)
total_marks=sum(student.values())
print("total marks of students are:",total_marks)
average=total_marks/length
print("average marks of student is:",average)
topper=max(student.items(),key=lambda X: X[1])
print("topper is:",topper[0],"with",topper[1],"marks")