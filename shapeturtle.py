import turtle
wn = turtle.Screen()
wn.bgcolor("black")
tess = turtle.Turtle()
tess.color("white")
tess.shape("turtle")

dist = 5
tess.up()                     # this is new
for _ in range(60):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist += 2
wn.exitonclick()