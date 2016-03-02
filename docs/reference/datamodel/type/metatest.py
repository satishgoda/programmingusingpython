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
