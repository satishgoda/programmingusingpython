from collections import namedtuple

if False:
    print "class"
    class _Shape(object):
        Rectangle, Circle, Triangle = map(lambda _: property(lambda self: _), range(3))
    Shape = _Shape()
else:
    print "namedtuple"
    Shape = namedtuple('Shape', 'Rectangle Circle Triangle')(*range(3))

print Shape

print Shape.Rectangle == 0
print Shape.Circle == 1
print Shape.Triangle == 2

Shape.Rectangle, Shape.Circle, Shape.Triangle = range(3)

"""
class
<__main__._Shape object at 0x04F76D30>
True
True
True
Traceback (most recent call last):
  File "<tmp 1>", line 18, in <module>
    Shape.Rectangle, Shape.Circle, Shape.Triangle = range(3)
AttributeError: can't set attribute

namedtuple
Shape(Rectangle=0, Circle=1, Triangle=2)
True
True
True
Traceback (most recent call last):
  File "<tmp 1>", line 18, in <module>
    Shape.Rectangle, Shape.Circle, Shape.Triangle = range(3)
AttributeError: can't set attribute
"""
