import turtle as t
import random

screen = t.Screen()
screen.listen()

# Set the screen size to the maximum window size
screen.setup(width=screen.window_width(), height=screen.window_height())

screen.bgcolor("black")

colors = ["red", "blue", "green", "yellow", "orange", "purple"]

turtle_user = screen.textinput("Turtle Race", "Which color turtle would win the race?")

turtles = []
for i in range(len(colors)):
    turtle = t.Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    # Adjust the starting position of the turtles
    turtle.goto(-screen.window_width()/2 + 20, -screen.window_height()/2 + 20 + i * (screen.window_height() - 40) / len(colors))
    turtles.append(turtle)

game_is_on = True
while game_is_on:
    for turtle in turtles:
        # Adjust the ending position of the race
        if turtle.xcor() > screen.window_width()/2 - 20:
            game_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == turtle_user:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()