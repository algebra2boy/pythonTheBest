from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Paddle, ball set up
r_pad = Paddle(350, 0)
l_pad = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


# Make screen listen for user input
screen.listen()
screen.onkey(r_pad.move_up, "Up")
screen.onkey(r_pad.move_down, "Down")

screen.onkey(l_pad.move_up, "w")
screen.onkey(l_pad.move_down, "s")


# Playing the game
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if r_pad misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_scored()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_scored()


screen.exitonclick()
