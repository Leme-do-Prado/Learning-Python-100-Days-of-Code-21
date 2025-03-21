import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.5, 0.5)
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)