from collections import OrderedDict

######## 
class Property(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def __set__(self, inst, value):
        if inst is None:
            return self
        else:
            props = inst.__dict__.get('_props', None)
            if not props:
                props = inst.__dict__['_props'] = OrderedDict()
            props[self._name] = value

    def __get__(self, inst, cls):
        raise NotImplementedError("Sub classes must implement this")
    
    def resetValue(self, inst):
        props = inst.__dict__.get('_props', None)
        if not props:
            raise ValueError("No properties have been ever initialized")
        else:
            if not props.get(self._name, None):
                raise ValueError("Property has never been initialized")
        props[self._name] = self._default

class IntProperty(Property):
    def __init__(self, name, description, default):
        super(IntProperty, self).__init__(name, description)
        self._default = default
    
    def __get__(self, inst, cls):
        if inst is None:
            return self
        else:
            props = inst.__dict__.get('_props', None)
            if not props:
                props = inst.__dict__['_props'] = OrderedDict()
            
            value = props.get(self._name, None)
            return value or self._default

########

class Person(object):
    age = IntProperty('age', "Age of the person", -1)

########

print Person.age._name
print Person.age._description

#########

person1 = Person()
print person1.age
person1.age = 30
print person1.age

########

person2 = Person()

try:
    Person.age.resetValue(person2)
except ValueError as e:
    print e

print person2.age

person2.age = 35

print person2.age

Person.age.resetValue(person2)

print person2.age

print person2.__dict__
