import random

A = int(input("enter value [1]: "))

AA = random.choice(["A","B"])

if A == 1:
    print(f"Your in {AA}")

B = input("Choose the field [Batting,Bowling] : ") 

Runs = random.choice([1,2,3,4,5,6,])

ball = 1
1,2,3,4,5,6

if B == "Bowling":
    Overs = input("Throw your 1st ball :")
    print("Match Start")
    if Overs >= ball:
        print("your ball's over limit is 6 only")
    if Overs == ball:
        print(f"Your score is {Runs}")