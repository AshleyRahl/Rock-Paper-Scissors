""""
Rock smashes scissors.
Paper covers rock.
Scissors cut paper.

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
"""
import random
choices = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

computer_choice = random.choice(choices)

# Check if the choices are valid
if user_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")

if user_choice == computer_choice:
    print("Its a tie")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print(f"You win! {user_choice.capitalize()} beats {computer_choice.capitalize()}.")
else:
    print(f"Computer wins! {computer_choice.capitalize()} beats {user_choice}.")
