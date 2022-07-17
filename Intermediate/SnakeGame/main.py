from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# Create a screen (600x600) with a black background and a title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creates a snake, food, and scoreboard object
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Let the screen listen for key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Playing the game
game_on = True
while game_on:
    # Updates the screen
    screen.update()
    time.sleep(0.09)

    # Tells the snake to move its position
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with the tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
