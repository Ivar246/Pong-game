from turtle import Turtle, Screen
import random
from playsound import playsound

color = ['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'aqua', 'violet', 'indigo']


wn = Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(1)

# Score
score_a = 0
score_b = 0


#   Paddle A
paddle_a = Turtle()
paddle_a.speed(5)
paddle_a.shape('square')
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#   Paddle_B
paddle_b = Turtle()
paddle_b.speed(5)
paddle_b.shape('square')
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#   Ball
ball = Turtle()
ball.speed(0)
ball.shape('circle')
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# pen
pen_a = Turtle()
pen_a.speed(0)
pen_a.color('green')
pen_a.penup()
pen_a.hideturtle()
pen_a.goto(-300, 260)
pen_a.write(f"Player A : {score_a}", align="left", font=("Courier", 24, "normal"))

pen_b = Turtle()
pen_b.speed(0)
pen_b.color('blue')
pen_b.penup()
pen_b.hideturtle()
pen_b.goto(300, 260)
pen_b.write(f"Player B : {score_b}", align="right", font=("Courier", 24, "normal"))

# Function
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


    
# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#   main game loop
while True:
    wn.update()
    
    #   move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #   Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy  *= -1
        playsound('hello.mp3')

        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy  *= -1
  
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen_a.clear()
        pen_a.write(f"Player A : {score_a}", align="left", font=("Courier", 24, "normal"))
        pen_b.clear()
        pen_b.write(f"Player B : {score_b}", align="right", font=("Courier", 24, "normal"))
     
            

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen_a.clear()
        pen_a.write(f"Player A : {score_a}", align="left", font=("Courier", 24, "normal"))
        pen_b.clear()
        pen_b.write(f"Player B : {score_b}", align="right", font=("Courier", 24, "normal"))
    
    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.color(random.choice(color))
        ball.setx(340)
        ball.dx *= -1
      
 
        
 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.color(random.choice(color))
        ball.setx(-340)
        ball.dx *= -1
 