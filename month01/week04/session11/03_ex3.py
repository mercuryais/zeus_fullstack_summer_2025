import turtle
import random

colours = ['blue', 'CadetBlue2', 'CadetBlue1', 'CadetBlue3']
turtle.width(8)
turtle.speed(0)
for n in range(250):
    width = random.randint(200, 300)
    angle = random.randint(30, 330)
    turtle.right(angle)
    turtle.color(random.choice(colours))
    turtle.forward(width)
    turtle.right(180)
    turtle.forward(width)
turtle.done()