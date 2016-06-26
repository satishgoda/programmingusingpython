class Attribute(object):
    def __init__(self, defn, instance):
        self.defn = defn
        self.value = defn.default
        self.instance = instance
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
    
    @property
    def path(self):
        return "{0}.{1}".format(self.instance.path, self.defn.name)
    
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
    def __init__(self, defn, instance):
        super(IntAttribute, self).__init__(defn, instance)

class StringAttribute(Attribute):
    def __init__(self, defn, instance):
        super(StringAttribute, self).__init__(defn, instance)

class AttributeDefinition(object):
    def __init__(self, name, default):
        self._name = name
        self._default = default
    
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
        return instance.__dict__.setdefault(self.name, self._init(instance))
    
    def __set__(self, instance, value):
        # pdb.set_trace()
        inst = instance.__dict__.setdefault(self.name, self._init(instance))
        if not self._readOnly:
            inst.value = value

class IntAttributeDefinition(AttributeDefinition):
    def __init__(self, name, default=0):
        super(IntAttributeDefinition, self).__init__(name, default)
    
    def _init(self, instance):
        return IntAttribute(self, instance)

class StringAttributeDefinition(AttributeDefinition):
    def __init__(self, name, default='Unspecified'):
        super(StringAttributeDefinition, self).__init__(name, default)
    
    def _init(self, instance):
        return StringAttribute(self, instance)

class Operator(object):
    id = IntAttributeDefinition('id', 0)
    label = StringAttributeDefinition('label')
    uid = StringAttributeDefinition('uid', '0x123')

##

print Operator.id

op1 = Operator()
op1.name = "op1"
op1.path = "op1"

##

import pdb

print op1.id
print op1.id.name
print op1.id.value
print op1.id.default

print op1.label
print op1.label.name

print op1.uid

##

op1.id.value = 20

print op1.id
print op1.id.value

##

op1.label.value = "Display Label"

print op1.label

## 

# op1.uid.value = 10

op1.label.path
op1.label.value = 'Yeah baby'
