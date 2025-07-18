import turtle

turtle.bgcolor('black')
turtle.speed(0)
turtle.width(1)

col = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for n in range(255):
    turtle.color(col[n%6])
    turtle.fd(n)
    turtle.rt(61)

turtle.done()