#hangman
import random

words = ['rat', 'cat', 'dog', 'monkey', 'bear', 'snake']
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("The word consists of", len(word), "letters.")

while True:
    print("\nAttempts remaining:", attempts)
    print("Guessed letters:", guessed_letters)

    displayed_word = ''.join([letter if letter in guessed_letters else '_ ' for letter in word])
    print("Word:", displayed_word)

    if '_' not in displayed_word:
        print("Congratulations! You have guessed the word correctly!")
        break

    guess = input("Guess a letter: ").lower()

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess.")

    if attempts == 0:
        print("Game over! You ran out of attempts.")
        print("The word was:", word)
        break
