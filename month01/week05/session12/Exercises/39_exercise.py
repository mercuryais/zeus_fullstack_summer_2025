import turtle

turtle.colormode(255)
turtle.bgcolor(120,0, 0)
turtle.speed(0)
turtle.width(1)
color = ["DarkGreen", 'DarkSeaGreen3']
for n in range(255):
    turtle.color(color[n%2])
    turtle.fd(n)
    turtle.rt(61)

turtle.done()