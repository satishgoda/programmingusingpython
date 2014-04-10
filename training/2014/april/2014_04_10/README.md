Glossary of terms covered today
-------------------------------

> __interpreter__

Just type ```python``` to launch the interpreter.

The function of an interpreter is to read expressions, statements, definitions and then evaluate them. The interpreter stops evaluating once it encounters an error.


> __function__

A function takes inputs, computes values and optionally returns them.

Examples: ```help``` ```pow``` ```dir```


> __operation__ and __operators__

Operators are used to perform operations on operands.

Examples: ```+``` ```**```

The types of the operands and the operator must be decided before hand for the computation to be valid.


> __type__

Builtin types in Python: ```int``` ```float``` ```str``` ```list``` ```dict``` ```set```


> __immutable type__

Those types whose value cannot be changed once created.

```s = 'the python language'```

Trying to change the first letter of s, ```s[0] = 'T'```, will result in an error.


> __assignment__

Example: ```age = 2**3```


> __equality testing__

Checking if ```2**3``` is equal to ```pow(2, 3)``` 

```2**3``` == ```pow(2, 3)```

The result of the above test is ```True```


> __module__

A module is a collection of attributes of different types. Modules must be imported before we can access the contained attributes.

Modules that we used today: ```math```, ```turtle```, ```math```, ```random```


```import math```

For example, in the ```math``` module, we have

```math.pi``` float attribute

```math.sin(radians)``` function attribute


The ```turtle``` module contains functionality for visual programming.

```python
import turtle

turtle.setup(width=600, height=600)

turtle.home()

turtle.forward(100)
```


Session Dump
------------
The following is a timelapse of the commands that were typed from 11:50 am - 12:23 pm
```python
help
help()
topics
keywords
help()
keywords
pow
help(pow)
pow(2, 3)
pow(2, 'satishg')
pow(2.0, 3)
2**3
2**3 == pow(2,3)
true
True
False
True == False
2*3
2+3
2-3
age
age = 2**3
age
del age
age
age = 2**3
age = float(2**3)
age
type(age)
age
age = age + 2
age
age = 100000000000000000000000000000000000000000000000000000000000000000
age = int(123.45)
age
int
float
str
list
dict
set
str.title
help(str.title)
s = "the python language"
s.title()
s
ss = s.title()
ss
s
ss[0]
ss[-1]
ss[-2]
ss[100]
s
s.capitalize()
s = s.capitalize()
s
s + s
s
import turtle
turtle
help(turtle)
dir(turtle)
turtle.setup
turtle.setup.__doc__
print(turtle.setup.__doc__)
help(turtle.setup)
turtle.setup(width=500, height=500)
turtle.home()
turtle.forward()
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.forward(-100)
turtle.clear()
turtle.home()
turtle.clear()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(-100)
sin
import math
dir(math)
math.sin(0)
math.sin(3.1415)
math.sin(3.1415/2)
math.pi
math.sin(math.pi/2)
import random
random
help(random.rand)
help(random.randint)
random.randint()
random.randint(20, 45)
random.randrange(20, 45)
help(random.randrange)
random.randint()
```
