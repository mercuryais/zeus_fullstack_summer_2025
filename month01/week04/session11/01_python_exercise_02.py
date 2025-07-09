import turtle
turtle.speed(0)
i = int(input("Ta heden udaa davtah ve"))
gradus = int(input("Heden gradus awah ve"))
for n in range (i):
    turtle.right(gradus)
    for n in range(4):
        turtle.forward(100)
        turtle.right(90)
turtle.done()