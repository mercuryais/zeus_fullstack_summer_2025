import turtle
# X 03

def square(orgon, ondor, angle, locationa, locationb, color):
    turtle.penup()
    turtle.goto(locationa, locationb)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(orgon)
    turtle.rt(angle)
    turtle.forward(ondor)
    turtle.rt(angle)
    turtle.forward(orgon)
    turtle.rt(angle)
    turtle.forward(ondor)
    turtle.end_fill()


square(200, 50, 90, -200, 0, 'red')
square(220, 50, 90, 0, 0, "blue")
square(200, 50, 90, -20, 50, "yellow")
turtle.done()