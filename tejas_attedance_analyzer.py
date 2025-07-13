
def get_user_info():
    student=[]
    count=0
    while count<5:
        n1=input(f"enter the name of student {count+1}:")
        try:
            a1=float(input(f"enter the attendance of{n1}:"))
            if 0<=a1<=100:
                student.append({"name":n1,"attendance":a1})
                count+=1
            else:
                print("Invalid attendance!!! please enter between 0 to 100")
        except ValueError:
            print("please enter valid attendance")

    for s in student:
        print(f"{s["name"]}-{s["attendance"]}%")
        if s["attendance"]<75:
            print(f"{s["name"]}-{s["attendance"]}=short attendance")
        else:
            print(f"{s["name"]}-{s["attendance"]}=Present")
        
get_user_info()