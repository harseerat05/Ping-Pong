import turtle

screen=turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("Navy blue")

screen.listen()

Paddle1=turtle.Turtle()
Paddle1.shape("square")
Paddle1.shapesize(stretch_len=5, stretch_wid=2)
Paddle1.penup()
Paddle1.goto(-350,0)

Paddle2=turtle.Turtle()
Paddle2.shape("square")
Paddle2.shapesize(stretch_len=5, stretch_wid=2)
Paddle2.penup()
Paddle2.goto(350,0)


ball=turtle.Turtle()
ball.shape("circle")

ball.color("Green")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=-0.1

score1=0
score2=0
scoreText=turtle.Turtle()
scoreText.color("white")
scoreText.hideturtle()
scoreText.penup()
scoreText.goto(0,260)
scoreText.write("Player1: 0            Player2: 0", align="center", font=("Courier",22,"normal"))




def moveBall():
      
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    x=ball.xcor()
    y=ball.ycor()
    
    if(x>390):
        ball.setx(390)
        ball.dx=ball.dx* -1
    
    if(x<-390):
        ball.setx(-390)
        ball.dx=ball.dx* -1
        
    if(y>290):
        ball.sety(290)
        ball.dy=ball.dy* -1
    
    if(y<-290):
        ball.sety(-290)
        ball.dy=ball.dy* -1




def collision():
    if(Paddle1.xcor()+20>=ball.xcor()>= Paddle1.xcor()-20 and Paddle1.ycor()+20>=ball.ycor()>=Paddle1.ycor()-20):
        ball.dx=ball.dx* -1
        ball.dy=ball.dy* -1
        
        ball.setx(ball.xcor()+10)
        
    if(Paddle2.xcor()+20>=ball.xcor()>= Paddle2.xcor()-20 and Paddle2.ycor()+20>=ball.ycor()>=Paddle2.ycor()-20):
        ball.dx=ball.dx* -1
        ball.dy=ball.dy* -1
        
        ball.setx(ball.xcor()-10)


def paddle1_up():
    y=Paddle1.ycor()
    y+=10
    Paddle1.sety(y)
    if y>250:
        Paddle1.sety(250)
    
def paddle2_up():
    y=Paddle2.ycor()
    y+=10
    Paddle2.sety(y)
    if y>250:
        Paddle2.sety(250)
        
        

screen.onkeypress(paddle1_up,"u")
screen.onkeypress(paddle2_up,"Up")


def paddle1_down():
    y=Paddle1.ycor()
    y-=10
    Paddle1.sety(y)
    if y<-250:
        Paddle1.sety(-250)

def paddle2_down():
    y=Paddle2.ycor()
    y-=10
    Paddle2.sety(y)
    if y<-250:
        Paddle2.sety(-250)

screen.onkeypress(paddle1_down,"d")
screen.onkeypress(paddle2_down,"Down")


def paddle1_right():
    x=Paddle1.xcor()
    x+=10
    Paddle1.setx(x)
    if x>-10:
        Paddle1.setx(-10)
        
def paddle2_right():
    x=Paddle2.xcor()
    x+=10
    Paddle2.setx(x)
    if x>350:
        Paddle2.setx(350)
        
screen.onkeypress(paddle1_right,"r")
screen.onkeypress(paddle2_right,"Right")


def paddle1_left():
    x=Paddle1.xcor()
    x-=10
    Paddle1.setx(x)
    if x<-350:
        Paddle1.setx(-350)
        
def paddle2_left():
    x=Paddle2.xcor()
    x-=10
    Paddle2.setx(x)
    if x<10:
        Paddle2.setx(10)
        
screen.onkeypress(paddle1_left,"l")
screen.onkeypress(paddle2_left,"Left")



screen.tracer(0)
while(1):
    screen.update()
    moveBall()
    collision()
    
    if(ball.xcor()<=-300):
        score1+=1
        scoreText.clear()
        scoreText.write("Player1: {}            Player2: {}".format(score1, score2), align="center", font=("Courier",22,"normal"))
        ball.penup()
        ball.goto(0,0)
        ball.dx=ball.dx* -1
        
    if(ball.xcor()>=300):
        score+=1
        scoreText.clear()
        scoreText.write("Player1: {}            Player2: {}".format(score1, score2), align="center", font=("Courier",22,"normal"))
        ball.penup()
        ball.goto(0,0)
        ball.dx=ball.dx* -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        