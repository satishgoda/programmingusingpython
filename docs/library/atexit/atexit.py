#!/usr/bin/env python

import atexit


def exitfunc1(context):
    print("{0}: Python interpreter is exiting..".format(exitfunc1.__name__))
    for key, value in context.items():
        print(key, value)

context = {}

atexit.register(exitfunc1, context)


context['message'] = "Python is not only a reptile"

print(context['message'])


def update_context(key, value, context):
    context[key] = value

update_context('message', "Python is also a language", context)
update_context('count', 1, context)
update_context('status', 'OK', context)


exit(0)
