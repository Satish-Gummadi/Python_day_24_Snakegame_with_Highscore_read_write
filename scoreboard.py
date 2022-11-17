from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 22, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        # self.high_score = 0
        with open('data.txt', mode = 'r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode = 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

