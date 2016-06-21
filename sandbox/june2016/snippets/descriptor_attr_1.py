class Attribute(object):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__.get(self.name, self.default)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class IntAttribute(Attribute):
    def __init__(self, name, default):
        super(IntAttribute, self).__init__(name)
        self.default = default

class Operator(object):
    id = IntAttribute('id', 0)

print Operator.id

op1 = Operator()

print op1.id
