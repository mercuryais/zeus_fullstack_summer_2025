import turtle

turtle.colormode(255)
turtle.bgcolor(70,70,180)
turtle.speed(0)
turtle.width(1)

col = ['white', 'yellow', 'white','DarkOliveGreen','white', 'pink']

for n in range(255):
    turtle.color(col[n%6])
    turtle.fd(n)
    turtle.rt(61)

turtle.done()