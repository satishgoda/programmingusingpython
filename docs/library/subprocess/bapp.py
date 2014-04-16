#!/usr/bin/env python

from subprocess  import Popen
import os
import sys
import itertools


class BlenderStartupError(Exception):
    def __init__(self, *args):
        super(BlenderStartupError, self).__init__(*args)
    
    def message(self):
        content, args = self.args
        print("{0}: {1}".format(self.__class__.__name__, content))
        for directory in args:
            print("\t{0}".format(directory))


_program = sys.argv[0]
_program_child = "blender"
_required_directories = ('./config', './scripts')
_custom_modules = '/home/satishg/blender/apps/modules'


sys.path.insert(0, _custom_modules)


try:
    import bargs
    
    p = bargs.ProgramDetails()
    
    print(p.launcher)
    
    try:
        if not all(itertools.imap(os.path.exists, _required_directories)):
            raise BlenderStartupError("The following directories do not exist",
                                                _required_directories
                                    )
    except BlenderStartupError as e:
        e.message()
        sys.exit(1)
    else:
        env = os.environ.copy()
        env['BLENDER_USER_CONFIG'] = _required_directories[0] 
        env['BLENDER_USER_SCRIPTS'] = _required_directories[1]
        env['PYTHONPATH'] = _custom_modules
        
        program_args = [_program_child]
        
        if os.path.exists('./boot.py'):
            program_args.extend('--python boot.py'.split())
        
        p = Popen(program_args, env=env)

        print("Parent {0} with pid {1} launched child with pid {2}".format(_program, os.getpid(), p.pid))

        retcode = p.wait()

        print("Child process {0} terminited with retcode {1}".format(p.pid, retcode))
       
        sys.exit(0)
    finally:
        print "Bye bye"
except SystemExit as e:
    print('The program "{0}" exited with retcode {1}'.format(_program, e.args[0]))
    
