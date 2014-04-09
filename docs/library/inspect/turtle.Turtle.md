About Turtle
-------------

https://docs.python.org/2.6/library/turtle.html


inspect Case Study
------------------

```python
>>> from inspect import getclasstree
>>> from pprint import pprint
>>> import turtle


>>> pprint(inspect.getclasstree(turtle.Turtle.mro(), unique=0))
[(<type 'object'>, ()),
 [(<class 'turtle.TNavigator'>, (<type 'object'>,)),
  [(<class 'turtle.RawTurtle'>,
    (<class 'turtle.TPen'>, <class 'turtle.TNavigator'>)),
   [(<class 'turtle.Turtle'>, (<class 'turtle.RawTurtle'>,))]],
  (<class 'turtle.TPen'>, (<type 'object'>,)),
  [(<class 'turtle.RawTurtle'>,
    (<class 'turtle.TPen'>, <class 'turtle.TNavigator'>)),
   [(<class 'turtle.Turtle'>, (<class 'turtle.RawTurtle'>,))]]]]


>>> pprint(getclasstree(turtle.Turtle.mro(), unique=1))
[(<type 'object'>, ()),
 [(<class 'turtle.TNavigator'>, (<type 'object'>,)),
  (<class 'turtle.TPen'>, (<type 'object'>,)),
  [(<class 'turtle.RawTurtle'>,
    (<class 'turtle.TPen'>, <class 'turtle.TNavigator'>)),
   [(<class 'turtle.Turtle'>, (<class 'turtle.RawTurtle'>,))]]]]
   

>>> len(ctree)
2

>>> ctree[0]
(<type 'object'>, ())

>>> pprint(ctree[1])
[(<class 'turtle.TNavigator'>, (<type 'object'>,)),
 (<class 'turtle.TPen'>, (<type 'object'>,)),
 [(<class 'turtle.RawTurtle'>,
   (<class 'turtle.TPen'>, <class 'turtle.TNavigator'>)),
  [(<class 'turtle.Turtle'>, (<class 'turtle.RawTurtle'>,))]]]
  
>>> len(ctree[1])
3

>>> len(ctree[1][0])
2

>>> len(ctree[1][1])
2

>>> len(ctree[1][2])
2

>>> ctree[1][0]
(<class 'turtle.TNavigator'>, (<type 'object'>,))

>>> ctree[1][1]
(<class 'turtle.TPen'>, (<type 'object'>,))

>>> pprint(ctree[1][2])
[(<class 'turtle.RawTurtle'>,
  (<class 'turtle.TPen'>, <class 'turtle.TNavigator'>)),
 [(<class 'turtle.Turtle'>, (<class 'turtle.RawTurtle'>,))]]

>>> ctree[1][2][0]
(<class 'turtle.RawTurtle'>, (<class 'turtle.TPen'>, <class 'turtle.TNavigator'>))

>>> ctree[1][2][1]
[(<class 'turtle.Turtle'>, (<class 'turtle.RawTurtle'>,))]

```
