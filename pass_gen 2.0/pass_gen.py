print("Welcome to the Password Generator!")
import random
import string
import os 
import time 

alphabets = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

alphabets = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)



def password_generator():
    app = input("What app are you using this password for? ")
    str_char = int(input("How many alphabets do you want in your password : "))
    int_char = int(input("How many numbers do you want in your password : "))
    sym_char = int(input("How many symbols do you want in your password : "))
    password = ""
    for i in range(0, str_char):
        password += random.choice(alphabets)
    for i in range(0, int_char):
        password += random.choice(numbers)
    for i in range(0, sym_char):
        password += random.choice(symbols)
    hard_password = ''.join(random.sample(password, len(password)))

    type = input("Do you want a easy password or a hard password : type easy or hard ").lower()
    if type == "easy":
        print(f"Your easy password is {password}")
        with open("./pass_gen 2.0/pass.txt", "a") as file:  # Changed filename to "pass.txt"
            file.write(f"Your password for {app} is {password} \n")
    elif type == "hard":
        print(f"Your hard password is {hard_password}")
        with open("./pass_gen 2.0/pass.txt", "a") as file:  # Changed filename to "pass.txt"
            file.write(f"Your password for {app} is {hard_password} \n")

Pass_gen = True 

while Pass_gen:
    password_generator()
    continues = input("Do you want to continue generating a new password :  (y/n) ").lower()
    if continues == "n":
        
        print("Thank you for using the password generator")
        print("Your passwords have been saved in the passwords.txt file")

        time.sleep(5)
        os.system('cls')

        Pass_gen = False

    elif continues == "y":
        os.system('cls')



    