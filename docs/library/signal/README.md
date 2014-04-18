> This module provides mechanisms to use signal handlers in Python. The signal.signal() function allows to define custom handlers to be executed when a signal is received. A small number of default handlers are installed: SIGPIPE is ignored (so write errors on pipes and sockets can be reported as ordinary Python exceptions) and SIGINT is translated into a KeyboardInterrupt exception.

* https://docs.python.org/3.3/library/signal.html
* https://docs.python.org/2.7/library/signal.html

# Reading

* [Linux and Signals] (http://www.computerhope.com/unix/signals.htm)
* [SE: Catch CTRL+C signal, prompt  and exit gracefully] (http://stackoverflow.com/questions/18114560/python-catch-ctrl-c-command-prompt-really-want-to-quit-y-n-resume-executi)
* [Signals and C++] (http://stackoverflow.com/questions/4250013/is-destructor-called-if-sigint-or-sigstp-issued)
