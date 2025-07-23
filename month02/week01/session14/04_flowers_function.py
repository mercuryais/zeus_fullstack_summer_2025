import turtle
import random

def flower(x, y, color):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.width(5)
    turtle.seth(90)
    turtle.color("green")
    turtle.fd(70)

    for n in range(5):
        turtle.width(25)
        turtle.rt(72)
        turtle.color(color)
        turtle.fd(25)
        turtle.backward(25)
    turtle.color("black")
    turtle.dot(15)

turtle.speed(0)
turtle.bgcolor("lightgreen")
colors = ["red", "purple", "yellow", "blue"]
for f in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    flower(x, y, random.choice(colors))
turtle.done()