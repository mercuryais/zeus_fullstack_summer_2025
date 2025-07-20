import turtle 
import random

turtle.penup() # no painting
turtle.speed(0)
turtle.colormode(255)

for c in range(0, 150):
    x = random.randint(-240, 240)
    y = random.randint(-240, 240)
    turtle.goto(x, y)
    turtle.color(255, c, c)
    turtle.dot(20)

for c in range(0, 200):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    turtle.goto(x, y)
    turtle.color(250, 250, c)
    turtle.dot(20)
turtle.done()  