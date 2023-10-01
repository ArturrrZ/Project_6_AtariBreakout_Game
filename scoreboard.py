from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.color('black')
        self.penup()
        self.goto(0,200)
        self.p_left=0
        # self.update_score()
        self.write(f"Break paddles", align='center', font=('Courier', 20, 'bold'))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(0,200)
        self.write(f"Paddles left: {self.p_left}", align='center', font = ('Courier', 20, 'normal') )
    def game_is_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font = ('Courier', 40, 'bold') )