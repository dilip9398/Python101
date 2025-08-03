import turtle
from  turtle import Turtle, Screen
import pandas
from tkinter import messagebox

screen = Screen()
screen.title("Guess the U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# guess = screen.textinput(title="Guess the state",prompt="Enter the State name?")
score = 0
states = pandas.read_csv("50_states.csv")
for i in range(5):
    guess = screen.textinput(title="Guess the state", prompt="Enter the State name?")
    guessed = states[states["state"] == guess.title()]
    if not guessed.empty:
        # Option 1: Use .iloc[0] after filtering
        state_name = guessed.iloc[0]["state"]
        x = guessed.iloc[0]["x"]
        y = guessed.iloc[0]["y"]
        print(f"State: {state_name}, x: {x}, y: {y}")
        score += 1

        # Option 2: Get original DataFrame index
        # orig_index = guessed.index[0]
        # print(f"Index in original DataFrame: {orig_index}")
        # print(states.loc[orig_index])  # Print the full row from the original DataFrame
    else:
        print("State not found.")

    timmy = Turtle()
    timmy.shape("circle")
    timmy.shapesize(stretch_len=0.3, stretch_wid=0.3)
    timmy.penup()
    timmy.goto(x, y)
    timmy.color("red")
    timmy.stamp()



    timmy.color("black")
    timmy.goto(x, y + 10)
    timmy.write(arg=f"{state_name}", align="center", font=('Arial', 10, 'bold'))
    timmy.hideturtle()


# turtle.write(arg=f"Total Guesses:  \n{score}/50", move=False, align="center", font=('Arial', 25, 'bold'))
messagebox.showinfo("Game Over", f"Your final score: {score}/50")


screen.exitonclick()