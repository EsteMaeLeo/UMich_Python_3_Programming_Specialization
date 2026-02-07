import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
for _ in range(20):
    elan.forward(distance)
    elan.right(90)
    distance +=  10

wn.exitonclick()