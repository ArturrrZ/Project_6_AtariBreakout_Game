from turtle import Screen
from user import User
from ball import Ball
from paddles import Paddles
from scoreboard import Score
import time
import random

#Screen
screen=Screen()
screen.title("Atari Breakout Game")
screen.setup(width=1000,height=500)
screen.tracer(0)
#gamer
user=User()
#Ball
ball=Ball()
#Score
score=Score()
#paddles
row_1=[]
#red
x=-470
for new_paddle in range(25):
    new_paddle1 = Paddles((x,0))
    new_paddle1.color('red')
    x = x + 70
    row_1.append(new_paddle1)
    if new_paddle1.xcor() > 430:
        # print(x)
        break
#yellow
row_2=[]
x=-470
for new_paddle in range(25):

    new_paddle2 = Paddles((x,30))
    new_paddle2.shapesize(stretch_len=4,stretch_wid=1)
    new_paddle2.color('yellow')
    x = x + 90
    row_2.append(new_paddle2)
    if new_paddle2.xcor() > 400:
        # print(x)
        break
#green
row_3 = []
x = -470
for new_paddle in range(25):
    new_paddle3 = Paddles((x,60))
    new_paddle3.shapesize(stretch_len=5,stretch_wid=1)
    new_paddle3.color('green')
    x = x + 110
    row_3.append(new_paddle3)
    if new_paddle3.xcor() > 400:
        # print(x)
        break
#blue
row_4 = []
x = -470
for new_paddle in range(25):

    new_paddle4 = Paddles((x,90))
    new_paddle4.shapesize(stretch_len=15,stretch_wid=1)
    new_paddle4.color('skyblue')
    x = x + 310
    row_4.append(new_paddle4)
    if new_paddle4.xcor() > 430:
        # print(x)
        break

total_num_paddles=len(row_4) + len(row_3) + len(row_2) + len(row_1)
print(total_num_paddles)
score.p_left=total_num_paddles

screen.listen()
screen.onkey(user.go_right,"d")
screen.onkey(user.go_left,'a')

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #collision with gamer
    if  ball.distance(user) < 70 and ball.ycor() < -190:
        #50% chance
        if random.randint(1,2) == 2:
            ball.bounce_x()
        ball.bounce_y()
    #collision with border
    if ball.xcor() < -480 or ball.xcor() > 480:
        ball.bounce_x()

    #top border
    if ball.ycor() > 230:
        ball.bounce_y()
    #rows
    for paddle in row_1:
        if paddle.distance(ball) < 30:
            ball.bounce_y()
            row_1.remove(paddle)
            paddle.hideturtle()
            print(f"Red Paddles left: {len(row_1)}")
            score.p_left -=1
            score.update_score()
    for paddle in row_2:
        if paddle.distance(ball) < 30:
            ball.bounce_y()
            row_2.remove(paddle)
            paddle.hideturtle()
            print(f"Yellow Paddles left: {len(row_2)}")
            score.p_left -= 1
            score.update_score()
    for paddle in row_3:
        if paddle.distance(ball) < 30:
            ball.bounce_y()
            row_3.remove(paddle)
            paddle.hideturtle()
            print(f"Green Paddles left: {len(row_3)}")
            score.p_left -= 1
            score.update_score()
    for paddle in row_4:
        if paddle.distance(ball) < 50:
            ball.bounce_y()
            row_4.remove(paddle)
            paddle.hideturtle()
            print(f"Blue Paddles left: {len(row_4)}")
            score.p_left -= 1
            score.update_score()
    if ball.ycor() < -250:
        print("GAME OVER")
        score.game_is_over()
        game_is_on=False
    if score.p_left == 0:
        game_is_on=False
        #score


screen.exitonclick()