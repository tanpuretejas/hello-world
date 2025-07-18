from functools import reduce
def student_summary():
    student=int(input("enter how many number of students marks you want to enter:"))
    list1=[]
    for j in range(student):
        j=float(input("enter marks of student:"))
        list1.append(j)
    print("student marks are:",list1)
    bonus_marks=list(map(lambda x:x*1.20,list1))
    print("marks of students after adding 20% bonus to each mark:",bonus_marks)
    top_performers=list(filter(lambda x:x>=75,bonus_marks))
    print("top performers on the basis of marks are:",top_performers)
    total_num_of_students=len(list1)
    print("total num of students are:",total_num_of_students)
    total_top_perfomers=len(top_performers)
    print("total top performers are:",total_top_perfomers)
    total_marks=reduce(lambda x,y:x+y,top_performers)
    average_marks=total_marks/total_top_perfomers
    print("average marks of top perfomers are:",average_marks)
student_summary()