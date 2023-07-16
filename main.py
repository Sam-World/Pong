from turtle import Screen
from line import Line
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong 2.0")
screen.tracer(0)

NUM_OF_WINS = 5

line = Line()
line.draw_line()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top / bottem wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # detect ball collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if ball misses r_paddle
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # detect if ball misses l_paddle
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

    # check first to 5
    score_l = scoreboard.l_score
    score_r = scoreboard.r_score
    if score_r == NUM_OF_WINS or score_l == NUM_OF_WINS:
        line.game_over_text()
        game_is_on = False


screen.exitonclick()
