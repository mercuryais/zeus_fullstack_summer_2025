import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.width(3)
turtle.bgcolor('DarkSlateBlue')
col = ['orchid4', 'plum1', 'purple1']

for a in range(0, 67):
    turtle.color(random.choice(col))
    turtle.goto(0, 0)
    turtle.left(5)
    turtle.fd(700)

turtle.done()