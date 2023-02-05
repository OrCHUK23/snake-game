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
        with open("data.txt", "r") as data:  # Reading the high score from data file.
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        """
        Function handles score status and prints it.
        """
        self.clear()
        self.write(f"Score : {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Function resets current score and updates the highest score if necessary.
        """
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        """
        Function increases current score by 1.
        """
        self.score += 1
        self.update_score()
