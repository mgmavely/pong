from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.deg = 45
        self.setheading(self.deg)
        self.color("white")
        self.penup()

    def move(self):
        self.forward(10)

    def hit_wall(self):
        return abs(self.ycor()) > 280

    def wall(self):
        if self.deg == 45:
            self.deg = 315
        elif self.deg == 315:
            self.deg = 45
        elif self.deg == 225:
            self.deg = 135
        else:
            self.deg = 225
        print(self.deg)
        self.setheading(self.deg)
        print("Wall!")

    def paddle(self):
        if self.deg == 45:
            self.deg = 135
        elif self.deg == 315:
            self.deg = 225
        elif self.deg == 225:
            self.deg = 315
        else:
            self.deg = 45
        self.setheading(self.deg)
