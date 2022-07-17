from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Courier", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Courier", 30, "bold"))
