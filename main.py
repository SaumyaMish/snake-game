from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

# screen setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

# creating objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# snake move controller
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

def exit_game():
    screen.bye()

screen.onkey(fun=exit_game, key="Escape")


pace = 0.2
game_is_on = True

while game_is_on:
    time.sleep(pace)
    screen.update()
    snake.move()

    # Detect snake's collision with food
    if snake.head.distance(food) < 17:
        scoreboard.update_scores()
        snake.single_segment()
        food.refresh()

    # Detect snake's collision with wall
    if (snake.head.xcor() >= 280) or (snake.head.xcor() <= -280) or (snake.head.ycor() >= 270) or (snake.head.ycor() <= -280):
        scoreboard.game_over()
        scoreboard.reset()
        game_is_on = False


        "to Restart game automatically uncomment the below line and comment out the above two line         " \
        " scoreboard.game_over() and  game_is_on = False"
        # snake.reset()


    # Detect snake's collision with itself(tail)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            scoreboard.reset()
            game_is_on = False

            "to Restart game automatically uncomment the below line and comment out the above two line         " \
            " scoreboard.game_over() and  game_is_on = False"
            # snake.reset()


screen.exitonclick()
