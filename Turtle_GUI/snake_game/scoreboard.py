from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_update()


    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}    HighScore: {self.highscore}"  , move=False, align=ALIGNMENT,font=FONT )

    #Add the high score'
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.score_update()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        # self.clear()
        self.score_update()