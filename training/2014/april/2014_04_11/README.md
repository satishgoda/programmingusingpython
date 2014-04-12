Overview of terms and concepts covered today
--------------------------------------------

> __Python's builtin functionality__

```python
>>> dir(__builtins__)
```

Python's builtin functionality incorporates a broad range of concepts and form the foundational building blocks of the language. The builtins and the keywords form the framework upon which we can build scripts, programs, libraries and software frameworks.

> __sequence data types (str, tuple, list)__

Elements (Python objects) stored in a sequence are accessible using the indexing method.

```python
# string
>>> name = "Bugs Bunny"
>>> name[0]
'B'
>>> name[-1]
'y'

# tuple
>>> name = ("Bugs", "Bunny")
>>> name[0]
'Bugs'
>>> name[-1]
'Bunny'
>>> name[1] == name[-1]
True

# list
>>> name = ["Bugs", "Bunny"]
>>> name[0] == 'Bugs'
True
>>> name[1][0]
'B'
```

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

> __Python Philosophy__

```python
>>> import this

>>> credits
>>> copyright
```


> __Exercise__

Import the ```antigravity``` module

```python
>>> import antigravity
```

> __Interacting with the Python Environment__

variable assignment and module importing are two of the ways to adding entries to the environment

```python
>>> env = globals()

>>> type(env)
>>> dir(env)

>>> env

>>> import pprint
>>> pprint.pprint(env)
```

Creating an alias for the ```pprint``` function in ```pprint module```

```python
>>> pp = pprint.pprint
>>> pp(env)
>>> pp(env.keys())
>>> pp(env.values())
```

Any updates made to the environment will still be accessible from the ```env``` variable

```python
>>> age = 10
>>> pp(env)

>>> env['age']
>>> env['age'] = 100
>>> env['age']
>>> del age

>>> env
```

Testing the membership of objects in a sequence or mapping

```python
>>> 'age' in env

>>> s = 'abcde'
>>> 'A' in s
```

functions can be accessed using the dotted syntax from modules.

```python
>>> import os
>>> os.path.abspath('../')
>>> env
>>> del os
```

### Python in action: Turtle tutorial #2

In the following script, we are going to learn about the concepts of functions while using the ```turtle``` module.

```python
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
