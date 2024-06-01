from turtle import Turtle

FONT = ("Courier", 14, "normal")
GAME_OVER_FONT = ("Game Over", 80, "normal")
FILE_PATH="d:/Deepak/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/Day-23"


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        with open(f"{FILE_PATH}/data.db") as file:
            self.high_level = int(file.read())
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level} Highest Level: {self.high_level}", align="left", font=FONT)


    def reset(self):
        if self.level > self.high_level:
            self.high_level = self.level
            with open(f"{FILE_PATH}/data.db", mode="w") as data:
                data.write(f"{self.high_level}") 
   


    def increase_level(self):
        self.level += 1   
        self.update_scoreboard() 
        

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=GAME_OVER_FONT)
        self.reset()