print("Welcome To Guess The Number Game. Guess the number correctly and you shall win >>>>")
import random
import os

number = random.randint(1, 101)

level = input("What level of difficulty do you want? (easy or hard) ").lower()
if level == "easy":
    lives = 10
elif level == "hard":
    lives = 5

game_is_on = True 
while game_is_on:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("You win")
        game_is_on = False
    elif guess > number:
        print("Too high")
        lives -= 1
    elif guess < number:
        print("Too low")
        lives -= 1
    else:
        print("Invalid input")

    if lives == 0:
        game_is_on = False
        print("You lose")
        print(f"The number was {number}")


