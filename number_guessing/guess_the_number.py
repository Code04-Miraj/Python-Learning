#Self Written Project

import random

print("Welcome to the game")
print("I'm thinking a nummber between 1 and 10")

# Generate random nummber
secret_number = random.randint(1, 10)
attemp = 0

while True:
    try:
        guess = int(input("Make a Guess: "))
        attemp += 1

        if guess < 1 or guess > 10:
            print("Guess the number between 1 and 10 only")

        elif guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print("Congrats! You Guessed it Right")
            break
    except ValueError:
        print("Enter the correct integer")



