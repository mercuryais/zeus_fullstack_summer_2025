import turtle
import random

turtle.speed(0)
def  dots(x, y, w, paint):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.color(paint)


    for n in range(3):
        turtle.color(paint)
        turtle.dot(w)
        if paint == 'red':
            paint = 'orange'
        else: 
            paint = "yellow"
        w = w - 30
    if
        dots(x, y, 90, 'red')
dots(0, 0, 90, 'red')
turtle.done()