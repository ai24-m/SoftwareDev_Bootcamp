

class BankAccount:

    def __init__(self,name, int_rate=0.05,balance=0): 
        self.name = name
        self.intRate=int_rate
        self.account_balance=balance



    def deposit(self,amount):
        self.account_balance += amount
        return self


    def withdrawal(self,amount):
        if amount > self.account_balance:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance = self.account_balance - 5
        else:
            self.account_balance -= amount
        return self 

        # self.account_balance -= amount
        # print(self.account_balance)
        # return self


    def display(self):
        print (self.name,self.account_balance)
        return self
    

    # def display(self):
    #     print (f" Current {self.name}, Balance:${self.account_balance} ")
    #     return self
    
    

    def yield_interest(self):
        self.account_balance *= (1+int(self.intRate))
        return self


# Aziza=BankAccount("Aziza",0.006)
# Awatif=BankAccount("Awatif",balance=1000)


# Aziza.deposit(1000).deposit(560).deposit(80).withdrawal(980).yield_interest().display()
# Awatif.deposit(200).deposit(200).withdrawal(20).withdrawal(10).withdrawal(20).withdrawal(10).yield_interest().display()