"""
Docstring for Python.PythonFundaments3.Assignment3
Concept: Encapsulation
Create a class with Student private attributes _name, _roll_no, and _marks.
Provide and methods with validation (e.g., marks cannot be
negative, roll number has to be between 1 & 100 & name cannot be empty).
"""

class Student:
    def __init__(self,name,roll_no,marks):
        self._name = name 
        self._roll_no = roll_no
        self._marks = marks 

    def set_name(self,name):
            if self._name == " ":
                print('Name is not empty')
            else:
                self._name = name 

    def get_name(self):
         print("Name is : ",self._name)

    def set_roll(self,roll_no):
        if self._roll_no == " ":
                print('roll_no is not empty')
        else:
            self._roll_no = roll_no 

    def get_roll(self):
        print("Roll number is : ",self._roll_no)

    def set_mark(self,marks):
        if self._marks == 0 :
              print("Marks is not Zero ")

        else:
             self._marks = marks

    def get_marks(self):
         print("Marks is : ", self._marks)
         
             

s1 = Student("Akash",46,95)
s1.get_name()
s1.get_roll()
s1.get_marks()
        
        



    


