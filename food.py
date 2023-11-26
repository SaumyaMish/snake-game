import random
from turtle import Turtle
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("circle")
        self.shapesize(stretch_len = 0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 260)
        self.goto(random_x, random_y)
