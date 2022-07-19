import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

# activate the button key
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect Collision with the any of the car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect when turtle reaches the other side
    if player.reach():
        player.go_to_start()
        car_manager.level_up()
        score_board.update_level()



screen.exitonclick()