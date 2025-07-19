import turtle

turtle.speed(0)
turtle.colormode(255)
turtle.width(1)
turtle.right(20)
for n in range(300):
    turtle.pencolor(250-n, 0, n) # pen colour
    turtle.fd(n) # fd = forward
    turtle.rt(130) # rt = right

turtle.done()