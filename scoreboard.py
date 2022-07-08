from turtle import Turtle
ALIGN, FONT = "center",("Courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.update_score()
    def update_score(self):
        self.goto(0, 250)
        self.write(f"Score: {self.player_score}", align=ALIGN, font=FONT)
    def point(self):
        self.player_score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
