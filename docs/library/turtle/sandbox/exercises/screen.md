```python

>>> from turtle import *

>>> getscreen()
<turtle._Screen object at 0x18d9a50>

>>> s = getscreen()

>>> s
<turtle._Screen object at 0x18d9a50>

>>> s.
s._RUNNING              s._color(               s._pointlist(           s.delay(
s.__class__(            s._colormode            s._rescale(             s.exitonclick(
s.__delattr__(          s._colorstr(            s._resize(              s.getcanvas(
s.__dict__              s._createimage(         s._root                 s.getshapes(
s.__doc__               s._createline(          s._setbgpic(            s.listen(
s.__format__(           s._createpoly(          s._setscrollregion(     s.mode(
s.__getattribute__(     s._delay(               s._shapes               s.onclick(
s.__hash__(             s._delayvalue           s._title                s.onkey(
s.__init__(             s._delete(              s._tracing              s.onscreenclick(
s.__module__            s._destroy(             s._turtles              s.ontimer(
s.__new__(              s._drawimage(           s._type(                s.register_shape(
s.__reduce__(           s._drawline(            s._update(              s.reset(
s.__reduce_ex__(        s._drawpoly(            s._updatecounter        s.resetscreen(
s.__repr__(             s._image(               s._window_size(         s.screensize(
s.__setattr__(          s._incrementudc(        s._write(               s.setup(
s.__sizeof__(           s._iscolorstring(       s.addshape(             s.setworldcoordinates(
s.__str__(              s._keys                 s.bgcolor(              s.title(
s.__subclasshook__(     s._listen(              s.bgpic(                s.tracer(
s.__weakref__           s._mode                 s.bye(                  s.turtles(
s._bgcolor(             s._onclick(             s.canvheight            s.update(
s._bgpic                s._ondrag(              s.canvwidth             s.window_height(
s._bgpicname            s._onkey(               s.clear(                s.window_width(
s._bgpics               s._onrelease(           s.clearscreen(          s.xscale
s._blankimage(          s._onscreenclick(       s.colormode(            s.yscale
s._canvas               s._ontimer(             s.cv

>>> s.title("Programming in Python using 'turtle' module")

>>> s.get
s.getcanvas(  s.getshapes(

>>> s.getshapes()
['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']

>>> s.getcanvas()
<turtle.ScrolledCanvas instance at 0x19057a0>

>>> c = s.getcanvas()

>>> c
<turtle.ScrolledCanvas instance at 0x19057a0>
```
