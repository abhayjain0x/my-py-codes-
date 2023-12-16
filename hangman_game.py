print("Welcome to Hangman Game . the game is simple Guess the word , 6 chances to get it right")

import random
from random_word import RandomWords

hangman_stages = [
    """
    +---+
    |   |
        |
        |
        |
        |
  ========
    """,  # Stage 0
    """
    +---+
    |   |
    O   |
        |
        |
        |
  ========
    """,  # Stage 1
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
  ========
    """,  # Stage 2
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
  ========
    """,  # Stage 3
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
  ========
    """,  # Stage 4
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
  ========
    """,  # Stage 5
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
  ========
    """   # Stage 6
]

ascii_new = hangman_stages[::-1]

word_lists = RandomWords()

word_list = []
for i in range(0, 10):
    word = word_lists.get_random_word()
    word_list.append(word)



game_is_on = True
chosen_word = random.choice(word_list)



display = []

for i in range(len(chosen_word)):
    display += "_"


print(display)

lives = 6


while game_is_on:
    guess = input("Guess a letter: ").lower()


    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(ascii_new[lives])
    
        print(f"You have {lives} lives left")
    if lives == 0:
        game_is_on = False
        print("You lose")
        print(f"The word was {chosen_word}")
        break
            

    print(display)

    if "_" not in display:
        game_is_on = False
        print("You win")

    