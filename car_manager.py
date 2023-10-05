from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.move_x = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.booleans = ["True", "False"]
        self.new_x = 300
        self.hideturtle()
        self.add_cars()

    def add_cars(self):
        if random.choice(self.booleans) == "True":
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(x=self.new_x, y=random.randint(-260, 260))  # Made the y-coords higher than originally anticipated to lessen total cars on screen
            car.color(random.choice(COLORS))
            car.speed("fastest")
            self.new_x += 100
            self.car_list.append(car)

    def car_move(self):
        for cars in range(len(self.car_list)):
            new_x = self.car_list[cars].xcor() - self.move_x
            self.car_list[cars].goto(new_x, self.car_list[cars].ycor())  # Sends each car to new x continuously and retains each car's random y-coordinate

    def update_speed(self):
        self.move_x += MOVE_INCREMENT
















# Old code below

# def random_coords(self):
#     for coords in range(25):
#         new_y_coords = random.randint(-240, 240)
#         self.y_coords.append(new_y_coords)


# def create_cars(self):
#     for car_index in range(100):
#         self.add_cars(car_index)


