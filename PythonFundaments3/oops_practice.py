class Product:
    count = 0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count += 1

    def get_info(self):
        print(f"Name of Product {self.name} and Price {self.price}")
    @classmethod
    def get_count(self):
        print(f"Total count of Product : {Product.count}")
    @staticmethod
    def cal_discount(price,Discount):
        print(f"Discount is {price -(price * Discount/ 100)}")

    

P1 = Product("Laptop",30000)
P1.get_info()
P1.get_count()
P1.cal_discount(30000,10)
        