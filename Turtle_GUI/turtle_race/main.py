import random
from turtle import *


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Set the bet", prompt="Enter the color:")
colors = ['red', 'blue', 'green', 'orange', 'black', 'cyan']
y_position = [70, 40, 10, -20, -50, -80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False #Intially it is false

if user_bet :
    is_race_on = True # check does the user willing to bet or not

#There comes the main logic the moving part of the turtles

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1,10))

        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color.lower() == user_bet.lower():
                print(f"You won! The {wining_color} turtle won the race")
            else:
                print(f"You loose! {wining_color} turtle has won")



screen.exitonclick()