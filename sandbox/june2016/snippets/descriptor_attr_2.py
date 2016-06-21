class Attribute(object):
    def __init__(self, defn):
        self.defn = defn
        self.value = defn.default        
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
    
    @property
    def name(self):
        return self.defn.name
    
    @property
    def default(self):
        return self.defn.default
    
    def __repr__(self):
        __repr__ = object.__repr__(self)
        return "{0} value={1}".format(__repr__, self.value)

class IntAttribute(Attribute):
    def __init__(self, defn):
        super(IntAttribute, self).__init__(defn)

class AttributeDefinition(object):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @property
    def default(self):
        return self._default
    
    def __get__(self, instance, owner):
        # pdb.set_trace()
        if not instance:
            return self
        return instance.__dict__.setdefault(self.name, self._init())
    
    def __set__(self, instance, value):
        # pdb.set_trace()
        inst = instance.__dict__.setdefault(self.name, self._init())
        inst.value = value

class IntAttributeDefinition(AttributeDefinition):
    def __init__(self, name, default):
        super(IntAttributeDefinition, self).__init__(name)
        self._default = default
    
    def _init(self):
        return IntAttribute(self)

class Operator(object):
    id = IntAttributeDefinition('id', 0)

##

print Operator.id

op1 = Operator()

import pdb

print op1.id
print op1.id.name
print op1.id.value
print op1.id.default
op1.id.value = 20
print op1.id
print op1.id.value
