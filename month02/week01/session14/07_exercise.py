import turtle

turtle.speed()

def square(color, location, size):
    turtle.color(color)
    turtle.pu()
    turtle.goto(location, location)
    turtle.rt(180)
    turtle.pd()
    turtle.begin_fill()
    for n in range(4):
        turtle.forward(size)
        turtle.lt(90)
    turtle.end_fill()
    turtle.rt(180)
square("red", 300, 300)
square("orange", 275, 250)
square("yellow", 250, 200)
square("green", 225, 150)
square("blue", 200, 100)
square("purple", 175, 50)
turtle.done()