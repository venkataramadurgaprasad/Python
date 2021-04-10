import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision detection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_up()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    # if head collides with any of it's tail: call game over
    for part in snake.turtles[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
