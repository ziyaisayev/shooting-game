import math
import turtle
import random
import time 

# Ekranin daxil olunmasi
wn=turtle.Screen()
wn.bgcolor("lightblue")
wn.setup(width=600,height=600)
wn.tracer(0)
count=0




turtle.bgcolor("lightblue")
turtle.color("blue")
turtle.speed(0)
turtle.penup()
turtle.setpos(-100,100)
turtle.write("Goals",font=("Arial",30,"bold"))
turtle.setpos(40,100)
turtle.write(count,font=("Arial",30,"bold"))
turtle.penup()






player=turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.direction="stop"
player.goto(-280,-280)
player.turtlesize(2,2,1)


bullet=turtle.Turtle()
bullet.color("black")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.turtlesize(0.3,0.3,1)
bullet.goto(0,-280)

maxGoals=6
goals=[]
color=["yellow","red","blue","green","purple","orange"]

for i in range(maxGoals):

    goals.append(turtle.Turtle())
    goals[i].color(color[i])
    goals[i].shape("circle")
    goals[i].penup()
    goals[i].speed(0)
    goals[i].setposition(random.randint(-300,300),290)

def isCollision(t1,t2):
    global count
    h=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if h<20:
        count+=1
        return True
        
    
    else:
        return False
def go_right():
    player.direction="right"
def go_left():
    player.direction="left"
def move():
    if player.direction=="left":
        x=player.xcor()
        player.setx(x-20)
    if player.direction=="right":
        x=player.xcor()
        player.setx(x+20)

wn.listen()
wn.onkey(go_right,"Right")
wn.onkey(go_left,"Left")
while True:
    
    
    wn.update()
    move()
    
    y=bullet.ycor()
    bullet.sety(y+30)
    time.sleep(0.1)
    turtle.clear()
    turtle.setpos(40,100)
    turtle.write(count,font=("Arial",30,"bold"))
    turtle.penup()
    turtle.setpos(-100,100)
    turtle.write("Goals",font=("Arial",30,"bold"))
    turtle.penup()
    
    if player.xcor()>300:
        go_left()
    if player.xcor()<-300:
        go_right()
        
    if bullet.ycor()>290:
        bullet.goto(player.xcor(),-280)
    for i in range (maxGoals):
        if isCollision(bullet,goals[i]):
           
            goals[i].setposition(random.randint(-280,280),280)
       
wn.mainloop()
    