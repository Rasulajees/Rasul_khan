# 1st movie ticket based program
"""
#1st Exercise:
#moive tickets:

print("\nWelcome to PVR cinimas!\n")

print(input("Choose your movie:"))

print("select the seats: ")

print(f"balcony{1}",f"Primium{2}",f"economy{3}",f"budjet{4}")

balcony=int(input("balcony:"))

Premium=int(input("Premium:"))

economy=int(input("economy:"))

budjet=int(input("budjet:"))

if balcony<=1:
   price_per_ticket=print("The price for balcony tickets is 250.00")

elif Premium<=2:
    price_per_ticket=print("The price for primium tickets is 200.00")

elif economy<=3:
    price_per_ticket=print("The price for economy tickets is 150.00")

elif budjet<=4:
    price_per_ticket=print("The price for buject tickets is 100.00")

else:
    print("Please select your seats!")
   
    
#movie ticket price calculation:
def calculate_total_cost(num_tickets, price_per_ticket):
    total_cost = num_tickets * price_per_ticket
    return total_cost
def main():
    print("Welcome to the Movie Ticket Calculator!")


    try:
        num_tickets = int(input("Enter the number of tickets: "))
        price_per_ticket = float(input("Enter the price per ticket: "))

        if num_tickets < 0 or price_per_ticket < 0:
            print("The number of tickets and the price per ticket must be non-negative.")
        else:
            total_cost = calculate_total_cost(num_tickets, price_per_ticket)
            print(f"The total cost for {num_tickets} ticket(s) at {total_cost:.2f} per ticket is {price_per_ticket:.2f}.")
    except ValueError:
        print("Please enter valid numbers for the number of tickets and the price per ticket.")

if __name__ == "__main__":
    main() 
"""

#2nd Exercise
"""
while True:
    print("\n Company name")
    print("\n XYZ Solutions")
    print("\n Performance Appraisal")
    print("Please Enter Employee Name:\n")
    employee1= "Rasul khan"
    employee2= "vijay"
    employee3= "Renesh"
    employees= input()
    print("Please Enter Employee's Achieved:\n")
    employee_achived= int(input())

    if employees == "Rasul khan" and employee_achived > 50000:
        print("Well Done Mr. Rasul khan - You got Increment amount Rs. 10000")

    elif employees == "Vijay" and employee_achived > 40000:
        print("Well Done Vicky - You got Increment amount Rs. 8000")

    elif employees == "Renesh" and employee_achived > 30000:
        print("Well Done Mr. Maddy - You got Increment amount Rs. 6000")
        
    else:
        print("Better Luck Next Time ")
        break
"""


#3rd Exercise
"""
number = [10,20,30,40,50,60,70,80,90,100]
ab = 0
for i in number:
    ab+=i
    print(ab)
"""

#4th Exercise
"""
for i in range(1,11):
    print(i,"x 2 =",i*2)
"""

#5th Exercise
"""
import random
print("\nParis Olympics 2024")
print("Game\n")
print("Enter Your Name:\n")
s= input()
print("Enter Your Game:\n")
a= input()
game= ["High Jump", "poll ward", "10m Shooting"]
print("Which Medal Do You won:")
c= input()
Overall_medal= ["Gold", "Silver", "Bronze"]

if "High Jump" in game and c == "Gold":
    print(f"Oh You Won Gold Medal and Rs. 5 Lakhs for Your Country - {s} ")
elif "javelling Throw" in game and c == "Silver":
    print(f"Wow You Won Silver Medal and Rs. 2.5 Lakhs for Your Country - {s}")
elif "10m Shooting" in game and c == "Bronze":
    print(f"You Won Bronze Medal and Rs. 1 Lakh for Your Country - {s}")
print("Game\n")
print("Enter Your name:\n")
ss= input()
print("Enter Your Game:\n")
game= ["High Jump", "javelling Throw", "10m Shooting"]
b= input()
print("Which Medal Do You won:")
cc= input()
if "High Jump" in game and cc == "Gold":
    print(f"Oh You Won Gold Medal and Rs. 5 Lakhs for Your Country - {ss}")
elif "javelling Throw" in game and cc == "Silver":
    print(f"Wow You Won Silver Medal and Rs. 2.5 Lakhs for Your Country- {ss}")
elif "10m Shooting" in game and cc == "Bronze":
    print(f"You Won Bronze Medal and Rs. 1 Lakh for Your Country - {ss}")
else:
    print("Please Enter Your Valid Input")
"""


#6th Exercise

