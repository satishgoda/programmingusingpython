
# Keyword arguments
## Problem

```python        
        cl.addFlag('-procs <num>', 'Number of processors to use.', convert=float, default='3.1315')
        cl.addFlag('-users <str> <str>', 'Number of users to process.', paramCount=2)
```

## Explanation

```python

In [1]: emailTemplate = "{0}.{1}@burger.com"

In [2]: emailTemplate.format('victor', 'qin')
Out[2]: 'victor.qin@burger.com'

In [3]: emailTemplate = "{fname}.{lname}@burger.com"

In [4]: emailRow = {'fname': 'victor', 'lname': 'qin'}

In [5]: email
emailRow       emailTemplate 

In [5]: emailTemplate.format(**email)
emailRow       emailTemplate 

In [5]: emailTemplate.format(**emailRow)
Out[5]: 'victor.qin@burger.com'

In [6]: emailTemplate.format(emailRow)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

KeyError: 'fname'

In [7]: emailTemplate.format(*emailRow)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

KeyError: 'fname'

In [8]: emailTemplate.format(**emailRow)
Out[8]: 'victor.qin@burger.com'

In [9]: emailRow = {'fname': 'victor'}

In [10]: emailTemplate.format(**emailRow)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

KeyError: 'lname'
```

# How len() works?

```python
In [13]: def findLength(this):
   ....:     return len(this)
   ....:

In [14]: findLength([1, 2, 3])
Out[14]: 3

In [15]: findLength('string')
Out[15]: 6

In [16]: findLength(1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

/home/qjia/Desktop/scripts/<ipython console> in findLength(this)

TypeError: object of type 'int' has no len()

In [18]: import collections

In [19]: collections.
collections.Callable          collections.ValuesView        collections.__reduce__
collections.Container         collections.__all__           collections.__reduce_ex__
collections.Hashable          collections.__builtins__      collections.__repr__
collections.ItemsView         collections.__class__         collections.__setattr__
collections.Iterable          collections.__delattr__       collections.__sizeof__
collections.Iterator          collections.__dict__          collections.__str__
collections.KeysView          collections.__doc__           collections.__subclasshook__
collections.Mapping           collections.__file__          collections._abcoll
collections.MappingView       collections.__format__        collections._iskeyword
collections.MutableMapping    collections.__getattribute__  collections._itemgetter
collections.MutableSequence   collections.__hash__          collections._sys
collections.MutableSet        collections.__init__          collections.defaultdict
collections.Sequence          collections.__name__          collections.deque
collections.Set               collections.__new__           collections.namedtuple
collections.Sized             collections.__package__      

In [19]: collections.Sized
Out[19]: <class '_abcoll.Sized'>

In [20]: collections.Sized?
Type:        ABCMeta
Base Class:    <class 'abc.ABCMeta'>
String Form:    <class '_abcoll.Sized'>
Namespace:    Interactive
File:        /usr/lib64/python2.6/_abcoll.py
Docstring:
    <no docstring>


In [21]: isinstance(str, collections.Sized)
Out[21]: False

In [22]: issubclass(str, collections.Sized)
Out[22]: True

In [23]: s = collections.Sized()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

TypeError: Can't instantiate abstract class Sized with abstract methods __len__

In [24]: issubclass(list, collections.Sized)
Out[24]: True

In [25]: issubclass(tuple, collections.Sized)
Out[25]: True

In [26]: issubclass(int, collections.Sized)
Out[26]: False


In [28]: [1, 2, 3].len()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

AttributeError: 'list' object has no attribute 'len'

In [29]: [1, 2, 3].__len__()
Out[29]: 3

In [30]: len([1, 2, 3])
Out[30]: 3

In [31]: len(1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

TypeError: object of type 'int' has no len()

In [32]: 
```
