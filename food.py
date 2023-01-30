from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("turquoise")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        height_location = random.randint(-280, 280)
        width_location = random.randint(-280, 280)
        self.goto(height_location, width_location)