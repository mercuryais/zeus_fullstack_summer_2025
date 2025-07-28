import turtle
import random

turtle.speed(0)
def game():
    for n in range(30):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        w = 90
        paint = "red"
        for i in range(3):
            turtle.color(paint)
            turtle.dot(w)
            if paint == "red":
                paint = "orange"
            elif paint == "orange":
                paint = "yellow"
            w = w - 30
game()
turtle.done()