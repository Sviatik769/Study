import turtle
window = turtle.Screen()
turtle.shape('turtle')
turtle.bgcolor('black')
turtle.color('white')
turtle.pensize(0.5)
turtle.speed(100)
for i in range(360):
    turtle.pensize(i/100 + 1)
    turtle.forward(i)
    turtle.left(i/100 + 100)
window.exitonclick()

