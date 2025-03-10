import random

options =["Rock","paper","scissor"]

user_choice =input("Choose [rock, paper, scissor]:")
computer_choice = random.choice(options)

print("You choice:",user_choice)
print("Computer choice:",computer_choice)

if user_choice == computer_choice:  
    print("It's a tie!")

elif user_choice=="rock" and computer_choice=="scissor":
    print("You win!")
elif user_choice=="paper" and computer_choice=="rock":
    print("You win!")
elif user_choice=="scissor" and computer_choice=="paper":
    print("You win!")

else:
    print("Computer wins!")              