"""
print("Thinks Shopping Mall")
a= ["T-shirts", "Shirts", "Pants"]
print("Enter Your Product:")
aa=input()
print("Enter Your Personal Sale")
b= int(input())
if "T-shirts" in a and b >= 100000:
    print("Wow, You Have High sale Perfromance - Congrats Mr. Rasul")
elif "T-Shirts" in a and b < 100000:
    print("Oh You Have Good Sale Perfromance - Mr. Rasul")
elif "T-Shirts" in a and b < 50000:
    print("No!! You Have Poor Performance - Mr. Rasul")
elif "Shirts" in a and b >= 100000:
    print("Wow, You Have High sale Perfromance - Congrats Mr. Rasul")
elif "Shirts" in a and b < 100000:
    print("Oh You Have Good Sale Perfromance - Mr. Rasul")
elif "Shirts" in a and b < 50000:
    print("No!! You Have Poor Performance - Mr. Rasul")
elif "Pants" in a and b >= 100000:
    print("Wow, You Have High sale Perfromance - Congrats Mr. Rasul")
elif "Pants" in a and b < 100000:
    print("Oh You Have Good Sale Perfromance - Mr. Rasul")
elif "Pants" in a and b < 50000:
    print("Oh You Have Good Sale Perfromance - Mr. Rasul")
else:
    print("Please Enter Your Valid Input")
"""

#07th Exercise
"""
print("Enter Your School Name:")
a=input()
print("Enter Your Class:")
b= input()
print("Enter Your Name:")
c= input()
print("Enter Your Percentage Rate:")
d=float(input())
total_percentage = 100

if  d >= 95:
    print("OH, You are a O+ Grade Student")
elif d >= 90:
    print(" Oh, You are a O Grade Student")
elif d >= 80:
    print("Oh, You are a A Grade Student")
elif d >= 70:
    print("Wow, You are a B Grade Student")
elif d >= 60:
    print("You are a C Grade Student ")
elif d >= 51:
    print("You are a D Grade Student")
elif d >= 50:
    print("You are Fail - Needs Improvement")
else:
    print("Please Enter Your Valid Input")
"""

#08th Exercise

"""
print("a")
a = int(input())
print("b")
b = int(input())

if a%b:
    0>a
    print("this is a prime number")
else:
    print("this is not a prime number")
"""

#09th Exercise
"""
a= [10,20,30,40,50]
#max
b= max(a)
print("Max")
bb=input(b)
#min
c=min(a)
print("Min")
cc=input(c)
#len
print("Len")
print(input(len(a)))
#sum
e=a[0]+a[1]+a[2]+a[3]+a[4]
ee=e
print("Sum")
print(e)
# count
f= a[0-5]
print("Count")
print(input(f))
#abs
print("ABS")
a = [-10, -20, -30, -40, -50]
abs_values = [abs(x) for x in a]
print(abs_values)
"""

#10th Exercise
"""
print("Cardia Disease clinic:\n")
print("Presents\n")
print("Heart Disease Camp - Who are all affecting in Heart Disease come here to cure your problems\n")

low_respiration_rate_for_Adult = (0 <= 12)
normal_respiration_rate_for_Adult = (12 <= 20)
high_respiration_rate_for_Adult = (20 < 25)

low_respiration_rate_for_Child = (0 <= 20)
normal_respiration_rate_for_Child = (20 <= 30)
high_respiration_rate_for_Child = (30 < 40)

child_min_age = 0
child_max_age = 17 
adult_min_age = 18
adult_max_age = 60

print("Enter Your Good Name:\n")
a = input()
print("Enter Your Age: \n")
b = int(input())  
print("Are You Affected by Respiratory Problems? (Yes/No): \n")
c = input()
print("Please Enter Your Respiration Rate: \n")
d = int(input())  


if child_min_age <= b <= child_max_age:  
    if low_respiration_rate_for_Child and d < 20:
        print("You Have Low Respiration Problem - Visit Dr. Rasul khan to cure your problem.")
    elif normal_respiration_rate_for_Child and 20 <= d <= 30:
        print("You Have Normal Respiration.")
    elif high_respiration_rate_for_Child and d > 30:
        print("You Have High Respiration Problem - Visit Dr. Rasul khan to cure your problem.")
    else:
        print("Please provide your correct respiration rate.")

# Check if the person is an adult
elif adult_min_age <= b <= adult_max_age:  
    if low_respiration_rate_for_Adult and d < 12:
        print("You Have Low Respiration Problem - Visit Dr. Rasul khan to cure your problem.")
    elif normal_respiration_rate_for_Adult and 12 <= d <= 20:
        print("You Have Normal Respiration.")
    elif high_respiration_rate_for_Adult and d > 20:
        print("You Have High Respiration Problem - Visit Dr. Rasul khan to cure your problem.")
    else:
        print("Please provide your correct respiration rate.")
else:
    print("Please provide your correct age.")
"""