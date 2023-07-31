from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("data.txt", "r") as hs:
            self.high_score = int(hs.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", "r") as hs:
            self.high_score = int(hs.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

#    def game_over(self):
#        self.goto(0, 0)
#        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as hs:
                self.high_score = hs.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def up_score(self):
        self.score += 1
        self.update_scoreboard()
