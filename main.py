"""
Pong Game

Author: Alan
Date: September 9th 2024

This script generates the famous pong game.
Player 1 can move right paddle with Up and Down arrow keys.
Player 2 can move left paddle with A and S keys.
This code also shows the current score.
"""

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Create new screen object to configure the width, height, title and its background color
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# Create new objects for the game elements
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# Configuring right player movement
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Configuring left player movement
screen.onkey(l_paddle.go_up, "w")
screen.onkey (l_paddle.go_down, "s")

game_is_on = True

# Simple loop to get the game on
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 410:
        scoreboard.l_point()
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()

    # Detect if left paddle misses
    if ball.xcor() < -410:
        scoreboard.r_point()
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()

screen.exitonclick()