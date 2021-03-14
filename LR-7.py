import turtle

angle = 60
length = 170
width = 1
counter = 6

while counter:
    turtle.forward(length)
    turtle.left(angle)
    turtle.speed(5)
    counter -= 1

turtle.exitonclick()