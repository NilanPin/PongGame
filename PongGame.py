# Python Pong Game

# Import the libraries needed.
import time
import turtle
# Height and Width variables

Height = 600
Width = 800

# intialises window for the game
GameWindow = turtle.Screen()
# Declares window size, colour and title
GameWindow.title("Pong Game in Python")
GameWindow.bgcolor("black")
GameWindow.setup(width = Width, height = Height)
GameWindow.tracer(0)

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid= 4.5, stretch_len= 1)
paddleA.penup()
paddleA.goto(-Width/2.29 , 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid= 4.5, stretch_len= 1)
paddleB.penup()
paddleB.goto(Width/2.29, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0 , 0)
# Separate movement in x and y movements
Ball.dx = 0.2
Ball.dy = 0.2

# Functions declared
def PaddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def PaddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def PaddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def PaddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keyboard binding
GameWindow.listen()
GameWindow.onkey(PaddleAUp,"w")
GameWindow.onkey(PaddleADown,"s")
GameWindow.onkey(PaddleBUp,"Up")
GameWindow.onkey(PaddleBDown,"Down")

# Flag for main game loop
flag = True

while flag:
    GameWindow.update()

    # Move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # border check

    #Upper
    if Ball.ycor() > Height/2 - 10:
        Ball.sety(290)
        Ball.dy *= -1
    #Lower
    if Ball.ycor() < -Height/2 - 10:
        Ball.sety(-290)
        Ball.dy *= -1

    #
    if Ball.xcor() > Width/2 - 10:
        Ball.goto(0,0)
        Ball.dx *= -1

    if Ball.xcor() < -Width/2 - 10:
        Ball.goto(0,0)
        Ball.dx *= -1

    # Paddle Ball collusion

    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < paddleB.ycor() + 50 and Ball.ycor() > paddleB.ycor() - 50):
        Ball.sety(340)
        Ball.dx *= -1

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddleA.ycor() + 50 and Ball.ycor() > paddleA.ycor() - 50):
        Ball.sety(-340)
        Ball.dx *= -1