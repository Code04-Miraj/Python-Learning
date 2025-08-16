# Program Flow:
# Define choices (r, p, s)
# Define emoji for each choice
# Define rules (what beats what)

# Loop
# Ask the user to make a choice (r/p/s)
# If user input is invalid
# Print error message
# Continue to next loop iteration

# Let the computer randomly choose (r/p/s)

# Print both choices using emojis

# If user choice == computer choice
# Print "Tie!"
# Else if user beats computer using rules
# Print "You Won!"
# Else
# Print "Computer Won!"

# Ask user if they want to play again (y/n)
# If input is 'n'
# Break the loop


# Tutorial Help

# ask if user want to play again
import random


choices = ('r', 'p', 's')
# declare emoji
emoji = {
    "r": "🪨",
    "s": "✂️",
    "p": "📃"
}
# setup rules
rules = {
    "r": "s",
    "s": "p",
    "p": "r"
}

while True:
    # Ask the user to make a choice
    user_choice = input('Rock,Paper, or Scissor?(r/p/s):').lower()
    if user_choice not in choices:
        # If choice is invalid, throw a error msg
        print('Invalid Choice!')
        continue

    # let computer make a choice
    computer_choice = random.choice(choices)

    # print choices with emoji
    print(f'You choose {emoji[user_choice]}')
    print(f'Computer Choose {emoji[computer_choice]}')

    # display who won with the rules of rock paper scissors

    if user_choice == computer_choice:
        print('Tie!')
    elif rules[user_choice] == computer_choice:
        print('You Won!')
    else:
        print('Computer Won')
    # Verify if user wants to continue the game or not
    should_continue = input('Continue? (y/n):').lower()
    if should_continue == 'n':

        break
