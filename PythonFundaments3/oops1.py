class Bankaccount:
    def __init__(self,name,Balance):
        self.name=name
        self.__balance=Balance

    def show(self):
        print(f"Costumer name is {self.name} and Balace is {self.__balance}")

c1 = Bankaccount("Akash",30000)
c1.show()