import turtle

# Set up turtle parameters 
turtle.speed(8)
turtle.bgcolor('black')
turtle.pensize(2)

# Define colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Function to draw a hexagon
def draw_hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.right(60)

turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

# Draw interlocking hexagons
size = 50
for i in range(6):
    turtle.pencolor(colors[i])
    for _ in range(6):
        draw_hexagon(size)
        turtle.right(60)
    size += 50

turtle.hideturtle()
turtle.done()