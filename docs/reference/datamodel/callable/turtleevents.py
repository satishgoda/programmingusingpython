from turtle import *


class TurtleEvents(object):
        def __init__(self, turtle):
            self.turtle = turtle
    
        def __call__(self, x, y):
            print(self.turtle.pencolor())


if __name__ == '__main__':
    
    s = Screen()
    
    s.setup(600, 600)

    t1 = Turtle('triangle')
    
    t1.onclick(TurtleEvents(t1))
    
    exitonclick()
