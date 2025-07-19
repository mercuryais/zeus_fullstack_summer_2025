import turtle

turtle.bgcolor("orange")
turtle.speed(0)
turtle.colormode(255)
turtle.width(1)
turtle.right(20)
for n in range(255):
    turtle.pencolor(250-n, 0, n) # pen colour
    turtle.fd(n) # fd = forward
    turtle.rt(89) # rt = right

turtle.done()