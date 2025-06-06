# game_logic.py

import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Select a random word from the WORDS list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current game state: snowman, guessed word, and stats."""
    print("\n" + "=" * 30)
    print(STAGES[mistakes])
    print("\nWord: ", end="")
    for letter in secret_word:
        print(letter if letter in guessed_letters else "_", end=" ")
    print("\nGuessed Letters:", " ".join(sorted(guessed_letters)))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("=" * 30 + "\n")


def ask_to_play_again():
    """Prompt the user to play again after the game ends."""
    while True:
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice in ["y", "n"]:
            return choice == "y"
        print("Please enter 'y' or 'n'.")


def play_game():
    """Main game loop."""
    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        max_mistakes = len(STAGES) - 1

        print("\n🎮 Welcome to Snowman Meltdown! ❄️")

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = input("Guess a letter: ").lower().strip()

            # Input validation
            if not guess.isalpha() or len(guess) != 1:
                print("❌ Please enter a single alphabetical letter.\n")
                continue

            if guess in guessed_letters:
                print("⚠️ You already guessed that letter.\n")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print("✅ Correct!\n")
            else:
                mistakes += 1
                print("❌ Incorrect!\n")

            # Win condition
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("🎉 You saved the snowman! The secret word is:", secret_word)
                break

            # Lose condition
            if mistakes >= max_mistakes:
                display_game_state(mistakes, secret_word, guessed_letters)
                print("💀 The snowman melted! The secret word was:", secret_word)
                break

        if not ask_to_play_again():
            print("👋 Thanks for playing!")
            break
