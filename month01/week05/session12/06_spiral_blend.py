import turtle

turtle.speed(0)
turtle.colormode(255)
turtle.width(1)

for n in range(255):
    turtle.pencolor(255, 255-n, n) # pen colour
    turtle.fd(n * 2) # fd = forward
    turtle.rt(90) # rt = right

turtle.done()