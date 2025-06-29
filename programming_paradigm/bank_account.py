class BankAccount:
    def __init__(self, balance=0):
        self.account_balance= float(balance)
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += float(amount)
    def withdraw(self, amount): 
        if 0 < amount  <= self.account_balance:
            self.account_balance -= float(amount)
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")