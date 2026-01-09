"""
Docstring for Python.PythonFundaments3.Assignment5
Concept: Inheritance
Q5. Create a base class Vehicle with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes - seats (in Car) & engine_cc (in Bike).
"""
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model,seats,engine):
        super().__init__(brand, model)
        self.seats = seats
        self.engine = engine

    def Car_deatils(self):
        return print(f"Car Brand {self.brand} ,Car Model {self.model} ,Seats in car {self.seats}, Engine in CC {self.engine}")
    
class Bike(Vehicle):
    def __init__(self, brand, model,seats,engine):
        super().__init__(brand, model)
        self.seats = seats
        self.engine = engine
        

    def Bike_deatils(self):
        return print(f"Bike Brand {self.brand} ,Bike Model {self.model} ,Seats in Bike {self.seats}, Engine in CC {self.engine}")

c = Car("Verna",2026,4,1200)
b = Bike("Honda",2026,2,450)
c.Car_deatils()
b.Bike_deatils()




        
