import turtle
import random

turtle.speed(0)
paint = ['purple', 'blue', 'yellow', 'green', 'orange']
turtle.goto(-120, 0)
for size in range(400, 0, -25):
    turtle.color(random.choice(paint))
    turtle.dot(size)

turtle.goto(120, 0)
for size in range(400, 0, -25):
    turtle.color(random.choice(paint))
    turtle.dot(size)

turtle.done()