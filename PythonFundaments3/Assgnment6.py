"""
Docstring for Python.PythonFundaments3.Assgnment6
|
Concept: Abstraction
Q6. Create an abstract class Employee with an abstract method calculate_salary().
Create subclasses Intern, FullTimeEmployee, and Contract Employee that implement the method differently.
"""

from abc import ABC , abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self,stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    
class FullTimeEmployee(Employee):
    def __init__(self,basic,hra,da):
        self.basic = basic
        self.hra = hra
        self.da = da

    def calculate_salary(self):
        return self.basic+self.hra+self.da
    
class Contract_Employee(Employee):
    def __init__(self,hour,day):
        self.hour = hour
        self.day = day

    def calculate_salary(self):
        return 50 * self.hour + 500 * self.day
    
print("Intern Salary:", Intern(10000).calculate_salary())
print("Full Time Salary:", FullTimeEmployee(20000,5000,5000).calculate_salary())
print("Contract Salary:", Contract_Employee(20,24).calculate_salary())

