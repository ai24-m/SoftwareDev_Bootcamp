from bankAccount import BankAccount

class User:

    def __init__(self,name) :
        self.name = name
        self.account = BankAccount(name ,int_rate=0.004,balance=0)
    def make_deposit(self, amount, name):
        self.account.deposit(amount, name) 
        return self
    def make_withdrawal(self,amount, name ):
        self.account.withdrawal(amount, name)
        return self
    def display_user_balance(self):
        print("User: " + self.name)
        self.account.display_account_info()
        return self

