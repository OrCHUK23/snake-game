from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Tahoma", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
