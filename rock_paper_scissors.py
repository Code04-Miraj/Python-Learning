# Program Flow:

    # Define emojis for rock, paper, scissors
    # Define rules (what beats what)

    # Define a function to get user input
        # Ask user to enter rock/paper/scissors
        # If input is invalid, raise error

    # Define a function to get computer's random choice

    # Define a function to decide winner
        # If same: draw
        # Else: check rules to determine win/loss

    # Main game function:
        # Loop forever:
            # Try getting user input
                # If invalid, print error and continue loop
            # Get computer choice
            # Print both choices with emojis
            # Print result (win/loss/draw)
            # Ask if user wants to play again
            # If not, break loop and end game

# self written project

import random

# emoji choices
emoji = {
    "rock": "🪨",
    "paper": "📃",
    "scissors": "✂️"
}

# Game ko Rules
rules = {
    "rock": "scissors",  # rock beats scissors
    "paper": "rock",  # paper beats rock
    "scissors": "paper"  # sciccors beat paper
}


def get_user_choice():
    choice = input('Choose rock , paper or scissors:').lower()
    if choice not in rules:
        raise ValueError(
            "Invalid choice. Please choose rock paper or scissors only")
    return choice


def get_computer_choice():
    return random.choice(list(rules.keys()))


def determine_winner(user, computer):
    if user == computer:
        return "It's a draw"
    elif rules[user] == computer:
        return "You Won"
    else:
        return "You lost. Computer Won"


def play_game():
    while True:
        try:
            user_choice = get_user_choice()
        except ValueError as e:
            print(e)
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou choose {user_choice}{emoji[user_choice]}")
        print(f"Computer chose {computer_choice}{emoji[computer_choice]}")

        print(determine_winner(user_choice, computer_choice))

        play_again = input("\nDo you want to play again ?(y/n)").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


play_game()
