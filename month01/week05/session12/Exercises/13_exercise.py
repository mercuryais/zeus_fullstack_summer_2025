import turtle
import random

turtle.speed(0)
paint = ['red', 'red4']

for size in range(400, 0, -10):
    turtle.color(random.choice(paint))
    turtle.dot(size)

turtle.done()