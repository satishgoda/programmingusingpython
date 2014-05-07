class Foo(object):
    def __init__(self):
        self.goo = 'Foo'

    @property
    def polygon(self):
        return self.goo
    
    @polygon.setter
    def polygon(self, value):
        self.goo = []
        self.goo.append(value[0])
        self.goo.append(value[1])


foo = Foo()
foo.polygon = (1, '[0, 1, 2, 3]')


print (foo.polygon)
