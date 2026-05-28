""""
Rock smashes scissors.
Paper covers rock.
Scissors cut paper.

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
"""
import random

def play():

    choices = ["rock", "paper", "scissors"]

    # Welcome message and rules
    print("\n--- Rock, Paper, Scissors ---\n")
    print("Rules are simple:")
    print("Rock smashes scissors.")
    print("Paper covers rock.")
    print("Scissors cut paper.\n")
    print("Best out of 3 wins! Let's play!")
    print("Type 'quit' to exit game.\n")

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)

    # Check if the choices are valid
    if user_choice not in choices:
        return "Invalid choice. Please choose rock, paper, or scissors."

    result = determine_winner(user_choice, computer_choice)
    print(result)

def determine_winner(user_choice, computer_choice):
    # Determine a Winner
    if user_choice == computer_choice:
        return "Its a tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return f"You win! {user_choice.capitalize()} beats {computer_choice.capitalize()}."
    else:
        return f"Computer wins! {computer_choice.capitalize()} beats {user_choice}."

if __name__ == "__main__":
    play()