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

> __In Turtle__

* A Screen contains a list of turtles
* A Turtle must belong to a screen

> __Creating objects in Turtle__

* Calling the Screen class using ```Screen()``` creates and returns an instance object

```python
>>> s = Screen()

>>> s.setup(600, 600)
```

> __When calling a Class, we can also pass arguments__

```python
>>> t1 = Turtle("turtle")

>>> t2 = Turtle("triangle")
```

> __Some objects contain other objects__

* For example, since all turtles must belong to a screen, the screen object ```s``` keeps track of them. 
* In order to access the list, we must use the ```turtles()``` method on the ```s```


```python
>>> s.turtles()

>>> turtles = s.turtles()

>>> turtles[0]

>>> turtles[1]
```

> __Introspection__

```python
>>> t1 is turtles[0]
True

>>> t2 is turtles[1]
True

>>> t1.__class__
<'class turtle.Turtle'>

>>> isinstance(t1, Turtle)
True

>>> t1 == Turtle
False

>>> t1.__class__ == Turtle
True
```
