#!/usr/bin/env python

from subprocess  import Popen
import os


p = Popen("blender", env={
                   'BLENDER_USER_CONFIG': './config', 
                   'BLENDER_USER_SCRIPTS' : './scripts', 
                   'DISPLAY': ':0',
                   'PYTHONPATH': '',
                   'PATH': '/home/satishg/bin/blenderinstalldir/'
               })


print("Parent {0} launched child {1}".format(os.getpid(), p.pid))

retcode = p.wait()

print("Child process terminited with retcode {0}".format(retcode))

