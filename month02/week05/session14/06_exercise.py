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


square(500, -200, 200, "yellow")
square(130, -130 , 130, "white")
square(130, 100 , 130, "white")
square(70, -70 , 70, "black")
square(70, 100 , 70, "black")
square(20, 20 , -140, "red")
square(20, 20 , -160, "red")
square(20, 20 , -180, "red")
square(20, 40 , -180, "red")
square(20, 60 , -180, "red")
turtle.done()
