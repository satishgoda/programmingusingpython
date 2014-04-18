import bpy
import os
import atexit
import pprint
import sys
import signal


@atexit.register
def byebye():
    print("Calling parent with pid {}".format(os.getppid()))
    #os.kill(os.getppid(), signal.SIGCHLD)
    for attr in ('is_dirty', 'is_saved'):
        value = getattr(bpy.context.blend_data, attr)
        print("{} = {}".format(attr, value))


print("{} with pid {}".format(sys.argv[0], os.getpid()))

#print(bpy.app.binary_path)

#pprint.pprint(sys.path)

bpy.context.user_preferences.view.show_splash = False

#os._exit(3)
