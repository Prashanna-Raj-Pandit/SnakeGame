import random
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Georgia", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.get_high_score()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()
        self.hideturtle()

    def get_high_score(self):
        with open("data.txt") as file:
            high_score=int(file.read())
            return high_score

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):

        self.score += 1
        self.update_scoreboard()
