import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Classic Game")
screen.bgcolor("black")
# turn off any animation
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
scoreboard = ScoreBoard()


# activate the key button
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    # After all the objects are created, the screen got updated
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle (make sure the ball is close enough with paddle and it is within a distance of 50 pixels)
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_left_score()

    # Detect if the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_right_score()

    if scoreboard.left_score == 4 or scoreboard.right_score  == 4:
        scoreboard.gameover()
        ball.goto(0,0)

screen.exitonclick()