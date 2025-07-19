import turtle

turtle.colormode(255)
turtle.speed(0)
turtle.width(10)
for size in range(255, 0, -1):
    turtle.color(255, 128, size)
    turtle.rt(90)
    turtle.forward(size)
    

turtle.done()