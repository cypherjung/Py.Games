#rock paper scissor
import random

def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!", 0
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def play():
    valid_choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice not in valid_choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(valid_choices)
        print(f"Computer chooses: {computer_choice}")

        result, score = winner(player_choice, computer_choice)
        print(result)

        if score > 0:
            player_score += 1
        elif score < 0:
            computer_score += 1

        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Final scores:")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

print("Let's play Rock-Paper-Scissors!")
play()
print("Thanks for playing")
exit()
