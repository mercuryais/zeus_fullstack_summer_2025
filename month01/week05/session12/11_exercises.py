import turtle
import random

turtle.goto(150, 150)
turtle.colormode(255)
turtle.speed(0)
turtle.width(3)
col = ['DarkSlateGray2', 'blue']



for a in range(100):
    turtle.color(random.choice(col))
    turtle.left(5)
    turtle.fd(700)
    turtle.goto(150, 150)

turtle.done()