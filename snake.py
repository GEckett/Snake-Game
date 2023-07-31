from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]


class Snake:
    """Models the Snake that moves on screen"""

    def __init__(self):
        """Generates the initial 3 segments of the snake"""
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment_1 = Turtle(shape="square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position)
        self.all_segments.append(segment_1)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())


    def move(self):
        """Keeps all segments of the snake moving together"""
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.all_segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]