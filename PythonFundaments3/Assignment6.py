"""
Docstring for Python.PythonFundaments3.Assignment6
Create a class Person that allows the constructor to work with:
• name only
• name + age
• name + age + address
As direct constructor overloading (multiple constructors) are not allowed but
we have to use default parameters to simulate constructor overloading
"""


class Person:
    def __init__(self,name,age=None,address=None):
        self.name = name
        self.age = age
        self.address = address

    def Display_details(self):
        if self.name is not None:
            print(f"Name is: {self.name}")
        if self.age is not None:
            print(f"Name is: {self.age}")
        if self.address is not None:
            print(f"Name is: {self.address}")

p = Person("Akash",23,"Greater Noida")
p.Display_details()



        

        