from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Board

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake GAME")
screen.tracer(0)    # to turn off the tracer

snake = Snake()
apple = Food()
board = Board()

screen.listen()

# configuring the key buttons
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    # for every 0.1 second, it updates the screen
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting if the snake has eaten the snake
    if snake.head.distance(apple) < 20:
        apple.refresh()
        snake.extend_snake()
        board.score_update()

    # Detecting if the snake hits the hall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        board.game_over()

    # Detect collision with tail.
    for square in snake.squares[1:]:
        # if any of the body has a close distance with the head
        if snake.head.distance(square) < 10:
            game_is_on = False
            board.game_over()
screen.exitonclick()