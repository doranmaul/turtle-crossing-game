from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.goto(-215, 260)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def update_score(self):
        self.current_level += 1
        self.clear()
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
