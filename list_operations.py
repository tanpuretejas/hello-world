#this program is for list operation
mylist=[]
for A in range(5):
    A=int(input("enter 5 number"))
    mylist.append(A)

print("number in the list are:",mylist)
print("maximum value in list",max(mylist))
print("minimum value in list",min(mylist))
print("sum of all values in list",sum(mylist))
print("average of all list values",sum(mylist)/len(mylist))

mylist.sort()
print("sorted list in asceding order",mylist)
mylist.reverse()
print("list after reversing",mylist)