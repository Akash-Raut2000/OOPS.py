class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds!")

# Create an account for a user
my_account = BankAccount("Alice", 1000)

# Perform operations
my_account.deposit(500)  # Depositing money
my_account.withdraw(200)  # Withdrawing money
my_account.withdraw(1500)  # Attempting to overdraw
