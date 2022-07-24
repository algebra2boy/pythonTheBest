from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Board(Turtle):

    def __init__(self):
        super().__init__()
        with open("highest_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)
        self.hideturtle()

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)
