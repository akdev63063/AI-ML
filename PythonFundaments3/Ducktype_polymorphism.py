class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher():
    def get_designation(self):
        print("Designation = Teacher")

t1 = Teacher()
t1.get_designation()

e1 = Employee()
e1.get_designation()