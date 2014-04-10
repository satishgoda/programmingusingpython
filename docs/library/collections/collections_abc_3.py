from collections import abc


>>> isinstance([], abc.Container)
True


>>> isinstance({}, abc.Container)
True


>>> isinstance('dsfs', abc.Container)
True


>>> isinstance(1, abc.Container)
False


>>> isinstance(set(), abc.Container)
True


>>> isinstance(set(), abc.Sized)
True


>>> isinstance({}, abc.Sized)
True


>>> isinstance(float, abc.Sized)
False


>>> class Foo:
...     def __len__(self):
...         pass
...         

>>> isinstance(Foo, collections.abc.Sized)
False


>>> isinstance(Foo(), collections.abc.Sized)
True


>>> len(Foo())
Traceback (most recent call last):
  File "<blender_console>", line 1, in <module>
TypeError: 'NoneType' object cannot be interpreted as an integer


>>> class Foo:
...     def __len__(self):
...         return id(self)
...         

>>> isinstance(Foo(), collections.abc.Sized)
True


>>> len(Foo())
46912756245136


>>> len(Foo())
46912756244880


>>> len(Foo())
46912756245328


>>> len(Foo())
46912756244560
