import random
import turtle

import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)

# extract 30 colors from this picture
# colors = colorgram.extract('color.jpg', 30)
#
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r,g,b))
# print(rgb)

color_list = [(197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68), (228, 160, 47),
              (243, 247, 253), (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11), (242, 34, 164),
              (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208), (11, 97, 62), (220, 160, 10), (18, 18, 43),
              (52, 211, 230), (11, 228, 239), (80, 73, 214), (238, 156, 217), (73, 212, 168), (81, 234, 202),
              (61, 233, 241), (5, 67, 42)]
t = Turtle()
t.penup()           # hide the tracing mark
t.hideturtle()      # hide the cursor
t.speed("fastest")
t.setpos(-200, -250)
number_dots = 100

for number_dots in range(1, number_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(30)

    if number_dots % 10 == 0:  # at the last dot
        t.setheading(90)  # set the head up
        t.forward(40)     # go north
        t.setheading(180)  # set the head point to west
        t.forward(300)  # create space for 10 dots and each dot needs to h ave 30
        t.setheading(0)    # set the head point to east

screen = Screen()
screen.exitonclick()
