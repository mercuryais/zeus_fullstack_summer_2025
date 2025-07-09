import turtle
import random

colours = ['blue', 'red', 'purple', 'pink', 'yellow', 'green']
turtle.width(7)
turtle.speed(0)
for n in range(80):
    width = random.randint(200, 350)
    angle = random.randint(30, 330)
    turtle.right(angle)
    turtle.color(random.choice(colours))
    turtle.forward(width)
    turtle.right(180)
    turtle.forward(width)
turtle.done()