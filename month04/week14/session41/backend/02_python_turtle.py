import turtle
# 1
def draw_square():
    t = turtle.Turtle()
    for _ in range(4):
        t.fd(100)
        t.rt(90)
# draw_square()
# turtle.done()

# 2
def draw_triangle():
    t = turtle.Turtle()
    for _ in range(3):
        t.fd(100)
        t.rt(120)
# draw_triangle()
# turtle.done()

# 3
def draw_cross():
    t = turtle.Turtle()
    t.speed(5)
    for _ in range(4):
        t.fd(50)
        t.bk(50)
        t.rt(90)
# draw_cross()
# turtle.done()

# 4
def draw_square(side_length):
    t = turtle.Turtle()
    for _ in range(4):
        t.fd(side_length)
        t.rt(90)
    t.fd(100)
# draw_square(50)
# draw_square(100) 
# draw_square(150) 
# turtle.done()

# 5
def draw_polygon(sides, length, color):
    t = turtle.Turtle()
    t.speed(5)
    t.color(color)
    for _ in range(sides):
        t.fd(length)
        t.rt(360/sides)
# draw_polygon(3, 100, "blue")
# draw_polygon(5, 80, "red")
# turtle.done()

# 6
def five():
    t = turtle.Turtle()
    for _ in range(5):
        draw_square(50)
        turtle.fd(100)
# five()
# turtle.done()

# 7
def draw_rosette(what , color):
    t = turtle.Turtle()
    t.speed(0) 
    t.color(color)
    for _ in range(12):
        t.circle(what)
        t.rt(30)
# draw_rosette(100, "purple")
# turtle.done()

# 8
def draw_star(size, color):
    t = turtle.Turtle()
    t.color(color)
    for _ in range(5):
        t.fd(size)
        t.rt(144)
        t.fd(size)
        t.lt(72)
# draw_star(150, "red")
# turtle.done()

# 9
def draw_square(size):
    t = turtle.Turtle()
    for _ in range(4):
        t.fd(size)
        t.rt(90)
def draw_triangle(size):
    turtle.color("red")
    for _ in range(2):
        turtle.fd(size)
        turtle.lt(120)
        turtle.fd(size)
        turtle.lt(120)
def draw_house(size):
    t = turtle.Turtle()
    t.color("brown")
    draw_square(size)
    draw_triangle(size)
    t.speed(5)
draw_house(100)
turtle.done()

# 10