from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

r_paddle = Paddle(xcor=350, ycor=0)
l_paddle = Paddle(xcor=-350, ycor=0)
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor(0, 0, 0)
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


gameState = 1
delay = 0.05

while gameState:
    ball.move()
    screen.update()
    time.sleep(delay)

    # Detect collision with top/bottom wall
    if ball.hit_wall():
        ball.wall()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and 325 < ball.xcor() < 335:
        print("Paddle!")
        ball.paddle()
        delay *= 0.75
    elif ball.distance(l_paddle) < 50 and -335 < ball.xcor() < -325:
        print("Paddle!")
        ball.paddle()
        delay *= 0.75

    # Detect ball being scored
    if ball.xcor() > 420:
        ball.goto(0, 0)
        ball.deg = 135
        ball.setheading(135)
        l_paddle.goto(-350, 0)
        r_paddle.goto(350, 0)
        scoreboard.l_score += 1
        scoreboard.score()
        delay = 0.05
    elif ball.xcor() < -420:
        ball.goto(0, 0)
        ball.deg = 45
        ball.setheading(45)
        l_paddle.goto(-350, 0)
        r_paddle.goto(350, 0)
        scoreboard.r_score += 1
        scoreboard.score()
        delay = 0.05

screen.exitonclick()
