> This module provides mechanisms to use signal handlers in Python. The signal.signal() function allows to define custom handlers to be executed when a signal is received. A small number of default handlers are installed: SIGPIPE is ignored (so write errors on pipes and sockets can be reported as ordinary Python exceptions) and SIGINT is translated into a KeyboardInterrupt exception.

* https://docs.python.org/3.3/library/signal.html
* https://docs.python.org/2.7/library/signal.html
