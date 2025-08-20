
#Program FLow:
# Ask the use to roll the dice
      # If user choose yes(y), Generate twon random number
      # Print it
      # If user choose no(n), Terminate the Game
      # Else print invalid choice

#Tutorial Help
import random

# Loop
while True:
    choice = input("Roll the Dice? (y/n): ").lower()
    
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1},{dice2})')
        
    elif choice == 'n':
        print('Thanks for playing')
        break
        
    else:
        print("Invalid Choice")

      
