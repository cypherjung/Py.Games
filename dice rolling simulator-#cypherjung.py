#dice rolling simulator
import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        roll = input("Press Enter to roll(or 'q' to quit): ")
        
        if roll.lower() == 'q':
            break
        
        
        dice_value = roll_dice()
        print("You rolled a", dice_value)

    print("Thank you for playing!")

play_game()
exit()
