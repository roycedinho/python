import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Fun with Shapes")
screen.bgcolor("lightblue")  # Set background color

# Create turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# Function to draw and fill a polygon
def draw_polygon(turtle_obj, sides, length, fill_color):
    angle = 360 / sides
    turtle_obj.fillcolor(fill_color)
    turtle_obj.begin_fill()
    for _ in range(sides):
        turtle_obj.forward(length)
        turtle_obj.right(angle)
    turtle_obj.end_fill()

# Draw Equilateral Triangle
t.penup()
t.goto(-200, 100)
t.pendown()
draw_polygon(t, 3, 100, "red")

# Draw Rectangle
t.penup()
t.goto(0, 100)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.right(90)
    t.forward(80)
    t.right(90)
t.end_fill()

# Draw Hexagon
t.penup()
t.goto(150, -50)
t.pendown()
draw_polygon(t, 6, 70, "yellow")

t.hideturtle()
turtle.done()
