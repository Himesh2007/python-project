class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")
    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred ${amount} to account {recipient.account_number}")
        else:
            print("Insufficient funds")
    def check_balance(self):
        print(f"Account Balance: ${self.balance}")
if __name__ == "__main__":
    account1 = BankAccount("12345")
    account2 = BankAccount("67890", 1000)
    account1.deposit(500)
    account2.deposit(200)
    account1.withdraw(200)
    account2.withdraw(400)
    account1.transfer(account2, 300)
    account1.check_balance()
    account2.check_balance()