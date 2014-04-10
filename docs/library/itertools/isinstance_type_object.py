import itertools


iterable = (type, object)


for i, t in itertools.product(iterable, repeat=2):
    names = (x.__name__ for x in (i, t))
    code = 'isinstance({:6}, {:6})'.format(*names)
    ret = eval(code)
    print("{} -> {}".format(code, ret))

"""
isinstance(type  , type  ) -> True
isinstance(type  , object) -> True
isinstance(object, type  ) -> True
isinstance(object, object) -> True
"""
