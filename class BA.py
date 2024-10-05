# Define the BankAccount class with various methods to manage an account
class BankAccount:
    # Constructor to initialize an account with a number and an optional initial balance
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Set the account number
        self.balance = balance              # Set the initial balance

    # Method to deposit a specified amount into the account
    def deposit(self, amount):
        self.balance += amount  # Increase the balance by the deposit amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    # Method to withdraw a specified amount from the account
    def withdraw(self, amount):
        if self.balance >= amount:  # Check if sufficient funds are available
            self.balance -= amount  # Decrease the balance by the withdrawal amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")  # Notify if there are not enough funds

    # Method to transfer a specified amount to another account
    def transfer(self, recipient, amount):
        if self.balance >= amount:  # Check if sufficient funds are available
            self.balance -= amount  # Decrease the balance by the transfer amount
            recipient.balance += amount  # Increase the recipient's balance
            print(f"Transferred ${amount} to account {recipient.account_number}")
        else:
            print("Insufficient funds")  # Notify if there are not enough funds

    # Method to check the current balance of the account
    def check_balance(self):
        print(f"Account Balance: ${self.balance}")

# Main code to demonstrate the functionality of the BankAccount class
if __name__ == "__main__":
    # Create two BankAccount instances
    account1 = BankAccount("12345")  # Account with default balance of 0
    account2 = BankAccount("67890", 1000)  # Account with initial balance of 1000

    # Perform various operations on the accounts
    account1.deposit(500)  # Deposit 500 into account1
    account2.deposit(200)  # Deposit 200 into account2
    account1.withdraw(200)  # Withdraw 200 from account1
    account2.withdraw(400)  # Withdraw 400 from account2
    account1.transfer(account2, 300)  # Transfer 300 from account1 to account2
    account1.check_balance()  # Check balance of account1
    account2.check_balance()  # Check balance of account2