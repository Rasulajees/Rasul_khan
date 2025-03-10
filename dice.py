import random
options =["1","2","3","4","5","6"]

user_choice=input("choice[1,2,3,4,5,6]:")
computer_choice=random.choice(options)

print("your choice:", user_choice)
print("computer choice:", computer_choice)

if user_choice ==computer_choice:
    print("It's tie")

elif user_choice > computer_choice:
    print("you win!")

elif user_choice < computer_choice:
    print("computer win!")

elif user_choice !=options:
    print("Invalid, please choose the option value between 1 and 6.")
else:
    print("Invalid ,please chooose the option valuse:") 