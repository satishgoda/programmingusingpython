#!/usr/bin/env python

import atexit
import sys


try:
    def exitfunc1(context):
        """Following is the state of 'context' """
        print("Python interpreter is exiting.")

        print("{0}: {1}".format(exitfunc1.__name__, exitfunc1.__doc__))

        for key, value in context.items():
            print(key, value)

    context = {}

    atexit.register(exitfunc1, context)


    context['message'] = "Python is not only a reptile"

    print(context['message'])


    def update_context(context, key, value):
        context[key] = value

    update_context(context, 'message', "Python is also a language")
    update_context(context, 'count', 1)
    update_context(context, 'status', ['OK'])

    sys.exit(1)
except SystemExit as e:
    import inspect
    print ("Exception caught : {0}({1}) : {2}".format(e.__class__.__name__, e.args[0], inspect.getdoc(e)))
    context['status'].insert(0, 'SystemExit')
    raise e
