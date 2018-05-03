#Space invaders game (With help fro YouTube tutorial)
#1st setup the screen

import turtle
import os
import math

#set up the screen

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for size in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Create the Invaders
invader = turtle.Turtle()
invader.color("red")
invader.shape("circle")
invader.penup()
invader.speed(0)
invader.setposition(-200, 250)

invaderspeed = 2

#Create the Player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#Ready = ready to fire
#Fire = bullet is firing
bulletstate = "ready"

    
#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate == "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()
    
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
                   

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


#Main game loop
while True:
    
    #Move the Invader
    x = invader.xcor()
    x += invaderspeed
    invader.setx(x)
    #Move the invader back and down
    if invader.xcor() > 280:
        y = invader.ycor()
        y -= 20
        invaderspeed *= -1
        invader.sety(y)

    if invader.xcor() < -280:
        y = invader.ycor()
        y -= 20
        invaderspeed *= -1
        invader.sety(y)

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate == "ready"

    #Check for a collision between the bullet and the invader
        if isCollision(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bulletsetposition(0, -400)
            #Reset the invader
            invader.setposition(-200, 250)
            
        







delay = raw_input("Press enter to finish.")
