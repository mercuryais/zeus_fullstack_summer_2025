import turtle
import random

turtle.speed(0)
turtle.width(120)
paint=['red','blue','yellow','green']

for angle in range(0, 360, 10):             
    turtle.goto(0, 0)
    turtle.color(random.choice(paint))
    turtle.seth(angle)
    turtle.forward(800)

turtle.done()
