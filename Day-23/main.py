import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    #Detect collision with cars.
    for car in cars.all_cars:
        if car.distance(player) < 23:
            game_is_on = False
            scoreboard.game_over()


    #Detect successful crossing.
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        cars.speed_up()



screen.exitonclick()