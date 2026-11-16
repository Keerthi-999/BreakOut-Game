#80's Breakout Game

import turtle

screen = turtle.Screen()
screen.title('Breakout')
screen.bgcolor('orange')
screen.setup(width=880,height=600)
screen.tracer(0)

score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('white')
pen.goto(0,260)
pen.write(f"Score:{score}", align='center', font=('Arial',16,'bold'))

# paddle
paddle = turtle.Turtle()
paddle.shape('square')
paddle.color('black')
paddle.shapesize(stretch_wid=1,stretch_len=6)
paddle.penup()
paddle.goto(0,-250)

#ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0,-100)
ball.dx = 3
ball.dy=3

bricks = []
colors = ['red','pink','yellow','green','blue']
for row in range(5):
    for col in range(10):
        brick = turtle.Turtle()
        brick.shape('square')
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1,stretch_len=2)
        brick.penup()
        x = -315 + (col*70)
        y = 250 -(row*30)
        brick.goto(x,y)
        bricks.append(brick)

# paddle movement
def move_left():
    x = paddle.xcor()
    if x > -330:
        paddle.setx(x-30)
def move_right():
    x = paddle.xcor()
    if x < 330:
        paddle.setx(x+30)
screen.listen()

screen.onkeypress(move_left,'Left')
screen.onkeypress(move_right,'Right')

def update_score():
    pen.clear()
    pen.write(
        f"Score:{score}",align='center',font=('Arial',16,'bold')
    )

while True:
    screen.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        pen.goto(0,0)
        pen.write(
            'Game Over',
            align='center',
            font = ('Arial',16,'bold')
        )
        break
    if (paddle.ycor()-15 < ball.ycor() < paddle.ycor()+15 and paddle.xcor()-60 <ball.xcor() < paddle.xcor()+60):
        ball.sety(paddle.ycor()+15)
        ball.dy *= -1
    for brick in bricks[:]:
        if ball.distance(brick) < 30:
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1
            score += 10
            update_score()
        if len(bricks) == 0:
            pen.goto(0,0)
            pen.write(
                'YOU WON!',
                align='center',
                font = ('Arial',16,'bold')
            )
            break
screen.mainloop()
