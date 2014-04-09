About Turtle
-------------

https://docs.python.org/2.6/library/turtle.html


inspect Case Study
------------------

```python
>>> from inspect import getclasstree
>>> from pprint import pprint
>>> import turtle


>>> pprint(getclasstree(turtle.Turtle.mro(), unique=1))
[(<type 'object'>, ()),
 [(<class 'turtle.TNavigator'>, (<type 'object'>,)),
  (<class 'turtle.TPen'>, (<type 'object'>,)),
  [(<class 'turtle.RawTurtle'>,
    (<class 'turtle.TPen'>, <class 'turtle.TNavigator'>)),
   [(<class 'turtle.Turtle'>, (<class 'turtle.RawTurtle'>,))]]]]

```
