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

    if color == 'purple':
        color = 'pink'
    else: 
        color = "purple"
    if w > 200:
        drawSquare(x + 7, y - 7, w-14, color)

drawSquare(0, 0, 300, 'purple')
turtle.done()