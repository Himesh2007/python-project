import os

# Function to display the menu options
def display_menu():
    print("Bank Management System")
    print("1. Create account")
    print("2. Check Balance")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Deposit")
    print("6. Exit")

# Function to create a new account
def create_account(account_number):
    owner_name = input("Enter your name: ")
    initial_balance = float(input("Enter your initial balance: "))
    filename = f"{account_number}.txt"  # File to store the account's balance
    with open(filename, "w") as file:
        file.write(str(initial_balance))  # Write initial balance to the file
    print("Account created successfully!")

# Function to check the balance of an account
def check_balance(account_number):
    filename = f"{account_number}.txt"
    if os.path.exists(filename):  # Check if the account file exists
        with open(filename, "r") as file:
            balance = float(file.readline())  # Read balance from the file
            print(f"Your current balance: ${balance}")
    else:
        print("Account not found.")
        create_account(account_number)  # Offer to create an account if not found

# Function to deposit money into an account
def deposit(account_number, amount):
    filename = f"{account_number}.txt"
    if os.path.exists(filename):  # Check if the account file exists
        with open(filename, "r+") as file:
            balance = float(file.readline())  # Read current balance
            balance += amount  # Update balance with deposit amount
            file.seek(0)  # Move to the start of the file
            file.write(str(balance))  # Write updated balance to the file
            file.truncate()  # Remove any old data
            print(f"Deposit successful. New balance: ${balance}")
    else:
        print("Account not found.")

# Function to withdraw money from an account
def withdraw(account_number, amount):
    filename = f"{account_number}.txt"
    if os.path.exists(filename):  # Check if the account file exists
        with open(filename, "r+") as file:
            balance = float(file.readline())  # Read current balance
            if balance >= amount:  # Check if sufficient funds are available
                balance -= amount  # Deduct withdrawal amount
                file.seek(0)  # Move to the start of the file
                file.write(str(balance))  # Write updated balance to the file
                file.truncate()  # Remove any old data
                print(f"Withdrawal successful. Remaining balance: ${balance}")
            else:
                print("Insufficient funds.")
    else:
        print("Account not found.")

# Function to transfer money between two accounts
def transfer(sender_account, receiver_account, amount):
    sender_file = f"{sender_account}.txt"
    receiver_file = f"{receiver_account}.txt"
    if os.path.exists(sender_file) and os.path.exists(receiver_file):  # Check if both account files exist
        with open(sender_file, "r+") as sender, open(receiver_file, "r+") as receiver:
            sender_balance = float(sender.readline())  # Read sender's balance
            receiver_balance = float(receiver.readline())  # Read receiver's balance
            if sender_balance >= amount:  # Check if sender has sufficient funds
                sender_balance -= amount  # Deduct amount from sender
                receiver_balance += amount  # Add amount to receiver
                sender.seek(0)  # Move to the start of the sender file
                sender.write(str(sender_balance))  # Write updated balance to sender file
                sender.truncate()  # Remove any old data
                receiver.seek(0)  # Move to the start of the receiver file
                receiver.write(str(receiver_balance))  # Write updated balance to receiver file
                receiver.truncate()  # Remove any old data
                print("Transfer successful.")
            else:
                print("Insufficient funds for transfer.")
    else:
        print("One or both accounts not found.")

# Main function to manage the bank system
def main():
    while True:
        display_menu()  # Display menu options
        choice = input("Enter your choice: ")  # Get user's choice
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

# Run the main function when the script is executed
if __name__ == "__main__":
    main()