#!/usr/bin/python

import inspect


def goo():
    foo()


def foo():
    top = inspect.stack()[0]
    one_below = inspect.stack()[1]

    output = '{0} in {1} at line number {2}'

    print(output.format(top[3], top[1], top[2]))
    print(output.format(one_below[3], one_below[1], one_below[2]))


goo()
