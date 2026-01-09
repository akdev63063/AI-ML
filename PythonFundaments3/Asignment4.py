"""
Docstring for Python.PythonFundaments3.Asignment4
Concept: Function Overriding 
Create a class Shape with a method area().
Create subclasses Circle,Rectangle and Triangle that the area()
method.
"""
import math
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self,len,bre):
        self.len = len
        self.bre = bre
    
    def area(self):
        return self.len * self.bre
    
class Triangle(Shape):
    def __init__(self,base,high):
        self.base  = base
        self.high = high

    def area(self):
        return (1/2) * self.base * self.high 

   
c1 = Circle(4)
r1 = Rectangle(2,3)
t1 = Triangle(5,2)
print("Area of Circle : ",c1.area())
print("Area of Rectangle : ",r1.area())
print("Area of Triangle : ",t1.area())





        
        

    
