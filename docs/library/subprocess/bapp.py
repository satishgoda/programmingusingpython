#!/usr/bin/env python

from subprocess  import Popen
import os
import itertools

class BlenderStartupError(Exception):
    def __init__(self, *args):
        super(BlenderStartupError, self).__init__(*args)
    
    def message(self):
        content, args = self.args
        print("{0}: {1}".format(self.__class__.__name__, content))
        for directory in args:
            print("\t{0}".format(directory))


_required_directories = ('./config', './scripts')


try:
    if not all(itertools.imap(os.path.exists, _required_directories)):
        raise BlenderStartupError("The following directories do not exist",
                                            _required_directories
                                  )
except BlenderStartupError as e:
    e.message()
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

