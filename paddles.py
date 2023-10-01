from turtle import Turtle

class Paddles(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=3,stretch_wid=1)
        self.color('green')
        self.penup()
        self.goto(position)
