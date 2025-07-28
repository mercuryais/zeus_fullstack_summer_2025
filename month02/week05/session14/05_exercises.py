import turtle
turtle.speed(0)

def square(size, x, y, color):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.color(color)
    turtle.begin_fill()
    for n in range(4):
        turtle.fd(size)
        turtle.right(90)
    turtle.end_fill()


square(60, -200, 200, "blue")
square(90, -130, 200, "green")
square(110, -200, 100, "yellow")
square(40, -80, 100, "purple")
square(150, -80, 55, "orange")
square(40, 77, 55, "purple")
square(40, 77, 10, "purple")
square(40, 77, -35, "purple")
square(180, -30, 240, "red")
turtle.done()
