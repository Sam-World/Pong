from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.width(4)
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=295)
        self.setheading(270)
        self.y_move = 30

    def draw_line(self):
        self.penup()
        self.goto(0, -280)
        while self.ycor() < 300:
            self.pendown()
            new_y = self.ycor() + self.y_move
            self.goto(0, new_y)
            self.penup()
            new_y = self.ycor() + self.y_move
            self.goto(0, new_y)

    def game_over_text(self):
        self.goto(10, -70)
        self.color("white")
        self.write("GAME OVER!", align="center", font=("courier", 80, "bold"))