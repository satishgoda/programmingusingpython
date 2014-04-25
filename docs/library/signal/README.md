> This module provides mechanisms to use signal handlers in Python. The signal.signal() function allows to define custom handlers to be executed when a signal is received. A small number of default handlers are installed: SIGPIPE is ignored (so write errors on pipes and sockets can be reported as ordinary Python exceptions) and SIGINT is translated into a KeyboardInterrupt exception.

* https://docs.python.org/3.3/library/signal.html
* https://docs.python.org/2.7/library/signal.html

# Signals in *nix

```bash
linux:~> kill -INT pid

linux:~> kill -2 pid

linux:~> kill -HUP 10850
```

# Reading

* [The Linux Kernel : Signals] (http://www.win.tue.nl/~aeb/linux/lk/lk-5.html)
* [Signal Handling in Linux] (http://www.alexonlinux.com/signal-handling-in-linux)
* [Linux and Signals] (http://www.computerhope.com/unix/signals.htm)
* [What are interrupts?] (http://www.computerhope.com/jargon/i/interrup.htm)
* [SE: Catch CTRL+C signal, prompt  and exit gracefully] (http://stackoverflow.com/questions/18114560/python-catch-ctrl-c-command-prompt-really-want-to-quit-y-n-resume-executi)
* [Signals and C++] (http://stackoverflow.com/questions/4250013/is-destructor-called-if-sigint-or-sigstp-issued)
