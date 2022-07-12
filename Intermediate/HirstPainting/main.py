# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as T
import random
T.colormode(255)
color_list = [(46, 97, 146), (206, 165, 87), (179, 44, 70), (98, 178, 210), (179, 152, 45), (221, 213, 109), (221, 121, 165), (201, 77, 121), (133, 88, 71), (102, 100, 183), (214, 65, 56), (123, 218, 208), (120, 43, 71), (103, 157, 59), (227, 170, 185), (19, 137, 133), (47, 189, 203), (131, 190, 172), (174, 186, 221), (150, 211, 220), (103, 51, 41), (42, 63, 101), (231, 173, 169), (57, 55, 65), (214, 209, 38), (83, 47, 32), (87, 38, 57), (9, 112, 112), (13, 93, 104)]
t = T.Turtle()

t.penup()
t.hideturtle()
t.speed("fastest")
for i in range(10):
    t.goto(-225, -225 + (50 * i))
    for j in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)

screen = T.Screen()
screen.exitonclick()
