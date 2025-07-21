import turtle

turtle.bgcolor('black')
turtle.speed(0)
turtle.width(1)

col = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'DarkGreen']

for n in range(255):
    turtle.color(col[n%8])
    turtle.fd(n*1.2)
    turtle.rt(46)

turtle.done()