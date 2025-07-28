import turtle
turtle.speed(0)
turtle.color("blue")
turtle.width(5)
def hexagon():
    for i in range(12):
        
        for n in range(6):
            turtle.fd(100)
            turtle.rt(60)   
        turtle.rt(30)
hexagon()
turtle.done()