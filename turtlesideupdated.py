import turtle
import math
import random
# import os
# import time



#set up screen
wn = turtle.Screen()
wn.bgcolor('black')
# wn.bgpic("im.gif")
wn.tracer(2)

pen = turtle.Turtle()
pen.penup()

#draw boarder
pen.setposition(-300, -270)
pen.pendown()
for r in range(2):
    pen.color('white')
    pen.forward(600)
    pen.left(90)
    pen.forward(550)
    pen.left(90)
pen.hideturtle()      


#creating player turtle (instance of the turtle)

player = turtle.Turtle()
player.color('green')
player.shape('triangle')
player.penup()


#create food
max_food = 2
food = []
for r in range(max_food):
    a = turtle.Turtle()
    food.append(a)
    food[r].color('yellow')
    food[r].shape('circle')
    food[r].penup()
    food[r].speed(-1) #speed food when reapearing
    food[r].setposition(-100, -100) #food start position

max_poison = 7
posion = []
for c in range(max_poison):
    b = turtle.Turtle()
    posion.append(b)
    posion[c].color('red')
    posion[c].shape('circle')
    posion[c].penup()
    posion[c].speed(-1)
    posion[c].setposition(-60, -60)    

#set speed variable
speed = 1

def turnleft():
    player.left(30) #turn 30 degrees left

def turnright():
    player.right(30)

def speed_increment():
    global speed
    speed += 1  #increasing speed of player

def speed_decrement():
    global speed
    speed -= 1

def is_collision(tur1, tur2):

    distance = math.sqrt(math.pow(tur1.xcor()-tur2.xcor(), 2) + math.pow(tur1.ycor()-tur2.ycor(), 2)) 
    if distance < 20:
        return True
    else:
        return False

#set keyboard bindings
turtle.listen() # tells our program to set the focus to the screen and to look for a key present
turtle.onkey(turnleft, 1)# listens for the user to press a certain key and when the user presses that key it calls the given function
turtle.onkey(speed_increment, 2)
turtle.onkey(turnright, 3)
turtle.onkey(speed_decrement, 8)

#create sscore
score = 0
while score != -25:
    player.forward(speed) 
    
    #Boundary checking
    if player.xcor() > 250 or player.xcor() < -250:  # if (x, ) > 300 or (x, ) < -300
        player.right(180)                                   #turn 180 degrees

    if player.ycor() > 190 or player.ycor() < -190:
        player.right(180) 
        
    for r in range(max_poison):
        posion[r].back(1)

        if posion[r].xcor() > 250 or posion[r].xcor() < -250:
            posion[r].right(180)

        if posion[r].ycor() > 190 or posion[r].ycor() < -190:
            posion[r].right(180)    
            
        if is_collision(player, posion[r]):
        
            posion[r].setposition(random.randint(-250, 250), random.randint(-190, 190)) # randomly set food position (-300:300 , -300:300 )
            posion[r].right(random.randint(0, 360))    
            score -= 1
            pen.undo()
            pen.penup()
            pen.hideturtle()
            pen.setposition(-250, 250)
            score_str = "Score: %s" %score
            pen.write(score_str, False, align="left", font=("Arial", 20, "normal"))


    for r in range(max_food):
        food[r].forward(1)

        if food[r].xcor() > 250 or food[r].xcor() < -250:
            food[r].right(180)
            
        if food[r].ycor() > 190 or food[r].ycor() < -190:
            food[r].right(180)    

        if is_collision(player, food[r]):
        
            food[r].setposition(random.randint(-250, 250), random.randint(-190, 190)) # randomly set food position (-300:300 , -300:300 )
            food[r].right(random.randint(0, 360))
            
            score += 1
            # Draw the score on the screen
            pen.undo()
            pen.penup()
            pen.hideturtle()
            pen.setposition(-250, 250)
            score_str = "Score: %s" %score
            pen.write(score_str, False, align="left", font=("Arial", 20, "normal"))

               
turtle.mainloop()
