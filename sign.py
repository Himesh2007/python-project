import os
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful!")
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")
            if user == username and pwd == password:
                print("Login successful!")
                return
    print("Login failed. Please check your username and password.")
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    if not os.path.exists("users.txt"):
        with open("users.txt", "w") as file:
            pass  
    main()