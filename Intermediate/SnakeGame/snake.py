from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    # Creates the initial size of the snake
    def create_snake(self):
        for i in range(3):
            self.add_segment((-20 * i, 0))

    # Move the snake forward by 20 paces
    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[i - 1].xcor()
            y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    # up, down, left, right allows the snake to turn directions, while not allowing the snake to turn backward on itself
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    # adds a new segment to the snake
    def add_segment(self, position):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(position)
        self.snake_segments.append(s)

    # Extends the snake when it eats food
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
