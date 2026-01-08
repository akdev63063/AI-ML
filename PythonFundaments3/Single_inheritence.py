class Employee:
    start_time = 10
    End_time = 4

class Teacher(Employee):
    def __init__(self,subject):
        self.subject= subject

t1 = Teacher("Mathe")
print(t1.subject,t1.start_time,t1.End_time)
        