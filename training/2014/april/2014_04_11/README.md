Overview of terms and concepts covered today
--------------------------------------------

> __Python's builtin functionality__

```python
>>> dir(__builtins__)
```

Python's builtin functionality incorporates a broad range of concepts and form the foundational building blocks of the language. The builtins and the keywords form the framework upon which we can build scripts, programs, libraries and software frameworks.

> __key value mapping (dictionary)__

Python provides a mapping datatype in which data is stored as key, value pairs.

```python
>>> person = dict()

>>> person['first_name'] = 'Bugs'
>>> person['last_name'] = 'Bunny'

>>> person.keys()
>>> person.values()
>>> person.items()
```

> __interpreter environment__

The ```globals()``` builtin function returns the environment state at call time. This function returns data of type dictionary (mapping type.)

```python
>>> globals()

>>> globals().keys()

>>> globals().values()
```

What actions populate key, value pairs in the globals() dictionary?
* Assignments statements
* import statements
* function definitions
* class definitions
* ...
* ...


> __useful modules__

```pprint``` provides functionality for [pretty printing] (https://docs.python.org/2/library/pprint.html) of data types. 
```time``` [time facilities] (https://docs.python.org/2/library/time.html)

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
