# creating snake class
from turtle import Turtle

# defining constants here, to make it easier to update when required
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# These are the directions to set heading of the snake, which are constants
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]   # since we are only moving first piece of snake, we named it head

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:           # to clear existing turtle existence from the screen
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)

        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # Alternative way
        # head = self.segments[0].heading()
        # if head == 90:
        #     self.segments[0].left(90)
        # elif head == 270:
        #     self.segments[0].right(90)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # Alternative way
        # head = self.segments[0].heading()
        # if head == 90:
        #     self.segments[0].right(90)
        # elif head == 270:
        #     self.segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # Alternative way
        # head = self.segments[0].heading()
        # if head == 0:
        #     self.segments[0].left(90)
        # elif head == 180:
        #     self.segments[0].right(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # Alternative way
        # head = self.segments[0].heading()
        # if head == 0:
        #     self.segments[0].right(90)
        # elif head == 180:
        #     self.segments[0].left(90)