import os
def display_menu():
    print("Bank Management System")
    print("1. Create account")
    print("2. Check Balance")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Deposit")
    print("6. Exit")
def create_account(account_number):
    owner_name = input("Enter your name: ")
    initial_balance = float(input("Enter your initial balance: "))
    filename = f"{account_number}.txt"
    with open(filename, "w") as file:
        file.write(str(initial_balance))
    print("Account created successfully!")
def check_balance(account_number):
    filename = f"{account_number}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            balance = float(file.readline())
            print(f"Your current balance: ${balance}")
    else:
        print("Account not found.")
        create_account(account_number)
def deposit(account_number, amount):
    filename = f"{account_number}.txt"
    if os.path.exists(filename):
        with open(filename, "r+") as file:
            balance = float(file.readline())
            balance += amount
            file.seek(0)
            file.write(str(balance))
            file.truncate()
            print(f"Deposit successful. New balance: ${balance}")
    else:
        print("Account not found.")
def withdraw(account_number, amount):
    filename = f"{account_number}.txt"
    if os.path.exists(filename):
        with open(filename, "r+") as file:
            balance = float(file.readline())
            if balance >= amount:
                balance -= amount
                file.seek(0)
                file.write(str(balance))
                file.truncate()
                print(f"Withdrawal successful. Remaining balance: ${balance}")
            else:
                print("Insufficient funds.")
    else:
        print("Account not found.")
def transfer(sender_account, receiver_account, amount):
    sender_file = f"{sender_account}.txt"
    receiver_file = f"{receiver_account}.txt"
    if os.path.exists(sender_file) and os.path.exists(receiver_file):
        with open(sender_file, "r+") as sender, open(receiver_file, "r+") as receiver:
            sender_balance = float(sender.readline())
            receiver_balance = float(receiver.readline())
            if sender_balance >= amount:
                sender_balance -= amount
                receiver_balance += amount
                sender.seek(0)
                sender.write(str(sender_balance))
                sender.truncate()
                receiver.seek(0)
                receiver.write(str(receiver_balance))
                receiver.truncate()
                print("Transfer successful.")
            else:
                print("Insufficient funds for transfer.")
    else:
        print("One or both accounts not found.")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            account_number = input("Enter your account number: ")
            create_account(account_number)
        elif choice == "2":
            account_number = input("Enter your account number: ")
            check_balance(account_number)
        elif choice == "3":
            account_number = input("Enter your account number: ")
            amount = float(input("Enter the amount to withdraw: "))
            withdraw(account_number, amount)
        elif choice == "4":
            sender_account = input("Enter your account number: ")
            receiver_account = input("Enter recipient's account number: ")
            amount = float(input("Enter the amount to transfer: "))
            transfer(sender_account, receiver_account, amount)
        elif choice == "5":
            account_number = input("Enter your account number: ")
            amount = float(input("Enter the amount to deposit: "))
            deposit(account_number, amount)
        elif choice == "6":
            print("Exiting...")
            print("Exited Successfully")
            print("Thank you for using Bank Management System BMS")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()