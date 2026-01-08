class Teacher:
    def __init__(self,salery):
        self.salery = salery
class Student():
    def __init__(self,gpa):
        self.gpa = gpa
class TA(Teacher,Student):
    def __init__(self,salery,gpa,name):
        super().__init__(salery)
        Student.__init__(self,gpa)
        self.name = name

t1 = TA(125000,54,"AKash")
print(t1.name,t1.salery,t1.gpa)


        