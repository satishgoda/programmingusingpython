#!/usr/bin/python

import inspect


def goo():
    foo()


def foo():
    top = inspect.stack()[0]
    one_below = inspect.stack()[1]

    output = '{0} in {1} at line number {2}'

    func_name, mod_name, func_def_line = top[3], top[1], top[2]

    print(output.format(func_name, mod_name, func_def_line))

    func_name, mod_name, func_def_line = one_below[3], one_below[1], one_below[2]

    print(output.format(func_name, mod_name, func_def_line))


goo()
