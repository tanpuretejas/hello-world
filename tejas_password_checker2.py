import re
for password in range(3):
    name=input("enter your username")
    password=(input("enter password"))
    if len(password)>=8:
            if re.search(r'\d',password):
                if re.search(r'[A-Z]',password):
                    if password !=name:
                        print("access Granted!")
                        break
                    else:
                        print("password should not be same as name")
                else:
                    print("password must be contain atleast 1 upper case letter")
            else:
                print("password must contain a digit")
    else:
        print("password too short")
print("too many failed attempts,access denied")