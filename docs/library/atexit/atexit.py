#!/usr/bin/env python

import atexit


def exitfunc1():
    print("{0}: Python interpreter is exiting..".format(exitfunc1.__name__))


atexit.register(exitfunc1)


message = "Python is not only a reptile"

print(message)

exit(0)
