print("Welcome to the Game of 21 . There are 2 levels in this game . easy or hard hard gives you 3 chances and easy gives you 5 chances, guess before the chances are over .")

import random

game_is_on = False 

starting = input("Do you want to play the game ? (y/n) ").lower()   

if starting == "y":
    game_is_on = True
random_num = random.randint(1, 101)


def game_level():
    global lives 
    global random_num
    global game_is_on
    level = input("Choose the level : ").lower()
    if level == "easy":
        lives = 5
        random_num = random.randint(1, 51)
    elif level == "hard":
        lives = 3
        random_num = random.randint(1, 101)
    
    while lives > 0 and game_is_on:
        user_input = int(input("Guess the number : "))
        if user_input == random_num:
            print("You win")
            game_is_on = False
        elif user_input > random_num:
            print("Too high")
            lives -= 1
        elif user_input < random_num:
            print("Too low")
            lives -= 1

        if lives == 0:
            print(f"You lose and The number was {random_num}")
            game_is_on = False


while game_is_on:
    game_level()