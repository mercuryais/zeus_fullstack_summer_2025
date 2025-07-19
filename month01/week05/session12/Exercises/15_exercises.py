import turtle
import random

turtle.speed(0)
turtle.colormode(255)
turtle.width(1)
paint = ['purple', 'blue', 'yellow', 'green', 'orange', 'red']

for n in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.goto(x, y)
    for size in range(250, 0, -25):
        turtle.color(random.choice(paint))
        turtle.dot(size)

turtle.done()
