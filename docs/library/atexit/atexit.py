#!/usr/bin/env python

import atexit
import sys


def exitfunc_logger(exitfunc):
    exitfunc_logger.header_done = False

    def _draw_header():
        if exitfunc_logger.header_done:
            return
        exitfunc_logger.header_done = True
        message = "Python interpreter is exiting."
        h1 = '-'*len(message)
        print('\n'.join([h1, message, h1]))


    def wrapped(*args, **kwargs):
        _draw_header()
        print("\n>>> {0}: {1}\n".format(exitfunc.__name__, exitfunc.__doc__))
        exitfunc(*args, **kwargs)

    return wrapped


try:

    @exitfunc_logger
    def exitfunc2():
        print("Bye bye")

    @exitfunc_logger
    def exitfunc1(context):
        """Following is the state of 'context' """
        for key, value in context.items():
            print(key, value)


    context = {}

    atexit.register(exitfunc2)
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
