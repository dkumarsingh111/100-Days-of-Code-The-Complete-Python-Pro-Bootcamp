from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILE_PATH = "c:/Users/testinganswers/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/Day-24"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        with open(f"{FILE_PATH}/data.db") as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(f"{FILE_PATH}/data.db", mode="w") as data:
                data.write(f"{self.high_score}") 
        self.score = 0
        self.update_scoreboard()   

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
