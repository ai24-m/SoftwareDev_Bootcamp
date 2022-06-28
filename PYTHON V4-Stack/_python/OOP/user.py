

class User:

    def __init__(self,name,account_balance=0):
        self.name = name
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount
        print(self.account_balance)
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount 
        print(self.account_balance)
        return self

    def display(self):
        print(self.name,self.account_balance)
        return self

S=User('Mark',3000)
M=User('Jill',2000)
N=User('Ramsy',1000)

S.deposit(600)
S.deposit(100)
S.deposit(70)
S.make_withdrawl(50)
S.display()
M.deposit(100)
M.deposit(90)
M.make_withdrawl(300)
M.make_withdrawl(30)
M.display()
N.deposit(300)
N.make_withdrawl(100)
N.make_withdrawl(100)
N.make_withdrawl(100)
N.display()