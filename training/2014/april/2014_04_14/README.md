# Overview of terms and concepts covered today

> __Class__

A ```class``` is a template which encapsulates the data and operations that uniquely sets it apart and using which ```instance```s can be manufactured on demand.


> __Instance__

An ```instance``` is created from a ```class``` and holds the data that differentiates it from its siblings (other instances that were created using their ```class```). When operations are called on an instance, the instance data is modified, but essentially the logic in the operation is the same for all instances. 



# Python Script ```myturtles.py```

```python
#!/usr/bin/env python

from turtle import *

s = Screen()

s.setup(600, 600)

t1 = Turtle('turtle')
t1.pencolor('red')
t1.setheading(90)
t1.fd(100)

t2 = Turtle('turtle')
t2.pencolor('blue')
t2.fd(100)

exitonclick()
```

# Executing ```myturtles.py```

```bash
linux:~> chmod +x myturtles.py
linux:~> ./myturtles.py
```

# Object Oriented Programming

In Turtle
* A Screen contains a list of turtles
* A Turtle must belong to a screen

Creating objects in Turtle
* Calling the Screen class using ```Screen()``` creates and returns an instance object

```python
>>> s = Screen()
```

* When calling a Class, we can also pass arguments*

```python
>>> t1 = Turtle("turtle")
```


```python
>>> from turtle import *
>>> dir()
>>> help(exitonclick)
>>> s = Screen()
>>> t1 = Turtle()
>>> help(Turtle)
>>> help(t1)
>>> t1.__class__
<'class turtle.Turtle'>

>>> isinstance(t1, Turtle)
True

>>> t1 == Turtle
False

>>> t1.__class__ == Turtle
True
```
