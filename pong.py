import turtle

wn = turtle.Screen()
wn.title("1st ping pong game")
wn.bgcolor("black")
wn.setup(width= 700, height= 600)
wn.tracer(0)

#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=6 , stretch_len= 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto((-300,0))

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=6 , stretch_len= 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto((300,0))

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_wid=1 , stretch_len= 1)
ball.color("white")
ball.penup()
ball.goto((0,0))
ball.dx = 1.5
ball.dy = 1.5
#Functions
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
#keyboard Keys

wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")
#Main game loop
while True:
    wn.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 340:
        ball.goto(0,0)
        ball.dx *= -1