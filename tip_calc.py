print("Today is New Year guys . so lets celebrate it with a tip calculator, shall we ?")
print("Welcome to the tip calculator")

bill = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give ? 10 , 12 or 15 ? "))
people = input("How many people are there to split the bill ?  type the names for the random person to pay the whole bill : ")
peps = people.split(",")
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / len(peps)


import random 

print(peps)
random_person = random.choice(peps)

print(f"{random_person} is going to pay ${bill_per_person:.2f}")