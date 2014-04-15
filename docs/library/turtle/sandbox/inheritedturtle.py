>>> from turtle import *

>>> s = Screen()
>>> s.setup(600, 600)

>>> t1 = Turtle('triangle')

>>> class MyTurtle(Turtle):
...     def __init__(self):
...         super(MyTurtle, self).__init__()
...     def cb_onclick(self, x, y):
...         print(self.pencolor())
...
>>> t2 = MyTurtle()
>>> t2.shape('turtle')
>>> t2.pencolor('red')
>>> t2.onclick(t2.cb_onclick)
