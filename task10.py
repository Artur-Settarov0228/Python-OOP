class BankAccount:
    def __init__(self , ower, balance):
        self.ower = ower
        self.balance = balance

    def deposit(self ,amount):
        self.balance += amount
        print(f"{amount} som  qoshildi. Yangi balance {self.balance}")

    def withdrow(self , amount):
        if self.balance >=amount:
            self.balance -=amount
            print(f"{amount} balance yechildi .Qolgan balance {self.balance}   ")


        else:
            print("yetarli balance mavjut emas")

p_1 = BankAccount("Artur" , 1_000_000)

p_1.deposit(5000)
p_1.withdrow(2000)
p_1.withdrow(5000)

            
