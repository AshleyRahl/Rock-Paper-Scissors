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
    # Initialize scores and choices
    user_score = 0
    computer_score = 0

    choices = ["rock", "paper", "scissors"]

    # Welcome message and rules
    print("\n--- Rock, Paper, Scissors ---\n")
    print("Rules are simple:")
    print("- Rock smashes scissors.")
    print("- Paper covers rock.")
    print("- Scissors cut paper.\n")
    print("Best out of 3 wins! Let's play!")
    print("Type 'quit' to exit game.")

    while user_score < 3 and computer_score < 3:
        
        print(f"\nCurrent Score -> You: {user_score} | Computer: {computer_score}")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = random.choice(choices)

        if user_choice == "quit" or user_choice == "q":
            print("Thanks for playing!")
            return # This exit function
        
        # Check if the choices are valid
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")

        # Get the result of the round and update scores
        result = determine_winner(user_choice, computer_choice)
        if result.startswith("You win"):
            user_score += 1
        elif result.startswith("Computer wins"):
            computer_score += 1
        print(result)


    # Announce the final winner
    print(f"\nFinal Score -> You: {user_score} | Computer: {computer_score}")
    if user_score == 3:
        print("CONGRATULATIONS! You won!")
    else:
        print("Computer Won! Better luck next time!")

    print("Thanks for playing! Good Guy")


def determine_winner(user_choice, computer_choice):
    # Determine a Winner
    if user_choice == computer_choice:
        return "Its a tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return f"You win! {user_choice.capitalize()} beats {computer_choice.capitalize()}."
    else:
        return f"Computer wins! {computer_choice.capitalize()} beats {user_choice.capitalize()}."

if __name__ == "__main__":
    play()