class BankAccount:
    def __init__(self , owner ,balance ):
        self.owner = owner
        self.balance = balance


    def deposit(self ,amount):
        self.balance += amount
        print(f"{amount} som  qoshildi. Yangi balance {self.balance}")

    def withdraw( self , amount):
        if self.balance >=amount:
            self.balance -=amount
            print(f"{amount} balance yechildi .Qolgan balance {self.balance} ")

    def show_balance(self):
        print(f"{self.owner} hisobida: {self.balance} som mavjud.")
           
acc1 = BankAccount("Ali", 100000)
acc2 = BankAccount("Laylo", 50000)
acc3 = BankAccount("Bekzod", 200000)

acc1.deposit(50000)       
acc1.withdraw(20000)     

acc2.deposit(10000)       
acc2.withdraw(80000)      

acc3.withdraw(50000)     
acc3.deposit(20000)       


acc1.show_balance()
acc2.show_balance()
acc3.show_balance()           

