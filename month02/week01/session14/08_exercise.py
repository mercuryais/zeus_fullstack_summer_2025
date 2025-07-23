import turtle


turtle.begin_fill()
def square(color, sizex, sizey, locx, locy):
    turtle.speed(0)
    turtle.pu()
    turtle.goto(locx, locy)
    turtle.pd()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(sizex)
    turtle.rt(90)
    turtle.fd(sizey)
    turtle.rt(90)
    turtle.fd(sizex)
    turtle.rt(90)
    turtle.fd(sizey)
    turtle.end_fill()
    
square("black", 280, 280, -160, 160)
turtle.rt(90)
square("red", 160, 160, -160, 160)
square("yellow", 100, 100, 10, 60)
square("blue", 100, 60,120, -20)
square("red", 80, 100, 120, -40)
square("blue", 25, 100, -160, -20)
square("yellow", 100, 100, -110, -120)

turtle.done()
    
