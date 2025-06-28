import random
import turtle
from turtle import *
import colorgram

rgb_colors = []
colors = colorgram.extract("image_hirst.jpg", 30)
turtle.colormode(255)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)

    rgb_colors.append(new_color)

timmy = Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")
timmy.pensize(width=20)

timmy.setheading(255)
timmy.forward(300)
timmy.setheading(0)
num = 100

# dot
for dot_count in range(1, num + 1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
