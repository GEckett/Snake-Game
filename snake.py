from turtle import Turtle
class Snake:
    """Models the Snake that moves on screen"""

    def __init__(self):
        """Generates the initial 3 segments of the snake"""
        self.all_segments = []
        for segment in range(0, 3):
            segment_1 = Turtle(shape="square")
            segment_1.color("white")
            segment_1.penup()
            segment_1.goto(x=(0 - (segment * 20)), y=0)
            self.all_segments.append(segment_1)
        self.head = self.all_segments[0]

    def move(self):
        """Keeps all segments of the snake moving together"""
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.all_segments[0].forward(20)


    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)


    def right(self):
        self.head.setheading(0)
