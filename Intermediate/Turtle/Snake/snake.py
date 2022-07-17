from turtle import Turtle

# Global var or constant var must be capitalized
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
'''
if constant are capitalized, we do not need to set it "global ..." when we call them 
'''

class Snake:
    def __init__(self):
        self.squares = []
        self.forming_body()
        self.head = self.squares[0]

    # initializing the snake body
    def forming_body(self):
        for positions in STARTING_POSITIONS:
            self.add_square(positions)

    def add_square(self, position):
        square = Turtle(shape="square")
        square.penup()
        square.color("white")
        square.goto(position)
        self.squares.append(square)

    # increase the length of the snake by lengthening tail of the snake once it eats food
    # add the square to the same position as the last square
    def extend_snake(self):
        self.add_square(self.squares[-1].position())

    # the current square will go to the position where the
    # front square is located. 3 -> 2, 2 -> 1, 1->0
    def move(self):
        for square_pos in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_pos - 1].xcor()
            new_y = self.squares[square_pos - 1].ycor()
            self.squares[square_pos].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    # if the snake faces one direction, it cannot go backwards
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



