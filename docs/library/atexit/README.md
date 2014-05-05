> The atexit module defines functions to register and unregister cleanup functions. Functions thus registered are automatically executed upon normal interpreter termination. atexit runs these functions in the reverse order in which they were registered; if you register A, B, and C, at interpreter termination time they will be run in the order C, B, A.
>
> Note: The functions registered via this module are not called when the program is killed by a signal not handled by Python, when a Python fatal internal error is detected, or when os._exit() is called.

* https://docs.python.org/dev/library/atexit.html

```python
#!/usr/bin/env python

import atexit
import sys

context = {}

def exitfunc1(context):
    print(exitfunc1.__name__)
    print(context.items())

atexit.register(exitfunc1, context)

context['state'] = 100

#@atexit.register
#def exitfunc1():
    #print(exitfunc1.__name__)


#exit(0)

#try:
    #sys.exit(10)
#except SystemExit as e:
    #print("Exception {0} raised with value {1}".format(e.__class__.__name__, e))
    #raise e
```
