import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.width(3)
col = ['red', 'orange', 'yellow']



for a in range(70):
    turtle.goto(150, 150)
    turtle.color(random.choice(col))
    turtle.left(5)
    turtle.fd(700)

col = ['blue', 'DarkSlateGray1']
turtle.goto(-150, -150)
turtle.colormode(255)
turtle.width(3)
for a in range(75):
    turtle.color(random.choice(col))
    turtle.left(5)
    turtle.fd(700)
    turtle.goto(-150, -150)
turtle.done()

