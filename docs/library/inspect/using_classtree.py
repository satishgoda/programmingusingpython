import types
import turtle

from turtle import *

from classtree import trace

seen = set()

for clsname in turtle._tg_classes:
    cls = eval(clsname)
    if cls in seen:
        continue
    seen.add(cls)
    if isinstance(cls, types.TypeType):
        print
        print('-'*79)
        print(clsname)
        trace(cls)    
