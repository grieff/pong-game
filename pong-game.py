# Pong game in Python 3 / Python Beginners

# Library used, installed on python
import turtle

# Sound, to be able to play the sounds
# Windows ONLY
import winsound



wn = turtle.Screen()
wn.title("Classic Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# wn won't refresh itself, games are faster ¬
wn.tracer(0)

# SCORE
score_a = 0
score_b = 0

# PADDLE A / left
paddle_a = turtle.Turtle()
# speed of animation, set to max speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# stretch the width so the paddle is longer, keep the same length
# Default is 20x20px
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# to not keep drawing the paddle
paddle_a.penup()
# initial position of the paddle
paddle_a.goto(-350, 0)


# PADDLE B / right
paddle_b = turtle.Turtle()
# speed of animation, set to max speed
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
# stretch the width: paddle is longer, keep the same length
# it usually starts by default in 20x20px
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# to not keep drawing a line when it moves
paddle_b.penup()
# initial position of the paddle
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# BALL MOVEMENT
# Depends on computer, slower for faster computers
ball.dx = 1/5
ball.dy = 1/5

# Pen / SCORING - default
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
# Do not draw a line when it moves
pen.penup()
# Hide the pen, only see the text it is gonna write
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0",
          align="center", font=("Courier", 20, "normal"))


# FUNCTIONS - PADDLE MOVEMENT
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# KEYBOARD BINDING
# listen to our keyboard input
wn.listen()
# Uses wasd for one player and arrow keys for the other
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "Down")


# MAIN GAME LOOP
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        # update the score to write the actual score for each player
        # clear score before write the new one
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        # update the score to write the actual score for each player
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 20, "normal"))

    # Paddle and ball collisions
    # Paddle B / right
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
            (ball.ycor() < paddle_b.ycor() + 40) and \
            (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    # Paddle A / left
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
            (ball.ycor() < paddle_a.ycor() + 40) and \
            (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Avoid Paddles going off screen
    if paddle_b.ycor() + 50 > 300:
        paddle_b.goto(350, 250)
    if paddle_b.ycor() - 50 < -300:
        paddle_b.goto(350, -250)

    if paddle_a.ycor() + 50 > 300:
        paddle_a.goto(-350, 250)
    if paddle_a.ycor() - 50 < -300:
        paddle_a.goto(-350, -250)


