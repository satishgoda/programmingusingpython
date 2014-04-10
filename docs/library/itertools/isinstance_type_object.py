from itertools import product, starmap


iterable = (type, object)


name = lambda c: c.__name__
onlynames = lambda i, t: map(name, (i, t))


for names in starmap(onlynames, product(iterable, repeat=2)):
    code = 'isinstance({:6}, {:6})'.format(*names)
    ret = eval(code)
    print("{} -> {}".format(code, ret))


"""
isinstance(type  , type  ) -> True
isinstance(type  , object) -> True
isinstance(object, type  ) -> True
isinstance(object, object) -> True
"""
