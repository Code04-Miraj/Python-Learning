# Program Flow:
    # Generate a ranmdom number
    # Loop
    # Ask the user to make a guess
    # If user input invalid num, print error
    # If number < guess
    #   print Too High
    # If number > guess
    #   Print Too Low


# Tutorial Help


import random

pc_guess = random.randint(1, 10)

while True:

    try:
        user_guess = int(input('Guess a number between 1 ans 10: '))

        if user_guess < pc_guess:
            print("Too Low")
        elif user_guess > pc_guess:
            print("Too High")
        else:
            print("Congrats! You guessed it correct")
            break
    except ValueError:
        print("Enter a valid Number")
