from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Car Crossing Game")
screen.tracer(0)

MOVE_INCREMENT = 5

class Obj(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
    
    def move(self):
        self.forward(10)
    
    def reset(self):
        self.goto(0, -280)

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(["red", "blue", "green", "yellow", "orange", "purple", "pink"]))
        self.setheading(180)
        self.goto(300, random.randint(-250, 250))  # Cars start from the right side of the screen
        self.speed = 10
    
    def move(self):
        self.forward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Courier", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

turtle = Obj()
cars = []
scoreboard = Scoreboard()
screen.listen()
screen.onkey(turtle.move, "w")

game_is_on = True
car_creation_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a new car every 6 iterations
    car_creation_counter += 1
    if car_creation_counter % 6 == 0:
        car = Cars()
        cars.append(car)

    for car in cars:
        car.move()
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.ycor() >= 280:
        turtle.reset()
        scoreboard.increase_score()
        car_creation_counter += 5
        for car in cars:
            car.next_level()  # Increase the speed of the cars

        # Create additional cars for each level
        for _ in range(scoreboard.score):
            car = Cars()
            cars.append(car)

screen.exitonclick()