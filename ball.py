from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.speed(6)
        # self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.xmove = -10
        self.ymove = -10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
    def bounce_x(self):
        self.xmove *= -1

    def bounce_y(self):
        self.ymove *= -1