import random
import turtle
from turtle import  *

timmy = Turtle() # object of the turtle

timmy.shape("turtle") # shape of the cursor
timmy.pensize(width= None) # pen size
timmy.speed("fastest") # Pen speed
turtle.colormode(255) #set the color mode to rgb

#Make the random color mixes
def color_mode():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

#SpiroGraph

def spirograph(size_of_gap):
    for _ in range(int(350/size_of_gap)):
        timmy.color(color_mode())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

spirograph(5)












colors = ['red', 'blue', 'cyan', 'orange']
directions = [32,34,56,34,7,3,53,654,345,3454,53,43]

def random_walk():
    for _ in range(200):
        timmy.forward(100)
        timmy.color(random.choice(colors))
        timmy.setheading(random.choice(directions)) # setheading is set the angle and direction






# This is the basic drawing shapes

# def drawing_shapes(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         timmy.forward(100)
#         timmy.left(angle)
#
# for i in range(3,11):
#     drawing_shapes(i)



screen = Screen()
screen.exitonclick()