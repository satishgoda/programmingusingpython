#!/usr/bin/env python

from subprocess  import Popen
import os
import itertools

class RequiredBlenderStartupError(Exception):
    pass


_required_directories = ('./config', './scripts')


try:
    if not all(itertools.imap(os.path.exists, _required_directories)):
        raise RequiredBlenderStartupError("Mwhahahha")
except RequiredBlenderStartupError as e:
    print(e)
    import sys
    sys.exit(1)
else:
    p = Popen("blender", env={
                    'BLENDER_USER_CONFIG': _required_directories[0], 
                    'BLENDER_USER_SCRIPTS' : _required_directories[1], 
                    'DISPLAY': ':0',
                    'PYTHONPATH': '',
                    'PATH': '/home/satishg/bin/blenderinstalldir/'
                })


    print("Parent {0} launched child {1}".format(os.getpid(), p.pid))

    retcode = p.wait()

    print("Child process {0} terminited with retcode {1}".format(p.pid, retcode))
finally:
    print "Bye bye"

