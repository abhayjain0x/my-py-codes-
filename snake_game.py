from turtle import Turtle, Screen
import time 
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


starting_positions = [(0, 0), (-20, 0), (-40, 0)]



class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.segments[0].forward(20)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extend(self):
        self.add_segment(self.segments[-1].position())



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    
class Scoreboard(Turtle):
    
        def __init__(self):
            super().__init__()
            self.score = 0
            self.color("white")
            self.penup()
            self.goto(0, 260)
            self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
            self.hideturtle()
        
        def increase_score(self):
            self.score += 1
            self.clear()
            self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

        def game_over(self):
            self.goto(0, 0)
            self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

ball = Ball()

screen.listen()
snake = Snake()

score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        score.game_over()
        game_is_on = False

    if snake.head.distance(ball) < 15:
        ball.refresh()
        snake.extend()
        score.increase_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    

    






























screen.exitonclick()