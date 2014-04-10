#!/usr/bin/env python

from inspect import getmro, getclasstree
from pprint import pprint


def trace(this):
    def _trace_tree(iterable):
        def _trace_bases(iterable):
            _qualname = lambda cls: "{0}.{1}".format(cls.__module__, cls.__name__)
            derived, bases = iterable
            cls_name = _qualname(derived)
            bases_str = ''
            if bases:
                bases_str = ', '.join([_qualname(base) for base in bases])
            print("{0}({1})".format(cls_name, bases_str))
            
        for item in iterable:
            trace = _trace_bases if isinstance(item, tuple) else _trace_tree
            trace(item)
    
    mro = getmro(this)
    
    tree = getclasstree(mro, unique=1)
    
    pprint(tree)
    
    print('')
    
    _trace_tree(tree)


if __name__ == '__main__':
    import turtle
    
    trace(turtle.Turtle)
