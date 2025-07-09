import turtle
import random

colours = ['blue', 'red', 'purple', 'pink', 'yellow', 'green']
turtle.width(3)
turtle.speed(0)
for n in range(100):
    width = random.randint(300, 400)
    angle = random.randint(30, 330)
    turtle.right(angle)
    turtle.color(random.choice(colours))
    turtle.forward(width)
    turtle.right(180)
    turtle.forward(width)
turtle.done()