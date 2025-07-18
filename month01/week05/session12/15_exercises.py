import turtle
import random

turtle.speed(0)
turtle.colormode(255)
turtle.width(1)
paint = ['purple', 'blue', 'yellow', 'green', 'orange']

for n in range(255):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.goto(x, y)
    turtle.color(255, n, 0)
    turtle.dot(20)
    for size in range(250, 0, -25):
        turtle.color(random.choice(paint))
        turtle.dot(size)

turtle.done()
