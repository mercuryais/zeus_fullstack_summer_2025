import turtle
turtle.speed(0)
turtle.color("red")
turtle.begin_fill()
turtle.goto(-250, 300)
for n in range(4):
    turtle.fd(500)
    turtle.rt(90)
turtle.end_fill()
def  drawSquare(x, y, w, color):
    turtle.goto(x, y)
    turtle.color(color, color)
    turtle.begin_fill()

    for n in range(4):
        turtle.fd(w)
        turtle.rt(90)
    turtle.end_fill()

    if color == 'red':
        color = 'black'
    else: 
        color = "red"
    
    if w > 50:
        drawSquare(x +6, y + 6 ,w-12, color)
drawSquare(-150, 150, 300, 'red')
turtle.done()