>>> class Foo(object):
...     """Foo yourself"""
...     def __init__(self, name):
...         self.name = name
...     def __call__(self, strfunc):
...         print("{0}: {1}".format(self.name, strfunc(self.name)))
...         
>>> upper = Foo("upper")
>>> upper(str.upper)
upper: UPPER

>>> 
>>> lower = Foo("LOWER")
>>> lower(str.lower)
LOWER: lower