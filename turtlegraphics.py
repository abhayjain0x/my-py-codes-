import turtle as t
import random

my_screen = t.Screen()
my_screen.bgcolor("black")
my_screen.title("My Turtle Game")
my_screen.setup(width=900, height=600)


turtle = t.Turtle()
turtle.shape("turtle")
turtle.color("green")
# turtle.penup()
# turtle.goto(-200, 0)
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.pendown()

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
# for i in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
# turtle.pensize(10)

# for i in range(3, 11):
#     turtle.color(random.choice(colors))
#     for j in range(i):
#         turtle.forward(100)
#         turtle.right(360 / i)





# for i in range(100):
#     turtle.color(random.choice(colors))
#     turtle.forward(40)
#     turtle.right(random.randint(0, 360))


turtle.speed("fastest")

def random_colors():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, g, b)
t.colormode(255)

# draw a spiropgraph 

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        turtle.color(random_colors())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)













my_screen.exitonclick()