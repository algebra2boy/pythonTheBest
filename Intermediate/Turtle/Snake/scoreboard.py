from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)
        self.hideturtle()

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, align=ALIGN, font=FONT)
