from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):        
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    
    def create_cars(self):
        if randint(1, 5) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(300, randint(-250, 250))
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)


    def move_cars(self):

        for car in self.all_cars: 
            car.backward(self.car_speed)

            if car.pos()[0] < -400:
                 self.all_cars.remove(car)   

   
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
