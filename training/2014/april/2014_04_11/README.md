Overview of terms and concepts covered today
--------------------------------------------

> __interpreter environment__

```python
>>> globals()
```

> __Python's builtin functionality__

```python
>>> dir(__builtins__)
```


Session Dump
------------
The following is a timelapse of the commands that were typed from 11:50 am - 12:23 pm

```python
import this
import antigravity
credits
copyright
env = globals()
type(env)
dir(env)
env
import pprint
pprint.pprint(env)
pp = pprint.pprint
pp(env)
age = 10
pp(env)
env.keys()
env.values()
'age' in env
env['age']
env['age'] = 100
env['age']
del age
env
s = 'abcde'
'A' in s
import os
os.path.abspath('../')
env
del os
from turtle import *
setup(600, 600)
home()
pencolor()
pencolor('red')
pensize()
pensize(3)
fd
forward
fd(100)
stamp()
lt(90)
bk(100)
pencolor('blue')
home()
clear()
def homeclear():
    home()
    clear()
homeclear
help(homeclear)
homeclear.__doc__ = "this homes and clears the turtle\n\n\tUse it wisely."
help(homeclear)
fd(100)
lt(100)
fd(500)
bk(300)
rt(45)
fd(100)
homeclear()
def homeclear():
    """simple doc line
            dadadadada
    """
    home()
    import time
    time.sleep(3)
    clear()
help(homeclear)
fd(100)
rt(45)
fd(100)
lt(45)
fd(10)
homeclear()
```
