import turtle
import time 
import random

delay = 0.1 

score = 0 
high_score = 0 
#set up the screen 
wn = turtle.Screen() 
#naming the window 
wn.title('Snake Game')
#the width and length of the screen 
wn.setup(width=600, height=600) 
#background color of the screen 
wn.bgcolor("Black")
#turns off the animation on the screen (screen updates) 
wn.tracer(0) 


##creating the snake head
head = turtle.Turtle()   
#animation speed (set at 0 because that is the fastest time)
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop" 

#snake food 
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("blue")
food.penup()
food.goto(0,150)

body = [] 

#create a turtle to create a pen 
pen = turtle.Turtle() 
pen.speed(0)
pen.shape('circle')
pen.color("red")
pen.penup() 
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0  High Score: 0", align="center", font =("Courier", 24, "normal"))

#functions for the snake to change directions 
def go_up():
    if head.direction != "down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"
        
def go_left():
    if head.direction != "right":
        head.direction = "left"
        
def go_right():
    if head.direction != "left":
        head.direction = "right"
        
#functions 
def move():
    if head.direction == "up":
        y = head.ycor() 
        head.sety(y+20) 

    if head.direction == "down":
        y = head.ycor() 
        head.sety(y-20) 

    if head.direction == "right":
        x = head.xcor() 
        head.setx(x+20) 
        
    if head.direction == "left":
        x = head.xcor() 
        head.setx(x-20) 

#keyboard binding 
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the body
        for x in body:
            x.goto(1000, 1000)
        
        # Clear the body list
        body.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a x
        new_x = turtle.Turtle()
        new_x.speed(0)
        new_x.shape("square")
        new_x.color("grey")
        new_x.penup()
        body.append(new_x)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end body first in reverse order
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)

    # Move x 0 to where the head is
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    move()    

    # Check for head collision with the body body
    for x in body:
        if x.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the body
            for x in body:
                x.goto(1000, 1000)
        
            # Clear the body list
            body.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()

