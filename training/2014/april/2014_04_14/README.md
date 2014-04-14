# About


# Python Script
```python
#!/usr/bin/env python

from turtle import *

s = Screen()

s.setup(600, 600)

t1 = Turtle('triangle')

t1.pencolor('red')

t2 = Turtle('triangle')

t2.pencolor('blue')

t1.setheading(90)

t1.fd(100)

t2.fd(100)

exitonclick()
```

# Introspecting Instances
```python
>>> import turtle
>>> dir()
>>> turtle
>>> help(turtle.exitonclick)
>>> from turtle import *
>>> t1 = Turtle()
>>> help(Turtle)
>>> help(t1)
>>> t1.__class__
>>> isinstance(t1, Turtle)
>>> t1 == Turtle
>>> t1.__class__ == Turtle
```
