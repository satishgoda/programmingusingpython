import myhacks

ctx
# Error: NameError: file <maya console> line 1: name 'ctx' is not defined

import __builtin__

__builtin__.globals()['ctx']
# Error: KeyError: file <maya console> line 1: ctx #

__builtin__.globals()['ctx'] = myhacks.ctx

ctx

ctx.scriptEditor.comment()
ctx.scriptEditor.uncomment()

del ctx

ctx
# Error: NameError: file <maya console> line 1: name 'ctx' is not defined

myhacks.ctx
# Result: <myhacks.Context object at 0x0000000748150FD0>

del myhacks.ctx

myhacks.ctx
# Error: AttributeError: file <maya console> line 1: 'module' object has no attribute 'ctx'

reload(myhacks)
# Result: <module 'myhacks' from 'C:/Users/satish goda/Documents/maya/scripts\myhacks.pyc'>

myhacks.ctx
# Result: <myhacks.Context object at 0x0000000759F420F0>

ctx
# Error: NameError: file <maya console> line 1: name 'ctx' is not defined

__builtin__.globals()['ctx'] = myhacks.ctx

ctx == myhacks.ctx
# Result: True

ctx.foo = 1

myhacks.ctx.foo
# Result: 1
