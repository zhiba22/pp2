#BANK ACCOUNT
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied! Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance = {self.balance}")

acc = Account("Alice", 100)

acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  
