import turtle
wm = turtle.Screen()
chepe = turtle.Turtle()
chepe.shape("turtle")
chepe.penup()
for size in range(10):
    chepe.forward(50)
    chepe.stamp()
    chepe.forward(-50)
    chepe.right(36)
wm.exitonclick()