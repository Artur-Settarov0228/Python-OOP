class Car:
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

car_1 = Car("Bmw" , "m5" , "2018")
print(f"{car_1.brand} , {car_1.model} ,{car_1.year}")      