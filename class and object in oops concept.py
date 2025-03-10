#ex:1
#class definion:
"""class Car:
    
    def __init__(self,brand):
        self.brand=brand
    #self.model=Model


    def display(self):
        print(f"car brand:{self.brand}")

    def color(self):
        print("my fevourite color is red")

#object creation:
car1=Car(input("Enter the car brand:"))
#car2=Car("Audi","A4")


car1.display()
car1.color()

"""
#ex:2
#Bank Account:
"""
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def display_balance(self):
        print(F"{self.name}'s Balance:{self.balance}")

Account1=BankAccount("Rasul",17000)
Account1.display_balance()
"""

#ex:3
#student grades:
"""
class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def display_info(self):
        print(f"Student Name:{self.name}")
        print(f"grade:{self.grade}")

student1=student("Rasul",90)
student1.display_info()
"""

#ex:4
#mobile:
"""
class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.prince=price

    def display_info(self):
        print(f"brand:{self.brand}")
        print(f"price:{self.prince}")

mobile1=mobile("Iphone 15 pro",132000)
mobile1.display_info()
"""

#ex:5
#student mark:

"""class student:
    def __init__(self,name,roll_no,mark):
        self.name=name
        self.roll_no=roll_no
        self.mark=mark

    def dispalyself(self):
        print(f"Name:{self.name}")
        print(f"Roll_no:{self.roll_no}")
        print(f"Mark:{self.mark}") 

    def check_pass(self):
        if self.mark>=35:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

student1=student("Rasul",1,90)
student2=student("jeva",2,30)

student1.dispalyself()
student2.dispalyself()

student1.check_pass()
student2.check_pass()"""

#ex:6
#cash deposit:
"""
class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited successfully")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"{amount}Withdrawn successfully")
        else:
            print("Insufficient balance")
    
    def display_balance(self):
        print(f"{self.name}'s  current balance:{self.balance}")

#creating objects:

account=bankaccount("Rasul",15000)
account.deposit(float(input("Enter the deposit amount: ")))
account.withdraw(float(input("Enter the withdraw amount: ")))

account.display_balance()"
"""

#ex:7
#snack:

class snack:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def display(self):
        print(f"Name:{self.name}")
        print(f"Price:{self.price}")

#list of snacks items:

snacks=[
    snack("chips",10),
    snack("burger",60),
    snack("Pizza",99),
    snack("samosa",20),
    snack("cake",50)
]
#random select a snack item;
import random
random_snack=random.choice(snacks)
print("random selected snack item:")
random_snack.display()

