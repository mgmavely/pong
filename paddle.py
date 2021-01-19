from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(x=xcor, y=ycor)

    def up(self):
        if self.ycor() <= 225:
            self.goto(x=self.xcor(), y=self.ycor() + 25)

    def down(self):
        if self.ycor() >= -225:
            self.goto(x=self.xcor(), y=self.ycor() - 25)
