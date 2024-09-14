# Game Instructions:
# 1. You control the turtle with the arrow keys (Up, Down, Left, Right).
# 2. Your goal is to "catch" the circles that appear randomly on the screen.
# 3. Each time you catch a circle, it disappears, and your score increases.
# 4. The game ends when you catch a certain number of circles.

import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Catch Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(-290, 290), random.randint(-290, 290))
score = 0

def go_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        x = -290
    player.setx(x)

def go_right():
    x = player.xcor()
    x += 20
    if x > 290:
        x = 290
    player.setx(x)

def go_up():
    y = player.ycor()
    y += 20
    if y > 290:
        y = 290
    player.sety(y)

def go_down():
    y = player.ycor()
    y -= 20
    if y < -290:
        y = -290
    player.sety(y)

def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 20:
        return True
    else:
        return False

screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

while True:
    if is_collision(player, target):
        score += 1
        print("Score:", score)
        target.goto(random.randint(-290, 290), random.randint(-290, 290))

    if score == 10:
        print("You win!")
        break
screen.exitonclick()
