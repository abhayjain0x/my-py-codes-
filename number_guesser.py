level = input("Welcome to the number Guessing game \n there are 3 levels in the game \n easy \n medium \n hard. \n choose the level according to your guessing skill nerd : ").lower()
easy_level_guide = "In easy level you have 10 chances to guess the number between 1 and 50."
medium_level_guide = "In medium level you have 5 chances to guess the number between 1 and 100."
hard_level_guide = "In hard level you have 6 chances to guess the number between 100 and 200. and this is bit special as you have to guess the number digit by digit, if the number is 123 then you have to guess 1 then 2 then 3."
import random 
game_is_on = True
if level == "easy":
    print(easy_level_guide)
    lives = 10
    random_num = random.randint(1, 51)
    while game_is_on:
        user_input = int(input("type a num"))
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
elif level == "medium":
    print(medium_level_guide)
    lives = 5
    random_num = random.randint(1, 101)
    while game_is_on:
        user_input = int(input("type a num"))
    
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
elif level == "hard":
    print(hard_level_guide)
    lives = 6
    random_num = random.randint(100, 201)
    number_list = [int(digit) for digit in str(random_num)]
    while game_is_on:
        user_input = int(input("type a num"))
        if user_input in number_list:
            print(f"You guessed the {number_list.index(user_input) + 1}nd digit correctly")
            number_list.remove(user_input)
            print(number_list)
        elif user_input not in number_list:
            print("You guessed the wrong digit")
            lives -= 1
        if len(number_list) == 0:
            print("You win")
            game_is_on = False


