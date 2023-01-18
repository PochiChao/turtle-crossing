import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
loop_count = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.onkeypress(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    cars.create_car()
    cars.move()
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        player.next_level()
        scoreboard.increase_level()
        cars.speed *= 1.25

    for each_car in cars.fleet:
        if each_car.xcor() < -320:
            cars.fleet.remove(each_car)
        if player.distance(each_car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
