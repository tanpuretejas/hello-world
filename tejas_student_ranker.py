#this program is for student ranker
for s in range(3):
    #following data is for 1st student
    name1=input("enter the name of 1st student:")
    list1=[]
    for t in range(5):
        t=int(input("enter the marks of 5 subject for 1st student="))
        if t<0 or t>100:
            print("invalid marks,please enter valid marks")
            continue
        list1.append(t)

    tmos1=sum(list1)
    print("total marks of",name1,"is:",tmos1)
    a1=tmos1/len(list1)
    print("average of",name1,"is:",a1)
    p1=tmos1/(len(list1)*100)*100
    print("percentage of",name1,"is:",p1)
    
    #following data is for 2nd student
    name2=input("enter the name of 2nd student:")
    list2=[]
    for x in range(5):
        x=int(input("enter the marks of 5 subject for 2nd student="))
        if x<0 or x>100:
            print("invalid marks,please enter valid marks")
            continue
        list2.append(x)

    tmos2=sum(list2)
    print("total marks of",name2,"is:",tmos2)
    a2=tmos2/len(list2)
    print("average of",name2,"is:",a2)
    p2=tmos2/(len(list2)*100)*100
    print("percentage of",name2,"is:",p2)

    #following data is for 3rd student
    name3=input("enter the name of 3rd student:")
    list3=[]
    for y in range(5):
        y=int(input("enter the marks of 5 subject for 3rd student="))
        if y<0 or y>100:
            print("invalid marks,please enter valid marks")
            continue
        list3.append(y)

    tmos3=sum(list3)
    print("total marks of",name3,"is:",tmos3)
    a3=tmos3/len(list3)
    print("average of",name3,"is:",a3)
    p3=tmos3/(len(list3)*100)*100
    print("percentage of",name3,"is:",p3)
    
    #ranking students based on their percentage
    if p1>p2 and p1>p3:
        print("topper is:",name1,"with",p1)
    elif p2>p1 and p2>p3:
        print("topper is:",name2,"with",p2)
    else:
        print("topper is:",name3,"with",p3)
    break

