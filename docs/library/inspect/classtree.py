#!/usr/bin/env python

from inspect import getmro, getclasstree
from pprint import pprint


ENABLE_DEFAULT = False

_name = lambda cls: cls.__name__
_qualname = lambda cls: "{0}.{1}".format(cls.__module__, _name(cls))

_which_name = (_name, _qualname)

NAME_FULL = False

def trace(this):
    def _trace_tree(iterable):
        def _trace_bases(iterable):
            name = _which_name[NAME_FULL]
            derived, bases = iterable
            cls_name = name(derived)
            bases_str = ''
            if bases:
                bases_str = ', '.join([name(base) for base in bases])
            print("{0}({1})".format(cls_name, bases_str))
            
        for item in iterable:
            trace = _trace_bases if isinstance(item, tuple) else _trace_tree
            trace(item)
    
    mro = getmro(this)
    
    tree = getclasstree(mro, unique=1)
    
    print('-'*79)
    print(this)
    print('')
    
    if ENABLE_DEFAULT:
        pprint(tree)
    
        print('')
    
    _trace_tree(tree)


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description="Class Tree using inspect module")
    
    parser.add_argument('--default', '-d', action='store_true', 
                        help='print the mro() from inspect')
    parser.add_argument('--qualname', '-q', action='store_true',
                        help='print fully qualified class names')
    
    args = parser.parse_args()
    
    
    ENABLE_DEFAULT, NAME_FULL = args.default, args.qualname
        
    import collections
    trace(collections.MutableSequence)

    import turtle
    trace(turtle.Turtle)

    import numbers
    trace(numbers.Integral)
    
    trace(numbers.Rational)


