import turtle 
import random

turtle.penup() # no painting
turtle.speed(0)
turtle.bgcolor("purple")
turtle.colormode(255)

for c in range(0, 200):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.goto(x, y)
    turtle.color(180, c, 240)
    turtle.dot(20)

turtle.done()