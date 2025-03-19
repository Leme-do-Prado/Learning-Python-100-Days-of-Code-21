from turtle import Turtle, Screen
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        new_segment.speed("fast")
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x_coord = self.segments[segment - 1].xcor()
            new_y_coord = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x_coord, new_y_coord)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(360)