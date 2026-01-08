class Employee:
    Start_time = "10am"
    End_time = "4pm"

class Admin(Employee):
    def __init__(self,roll):
        self.roll = roll

class Account(Admin):
    def __init__(self, roll,salery):
        super().__init__(roll) 
        self.salery = salery

Ac1 = Account("CA",25000)
print(Ac1.roll,Ac1.salery,Ac1.Start_time,Ac1.End_time)