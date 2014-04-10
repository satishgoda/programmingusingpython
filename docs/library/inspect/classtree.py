#!/usr/bin/env python

from inspect import getmro, getclasstree
from pprint import pprint
import turtle


def trace_bases(iterable):
    cls_name = iterable[0].__name__
    bases =[base.__name__ for base in iterable[1]]
    bases_str = ', '.join(bases) if bases else ''
    print("{0}({1})".format(cls_name, bases_str))


def trace_tree(iterable):
    for item in iterable:
        trace = trace_bases if isinstance(item, tuple) else trace_tree
        trace(item)


if __name__ == '__main__':
    import exceptions
    mro = getmro(exceptions.OSError)
    
    tree = getclasstree(mro, unique=1)
    
    pprint(tree)
    
    trace_tree(tree)
