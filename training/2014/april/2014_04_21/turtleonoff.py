#!/usr/bin/env python

import turtle


class ToggleTurtle(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        turtle.Turtle.__init__(self, *args, **kwargs)
        self.clicked = False
        self.onclick(self.handleClick)

    def handleClick(self, x, y):
        if self.clicked:
            self.color('red')
        else:
            self.color('green')

        self.clicked = not self.clicked


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(400, 400)

    turtle1 = ToggleTurtle('turtle')
    turtle1.fd(100)

    turtle2 = ToggleTurtle('circle')
    turtle2.bk(100)

    raw_input("Press any key to exit")
