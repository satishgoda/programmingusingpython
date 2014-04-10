#!/usr/bin/env python

from inspect import getmro, getclasstree
from pprint import pprint


def trace(this):
    def _trace_tree(iterable):
        def _trace_bases(iterable):
            cls_name = iterable[0].__name__
            bases =[base.__name__ for base in iterable[1]]
            bases_str = ', '.join(bases) if bases else ''
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
    import exceptions
    
    trace(exceptions.OSError)
