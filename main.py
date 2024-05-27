from turtle import Turtle, Screen
import time

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food

    if snake.head.distance(food) < 15:  # turtle.distance(turtle) this function helps to get distance between two turtle
        food.refresh()
        snake.add_new_segment()
        scoreboard.increase_score()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()

    # collision detection

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
