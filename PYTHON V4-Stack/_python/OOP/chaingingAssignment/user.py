
class User:

    def __init__(self,name,email,balance = 0) :
        self.name = name
        self.email = email
        self.account_balance = balance



    def deposit(self, amount):
        self.account_balance += amount
        print(self.account_balance)
        return self

    def withdrawal(self,amount):
        self.account_balance -= amount
        print(self.account_balance)
        return self

    def display(self):
        print(self.name,self.account_balance)
        return self

Aziza=User("Aziza", "az@mail.co",500)
Reemas=User("Remaas","re@mail.co",200)
Awatif=User("Awatis","af@mail.co",1000)

Aziza.deposit(1000).deposit(200).deposit(800).withdrawal(1000).display()
Reemas.deposit(300).deposit(700).withdrawal(150).withdrawal(50).display()
Awatif.deposit(1500).withdrawal(200).withdrawal(100).withdrawal(20).display()

