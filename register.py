import os
inp = int(input("1.register 2.login"))
if inp =="1":
    username = input("enter a username:")
    password = input("enter a password:")
    if not os.path.exists("/signup"):
        os.mkdir("signup")
    with open(f"/signup/{username}.txt","w") as file:
        file.write(f"{username} {password}")
        print("signup successfully")
        print("you are register successfully")