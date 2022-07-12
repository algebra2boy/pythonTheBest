import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")
turtle.colormode(255)

# make a square
for _ in range(4):
    tim.fd(100)
    tim.lt(90)

# Draw a dash line
for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# Drawing different shapes (first is the square)

colors = ["medium aquamarine", "magenta", "yellow", "blue", "black", "pink"]



def draw_shape(number_sides: int):
    for _ in range(number_sides):
        tim.fd(100)
        tim.lt(360/number_sides)

for shape_side_n in range(2,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

# a turtle walk on different color
directions = [0, 90, 180, 270]
for _ in range(200):
    tim.pensize(10)
    tim.color(random_color())
    tim.speed(random.randint(1, 10))
    tim.forward(30)
    tim.setheading(random.choice(directions))

# making a Spirograph
tim.speed("fastest")
def draw_Spirograph(size_of_gap):
    # this would complete one cycle of a circle
    # it will run 360/size_of_gap times, but each time it will turn size_of_gap degree
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_Spirograph(5)


screen = Screen()
screen.exitonclick()
