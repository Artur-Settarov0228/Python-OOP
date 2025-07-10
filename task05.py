class Product:
    def __init__(self , name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

product_1 = Product("Smartfon" , 12999.99 , "electronics", True)
product_2 = Product("Stol" , 500_000 , "furniture" , False)

print("Mahsulot 1:", product_1.name, "-", product_1.price, "so'm")
print("Mahsulot 2:", product_2.name, "-", product_2.price, "so'm")     

        