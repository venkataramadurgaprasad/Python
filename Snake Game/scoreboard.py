from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score_up()

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Your score: {self.score}",move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
