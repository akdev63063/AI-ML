"""Concept: Classes & Objects
    Create a class with and 
Q1 BankAccount attributes account_number owner_name balance
methods deposit withdraw check Balance """
class BankAccount:
    def __init__(self,Owner_name,Acc_no,Balance = 0):
        self.Owner_name = Owner_name
        self.Acc_no = Acc_no
        self.Balance = Balance

    def deposit(self,amount):
        if amount > 0:
            self.Balance += amount
            print(f"{amount} Successfully Deposit")
        else:
            print("Amount must we Postive")

    def Withdrawl(self,amount):
        if amount <= self.Balance:
            self.Balance -= amount
            print(f"{amount} Successfully Withdrawl")
        elif amount < 0:
            print('Enter Postive Amouunt')
        else:
            print('Balance Insufficient')

    def Check_Balance(self):

        print("Current Balance: ",self.Balance)

    def Show_Customer_details(self):
        print('Customer Name : ',self.Owner_name)
        print('Customer Account Number : ',self.Acc_no)
        print('Customer Account Balance : ',self.Balance)


b1 = BankAccount('Akash',123456789,5000)
b1.deposit(5000)
b1.Withdrawl(4000)
b1.Check_Balance()
b1.Show_Customer_details()









        