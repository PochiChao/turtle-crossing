from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.fleet = []
        self.hideturtle()
        self.create_car()
        self.speed = MOVE_INCREMENT

    def move(self):
        for n in range(len(self.fleet)-1):
            self.fleet[n].forward(self.speed)

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            each_car = Turtle()
            each_car.penup()
            each_car.color(random.choice(COLORS))
            each_car.setheading(180)
            each_car.shape("square")
            each_car.shapesize(stretch_len=2)
            each_car.goto(310, random.randint(-240, 240))
            self.fleet.append(each_car)
