#!/usr/bin/env python

import signal
import time
import os


def whats_HUP(_signal, frame):
    
    if not whats_HUP.called:
        whats_HUP.called = True
    else:
        return

    with open("/home/satishg/hup.txt", 'a') as f:
        f.write("Caught hup at {0}\n".format(time.asctime()))
    
    signal.signal(signal.SIGHUP, whats_HUP.original)


if __name__ == '__main__':
    whats_HUP.original = signal.getsignal(signal.SIGHUP)
    whats_HUP.called = False
    
    signal.signal(signal.SIGHUP, whats_HUP)
    
    try:
        raw_input("send me (pid {0}) a SIGHUP".format(os.getpid()))
    except EOFError as eof:
        with open("/home/satishg/hup.txt", 'r') as f:
            lines = f.readlines()
            message = lines[-1].strip() if lines else "No previous HUP history saved"
            print('\n{line}'.format(line=message))
