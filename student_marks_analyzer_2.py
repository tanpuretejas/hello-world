#importing functools for reduce function
from functools import reduce
#declaring list of containing marks of 10 student
student=[77,55,39,35,67,88,25,85,51,49]
print("students marks are:",student)
#using map function for adding 10% bonus to each student marks
bonus_marks=list(map(lambda mark:mark*1.10,student))
print("students marks after 10% bonus:",bonus_marks)
#using filter for finding passed students
great_students=list(filter(lambda x:x>50,bonus_marks))
print("passed students are:",great_students)
#calculating total marks of students with the help of reduce function
total_marks=reduce(lambda x,y:x+y,great_students)
print("total marks of students are:",total_marks)