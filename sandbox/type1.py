>>> ABC = type("ABC", (object,), { char: char.upper() for char in 'abc'})
>>> 
>>> ABC
<class '__main__.ABC'>

>>> vars(ABC)
mappingproxy({'__doc__': None, '__weakref__': <attribute '__weakref__' of 'ABC' objects>, '__dict__': <attribute '__dict__' of 'ABC' objects>, 'a': 'A', 'b': 'B', 'c': 'C', '__module__': '__main__'})

>>> ABC.__dict__
mappingproxy({'__doc__': None, '__weakref__': <attribute '__weakref__' of 'ABC' objects>, '__dict__': <attribute '__dict__' of 'ABC' objects>, 'a': 'A', 'b': 'B', 'c': 'C', '__module__': '__main__'})

>>> ABC.__dict__.keys()
dict_keys(['__doc__', '__weakref__', '__dict__', 'a', 'b', 'c', '__module__'])

>>> aBC = ABC()
>>> aBC.a = aBC.a.lower()

>>> aBC
<__main__.ABC object at 0x2aaab0ead750>

>>> aBC.a
'a'

>>> aBC.b
'B'

>>> aBC.c
'C'

>>> print(aBC)
<__main__.ABC object at 0x2aaab0ead750>

>>> def __repr__(self):
...     return "Instance of class: {0} in module: {1} with value: {2} in memory: {3}".format(self.__class__.__name__, self.__class__.__module__, self, hex(id(self)))
...     
>>> 

>>> def __str__(self):
...     return "".join(map(lambda attr: getattr(self, attr), 'abc'))
...     
>>>

>>> ABC.__str__ = __str__

>>> print(aBC)
aBC

>>> print(ABC)
<class '__main__.ABC'>

>>> ABC
<class '__main__.ABC'>

>>> aBC
<__main__.ABC object at 0x2aaab0ead750>


>>> ABC.__repr__ = __repr__

>>> aBC
Instance of class: ABC in module: __main__ with value: aBC in memory: 0x2aaab0ead750

>>> print(aBC)
aBC

>>> ABC
<class '__main__.ABC'>

>>> print(ABC)
<class '__main__.ABC'>
