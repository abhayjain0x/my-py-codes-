import os 
import random
print("Welcome To the Rock paper scissors Game" ) 
print("This is one of the hardest rps you would ever play")
print("You have to play against leo ")
games = False 
startthegame = input("Do you want to start the game? (y/n) ")


ascii_art = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,  # Rock
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,  # Paper
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """,  # Scissors
]

vs_ascii = r"""

____   _____________
\   \ /   /   _____/
 \   Y   /\_____  \ 
  \     / /        \
   \___/ /_______  /
                 \/ 

"""

choices = ["rock", "paper", "scissors"]
score = 0

def game():
    global score
    your_choice = input("What do you choose? (rock, paper or scissors) ")
    leo_choice = random.choice(choices)
    print("You chose " + your_choice)
    print(ascii_art[choices.index(your_choice)])
    print(vs_ascii)
    print("Leo chose " + leo_choice)
    print(ascii_art[choices.index(leo_choice)])
    if your_choice == leo_choice:
        print("It's a tie!")
    elif your_choice == "rock" and leo_choice == "scissors":
        print("You win!")
        score += 1 
    elif your_choice == "paper" and leo_choice == "rock":
        print("You win!")
        score += 1 
    elif your_choice == "scissors" and leo_choice == "paper":
        print("You win!")
        score += 1 
    elif your_choice == "rock" and leo_choice == "paper":
        print("You lose!")
        score -= 1 
    elif your_choice == "paper" and leo_choice == "scissors":
        print("You lose!")
        score -= 1 
    elif your_choice == "scissors" and leo_choice == "rock":
        print("You lose!")
        score -= 1 
    else:
        print("That's not a valid play. Check your spelling!")




    

while startthegame == "y":
    os.system("clear")
    game()
    startthegame = input("Do you want to play again? (y/n) ")
    if startthegame == "n":
        print(f"your total score is {score}")
        print("Thank you for playing")
        break

