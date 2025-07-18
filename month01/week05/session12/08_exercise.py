import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.width(5)
col = ['red', 'yellow', 'orange', 'purple', 'green']

for a in range(0, 180):
    turtle.color(random.choice(col))
    turtle.goto(0, 0)
    turtle.right(2)
    turtle.fd(700)

turtle.done()