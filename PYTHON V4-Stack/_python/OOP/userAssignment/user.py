
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

Aziza.deposit(1000)
Aziza.deposit(200)
Aziza.deposit(800)
Aziza.withdrawal(1000)
Aziza.display()
Reemas.deposit(300)
Reemas.deposit(700)
Reemas.withdrawal(150)
Reemas.withdrawal(50)
Reemas.display()
Awatif.deposit(1500)
Awatif.withdrawal(200)  
Awatif.withdrawal(100)
Awatif.withdrawal(20)
Awatif.display()

