import turtle
color = input("Enter Background color ")
tcolor = input("Enter turtle color ")
tsize = input("Enter pen size ")
wn = turtle.Screen()
wn.bgcolor(color)  # Optional: Set background color
wn.title("Turtle")  # Optional: Window title

# Create a turtle (the drawing "pen")
my_turtle = turtle.Turtle()
my_turtle.color(tcolor)  # Pen color
my_turtle.pensize(int(tsize))      # Line thickness

# Draw a simple square
for _ in range(4):
    my_turtle.forward(100)  # Move forward 100 pixels
    my_turtle.right(90)     # Turn right 90 degrees

    

# Keep window open until clicked
wn.exitonclick()