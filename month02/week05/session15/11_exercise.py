import turtle
turtle.speed(0)

def  drawSquare(x, y, w, color):
    turtle.goto(x, y)
    turtle.color(color, color)
    turtle.begin_fill()

    for n in range(4):
        turtle.fd(w)
        turtle.rt(90)
    turtle.end_fill()

    if color == 'orange':
        color = 'black'
    else: 
        color = "orange"
    if w > 180:
        drawSquare(x, y, w-15 , color)

drawSquare(0, 0, 300, 'orange')
turtle.done()