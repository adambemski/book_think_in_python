import turtle

from official_solutions import polygon


"""
4.1
"""


class Artist:

    def __init__(self):
        self.t = turtle.Turtle()

    def draw_flower(self, nr_of_petals, size):
        polygon.arc(self.t, r=(size / 2), angle=20)
        polygon.arc(self.t, r=(size / 2), angle=200)


if __name__ == '__main__':
    painter = Artist()
    painter.draw_flower(nr_of_petals=7, size=500)
