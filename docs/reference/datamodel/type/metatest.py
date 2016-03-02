import time


class MetaTest(type):
    def __new__(mcs, name, bases, namespace):
        print("About to define class '{0}' via type '{1}'".format(name, mcs))
        print (mcs, name, bases, namespace)
        now = time.asctime()
        namespace['time'] = property(lambda self: now)
        return super(mcs, mcs).__new__(mcs, name, bases, namespace)
    
    def __init__(cls, name, bases, namespace):
        print("About to initialize class '{0}' that was defined via type '{1}'".format(cls.__name__, type(cls)))
        print (cls, name, bases, namespace)
        print cls.time
        print

class Base(object):
    __metaclass__ = MetaTest

class Derived1(Base):
    pass

class Derived2(Base):
    pass
    
print Derived1
print Derived2.__class__

d11 = Derived1()
d21 = Derived2()

print d11.time
print d21.time

# Why is time the same in both the above cases?

print Base.time
print Derived1.time
print Derived2.time

"""
>>> (executing lines 1 to 33 of "metatest.py")
About to define class 'Base' via type '<class '__main__.MetaTest'>'
(<class '__main__.MetaTest'>, 'Base', (<type 'object'>,), {'__module__': '__main__', '__metaclass__': <class '__main__.MetaTest'>})
About to initialize class 'Base' that was defined via type '<class '__main__.MetaTest'>'
(<class '__main__.Base'>, 'Base', (<type 'object'>,), {'__module__': '__main__', '__metaclass__': <class '__main__.MetaTest'>, 'time': <property object at 0x0000005A27EF9BD8>})
<property object at 0x0000005A27EF9BD8>

About to define class 'Derived1' via type '<class '__main__.MetaTest'>'
(<class '__main__.MetaTest'>, 'Derived1', (<class '__main__.Base'>,), {'__module__': '__main__'})
About to initialize class 'Derived1' that was defined via type '<class '__main__.MetaTest'>'
(<class '__main__.Derived1'>, 'Derived1', (<class '__main__.Base'>,), {'__module__': '__main__', 'time': <property object at 0x0000005A27EF9C28>})
<property object at 0x0000005A27EF9C28>

About to define class 'Derived2' via type '<class '__main__.MetaTest'>'
(<class '__main__.MetaTest'>, 'Derived2', (<class '__main__.Base'>,), {'__module__': '__main__'})
About to initialize class 'Derived2' that was defined via type '<class '__main__.MetaTest'>'
(<class '__main__.Derived2'>, 'Derived2', (<class '__main__.Base'>,), {'__module__': '__main__', 'time': <property object at 0x0000005A27F05E58>})
<property object at 0x0000005A27F05E58>

<class '__main__.Derived1'>
<class '__main__.MetaTest'>
Thu Mar 03 06:34:18 2016
Thu Mar 03 06:34:18 2016

>>> Base.time
<property object at 0x0000005A27EF9BD8>

>>> Derived1.time
<property object at 0x0000005A27EF9C28>

>>> Derived2.time
<property object at 0x0000005A27F05E58>
"""
