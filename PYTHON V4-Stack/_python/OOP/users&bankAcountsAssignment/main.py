from user import User
from bankAccount import BankAccount

#create instances of class User
Sara = User("Sara")
Aziza = User("Aziza")

#create instances of class BankAccount
checking = BankAccount('Checking',0.001)
savings = BankAccount('Savings',0.004)

Sara.make_deposit(500,checking).make_deposit(500,checking).make_deposit(100,savings).make_withdrawal(200,savings).account.yield_interest()
Sara.display_user_balance()
Aziza.make_deposit(300,checking).make_deposit(150,savings).make_deposit(200,savings).make_withdrawal(50,checking).account.yield_interest()
Aziza.display_user_balance()