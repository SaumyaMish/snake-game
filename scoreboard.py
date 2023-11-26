from turtle import Turtle

FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        # Score status
        self.score_status = Turtle()
        self.score_status.color("white")
        self.score_status.penup()
        self.score_status.hideturtle()
        self.score_status.score = 0
        self.score_status.goto(0,270)

        with open("highscore.txt") as hs:
            self.high_score = int(hs.read())

        self.scores()

        # for game over message
        self.color("White")
        self.hideturtle()

    def scores(self):
        self.score_status.clear()
        self.score_status.write(f"Score:{self.score_status.score} & Highest Score:{self.high_score}", align="center", font=FONT)

    def update_scores(self):
        self.score_status.score += 1
        self.scores()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center",font=FONT)
        self.goto(0,-20)
        self.write(f"[Your score:{self.score_status.score}]",align="center",font=FONT)

    def reset(self):
        if self.score_status.score > self.high_score:
            self.high_score = self.score_status.score
            with open("highscore.txt" ,mode="w") as hs:
                hs.write(f"{self.high_score}")
        self.score_status.score = 0
        self.scores()
