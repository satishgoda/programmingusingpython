class Base(object):
    def __init__(self, a):
        self.A = a
        

class Derived(Base):
    def __init__(self, a, b):
        super(Derived, self).__init__(a)
        self.B = b
        
if __name__ == '__main__':
    b1 = Base("AAA")
    print(vars(b1))
    
    d1 = Derived("AAA", "BBB")
    print(vars(d1))
    
    print(d1.__class__.mro())
    
    setdir = lambda instance: set(dir(instance))
    attrsd1 = tuple(set.difference(*map(setdir, (d1, b1))))
    
    print(attrsd1)
