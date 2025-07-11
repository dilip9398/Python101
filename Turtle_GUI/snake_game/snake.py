
from turtle import  Turtle

STARTING_POSITION =  [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:

            self.add_segments(position)

    def add_segments(self, position):
        new_segments = Turtle(shape='square')
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extend(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != DOWN:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        pass

