import random

# This txt file
with open("words.txt") as file:
    word_list = [line.strip() for line in file]

# Select a random word from the list
word = random.choice(word_list)

# Create a set of the letters in the word
word_letters = set(word)

# Create an empty set to store the player's guesses
player_guesses = set()

# Set the number of mistakes allowed
max_mistakes = 7

# Hangman ASCII art (same as before)
HANGMAN = (
    """
    -----
    |   |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |   |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |  /|
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  /
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    |
    |
    |
    --------
    """,
)

# Loop until the game is over
while True:
    # Print the current state of the word with underscores for unguessed letters
    print("Word: ", end="")
    for letter in word:
        if letter in player_guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print()

    # Draw the hangman
    print(HANGMAN[max_mistakes])

    # Display the number of guesses remaining
    print("Guesses remaining:", max_mistakes)

    # Ask the player to guess a letter
    guess = input("Guess a letter: ")

    # Add the guess to the player's set of guesses
    player_guesses.add(guess)

    # Check if the guess is correct
    if guess in word_letters:
        print("Correct!")
    else:
        print("Incorrect!")
        max_mistakes -= 1

    # Check if the game is over
    if max_mistakes == 0:
        print("You lost! The word was", word)
        break
    elif word_letters.issubset(player_guesses):
        print("You won!")
        break
