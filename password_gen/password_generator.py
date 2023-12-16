import random 
import os 

# Alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']

print("Welcome to the PyPassword Generator!")
game_is_on = True 
app = input("What app are you using this password for? ")

nr_letters= int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))
level = input("What level of security do you want? (low or  high) ").lower()

def password_generator():
    password = ""
    for i in range(0, nr_letters):
        password += random.choice(alphabets)

    for i in range(0, nr_symbols):
        password += random.choice(symbols)

    for i in range(0, nr_numbers):
        password += random.choice(numbers)

    new_password = ''.join(random.sample(password, len(password)))

    if level == "low":
        print(f"the password for your {app} app  is  {password}")
        with open("passwords.txt", "a") as file:
            file.write(f"the password for your {app} app  is  {password} \n")
    elif level == "high":
        print(f"the password for your {app} app  is  {new_password}")
        with open("passwords.txt", "a") as file:
            file.write(f"the password for your {app} app  is  {new_password} \n")

# Call the function before asking the user if they want to continue
password_generator()

continues = input("Do you want to continue generating a new password :  (y/n) ").lower()

if continues == "y":
    while game_is_on:
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux/OS X
            os.system('clear')
        password_generator()
        continues = input("Do you want to continue generating a new password :  (y/n) ").lower()
        if continues == "n":
            game_is_on = False
            print("Thank you for using the password generator")