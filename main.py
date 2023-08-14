import random

with open("words.txt") as file:
    word_list = [line.strip() for line in file]

word = random.choice(word_list)
word_letters = set(word)
player_guesses = set()
max_mistakes = 7

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

while True:
    print("Word: ", end="")
    for letter in word:
        if letter in player_guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print()

    print(HANGMAN[max_mistakes])
    print("Guesses remaining:", max_mistakes)
    guess = input("Guess a letter: ")
    player_guesses.add(guess)

    if guess in word_letters:
        print("Correct!")
    else:
        print("Incorrect!")
        max_mistakes -= 1

    if max_mistakes == 0:
        print("You lost! The word was", word)
        break
    elif word_letters.issubset(player_guesses):
        print("You won!")
        break
