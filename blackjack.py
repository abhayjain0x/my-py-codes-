import random 
import os 
import art 
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

print(logo)
game_is_on = False

start_the_game = input("Do you want to play a game of Blackjack ? (y/n) ").lower()
if start_the_game == "y":
    os.system("cls")
    game_is_on = True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

computer_nums = [random.choice(numbers) for num in range(3)]

player_nums = [random.choice(numbers) for num in range(3)]


import art

def game_if_quitat2():
    comp_sum = computer_nums[0] + computer_nums[1]
    player_sum = player_nums[0] + player_nums[1]

    # ASCII art of numbers
    comp_nums_art = [art.text2art(str(num), "block").split('\n') for num in computer_nums[:2]]
    player_nums_art = [art.text2art(str(num), "block").split('\n') for num in player_nums[:2]]

    # Concatenate and print ASCII art
    print("Computer's numbers:")
    for lines in zip(*comp_nums_art):
        print(' '.join(lines))
    print("Player's numbers:")
    for lines in zip(*player_nums_art):
        print(' '.join(lines))

    if comp_sum > player_sum:
        print("You lose as your sum is less than the computer's sum")
    elif comp_sum < player_sum:
        print("You win as your sum is greater than the computer's sum")
    else:
        print("Draw")

def game_if_quitat3():
    comp_sum = computer_nums[0] + computer_nums[1] + computer_nums[2]
    player_sum = player_nums[0] + player_nums[1] + player_nums[2]

    # ASCII art of numbers
    comp_nums_art = [art.text2art(str(num), "block").split('\n') for num in computer_nums]
    player_nums_art = [art.text2art(str(num), "block").split('\n') for num in player_nums]

    # Concatenate and print ASCII art
    print("Computer's numbers:")
    for lines in zip(*comp_nums_art):
        print(' '.join(lines))
    print("Player's numbers:")
    for lines in zip(*player_nums_art):
        print(' '.join(lines))

    if comp_sum > 21 and player_sum < 21:
        print("You win")
    elif comp_sum < 21 and player_sum > 21:
        print(f"You lose as you crossed 21")
    elif comp_sum > player_sum:
        print("You lose as your sum is less than the computer's sum")
    elif comp_sum < player_sum:
        print("You win as your sum is greater than the computer's sum")
    else:
        print("Draw")



while game_is_on:
    print(f"computer one of the numbers is {computer_nums[0]}")
    print(f"your 2 of the numbers are {player_nums[:2]}")

    ask_for_show = input("Do you want to see the third card ? (y/n) ").lower()
    if ask_for_show == "y":
        game_if_quitat3()
        game_is_on = False
    elif ask_for_show == "n":
        game_if_quitat2()
        game_is_on = False  

    play_again = input("Do you want to play again ? (y/n) ").lower()
    if play_again == "y":
        game_is_on = True
        os.system("cls")
    elif play_again == "n":
        game_is_on = False
        print("Thank you for playing the game")
        break