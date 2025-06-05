import random

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,
    # Stage 2: Only the head remains
    """
      ___  
     /___\\ 
     (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
      ___  
     /___\\ 
    """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage and the current state of the word."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word.strip())


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, remove this later

    # Show game state before guessing
    display_game_state(mistakes, secret_word, guessed_letters)

    # Just one guess for now
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)

    # Update and display game state again
    mistakes += 1  # Simulating a mistake for now
    display_game_state(mistakes, secret_word, guessed_letters)


if __name__ == "__main__":
    play_game()
