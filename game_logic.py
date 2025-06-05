# game_logic.py

import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word.strip())
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            mistakes += 1
            print("Wrong guess!\n")

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("🎉 You saved the snowman! The word was:", secret_word)
            break

        # Check lose condition
        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("💧 The snowman melted! The word was:", secret_word)
            break
