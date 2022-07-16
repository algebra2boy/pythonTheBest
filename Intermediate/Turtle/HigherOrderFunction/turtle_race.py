from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="guess the bet", prompt="Which turtle is going to win the race?")
colors = ["red", "orange", "yellow", "black", "blue", "purple"]
is_race_on = False

turtle_list = []
# initialize turtles
for i in range(6):
    turtle_list.append(Turtle(shape="turtle"))
    turtle_list[i].color(colors[i])
    turtle_list[i].penup()
    turtle_list[i].goto(x=-230,y=-100 + 40 * i)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle_color = turtle.pencolor()
            if winner_turtle_color == user_input:
                print(f"You've win. The {winner_turtle_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winner_turtle_color} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)




screen.exitonclick()