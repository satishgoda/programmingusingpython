# Intro to ```bpython```

* http://bpython-interpreter.org

# Deriving from ```list``` datatype

We want our list objects to have a length attribute (in this case a read-only ```proeprty``` called length)

```python
class ListWithLength(list):
    def __init__(self, *args):
        super(ListWithLength, self).__init__(*args)

    @property
    def length(self):
        return len(self)
```

> __Using our custom class with the builtin list class__

```python
>>> from listwithlength import ListWithLength

>>> lwl = ListWithLength((1,2,3))

>>> lwl
[1, 2, 3]

>>> l = list((4, 5, 6))

>>> l
[4, 5, 6]

>>> l + lwl
[4, 5, 6, 1, 2, 3]

>>> type(l)
<type 'list'>

>>> type(lwl)
<class 'listwithlength.ListWithLength'>
```

# Functions are objects too

```python
>>> def foo():
...     foo.was_called += 1
...
...
>>>

>>> foo.was_called = 0

>>> foo()
>>> foo()
>>> foo()

>>> foo.was_called
3
```

> __Notes__

* After the function definition of ```foo``` we need to create and initialize the ```was_called``` attribute.

