import turtle
window = turtle.Screen()
turtle.shape('turtle')
turtle.bgcolor('black')
turtle.color('white')
turtle.pensize(2)
turtle.speed(100000)
for i in range(360):
    turtle.pensize(i/100 + 1)
    turtle.forward(i)
    turtle.left(i/45 + 100)
    turtle.forward(i)
window.exitonclick()
