# Sanke Game

import turtle
import random
import time

# Screen
game=turtle.Screen()
game.title("Snake Game")
game.bgcolor("black")
game.setup(width=500,height=600)
game.tracer(0)
line1=turtle.Turtle()
line1.color('white')
line1.pensize(2)
line1.penup()
line1.goto(-250,250)
line1.pendown()
line1.forward(500)
line1.hideturtle()

# score
score=0
high_score=0

score_display=turtle.Turtle()
score_display.color('grey')
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: 0  High Score: 0", align="center", font=("Algerian", 24, "bold"))

# snake snake
snake=turtle.Turtle()
snake.shape('square')
snake.color("light green")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"
segments=[]

# food
food=turtle.Turtle()
food.shape('circle')
food.color("red")
food.penup()
food.goto(0, 100)

# movement
def up():
    if snake.direction != "down":
        snake.direction="up"
def down():
    if snake.direction != "up":
        snake.direction="down"
def right():
    if snake.direction != "left":
        snake.direction = "right"
def left():
    if snake.direction != "right":
        snake.direction="left"
def move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

# reset game
def reset():
    global score
    time.sleep(1)
    snake.goto(0, 0)
    snake.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    update_score()

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Algerian", 24, "bold"))

# key movement
game.listen()
game.onkeypress(up,'w')
game.onkeypress(up,'Up')
game.onkeypress(down,'s')
game.onkeypress(down,'Down')
game.onkeypress(right,'d')
game.onkeypress(right,'Right')
game.onkeypress(left,'a')
game.onkeypress(left,'Left')

try:
    while True:
        game.update()
        if snake.xcor()>220 or snake.xcor()<-220 or snake.ycor()>230 or snake.ycor()<-260:
            reset()

        if snake.distance(food)<20:
            x=random.randint(-240,240)
            y=random.randint(-240,240)
            food.goto(x,y)

    # For New Segment
            new_seg=turtle.Turtle()
            new_seg.speed(0)
            new_seg.shape('square')
            new_seg.color('green')
            new_seg.penup()
            segments.append(new_seg)

            score+=1
            if score>high_score:
                high_score=score
            update_score()

        for i in range(len(segments) - 1,0,-1):
            x=segments[i - 1].xcor()
            y=segments[i - 1].ycor()
            segments[i].goto(x,y)

        if len(segments)>0:
            x=snake.xcor()
            y=snake.ycor()
            segments[0].goto(x,y)

        move()

        for segment in segments:
            if segment.distance(snake) < 20:
                reset()

        time.sleep(0.1)
except turtle.Terminator:
    print("Game exited.")
game.mainloop()