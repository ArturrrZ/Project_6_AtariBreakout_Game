from turtle import Turtle

class User(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.goto(x=0,y=-210)

    def go_right(self):
        new_x=self.xcor() + 30
        self.goto(new_x,self.ycor())

    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
