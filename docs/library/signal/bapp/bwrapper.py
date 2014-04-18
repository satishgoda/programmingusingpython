#!/usr/bin/env python


import os
import pprint
import sys
import subprocess
import signal


def child(_signal, frame):
    print("Child sent a message")
    #os.kill(os.getpid(), signal.SIGKILL)

signal.signal(signal.SIGCHLD, child)

print("{0} with pid {1}".format(sys.argv[0], os.getpid()))

#pprint.pprint(sys.path)

command = 'blender --python boot.py'

args = command.split()

ret = subprocess.call(args)

#signal.pause()

print(ret)

