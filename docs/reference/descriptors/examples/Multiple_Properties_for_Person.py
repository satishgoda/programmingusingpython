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
            props = inst.__dict__.setdefault('_props', OrderedDict())
            props[self._name] = value

    def __get__(self, inst, cls):
        if inst is None:
            return self
        
        props = inst.__dict__.setdefault('_props', OrderedDict())
        
        return props.get(self._name, None) or self._default

    
    def resetValue(self, inst):
        props = inst.__dict__.get('_props', None)
        
        if not props:
            raise ValueError("No properties have been ever initialized")
        
        if not props.get(self._name, None):
            raise ValueError("Property has never been initialized")
        
        if not isinstance(self, PropertyHasDefaultValue):
            raise ValueError("Property cannot have a default value, so cannot reset to default")
        
        props[self._name] = self._default

########

class PropertyHasDefaultValue(object):
    def __init__(self, default):
        self._default = default

########

class IntProperty(Property, PropertyHasDefaultValue):
    def __init__(self, name, description, default):
        super(IntProperty, self).__init__(name, description)
        PropertyHasDefaultValue.__init__(self, default)

########


class StringProperty(Property):
    def __init__(self, name, description):
        super(StringProperty, self).__init__(name, description)

########

class Person(object):
    name = StringProperty("name", "Name of the person")
    age = IntProperty('age', "Age of the person", -1)
    degrees = IntProperty('degrees', "Number of degrees held by this person", 0)
    
    def __init__(self, name):
        self.name = name

########

print Person.name._description
print Person.age._name
print Person.age._description

#########

person1 = Person("Bugs Bunny")

print person1.__dict__

person1.age = 30
person1.degrees = 10000L

print person1.__dict__

########

person2 = Person("Daffy Duck")

print person2.__dict__

try:
    Person.name.resetValue(person2)
except ValueError as e:
    print e

print person2.name
print person2.age
print person2.degrees

person2.age = 35
person2.degrees = 2

print person2.__dict__

print "\nResetting person's properties to default values\n"

instance_properties = person2.__dict__['_props']

for prop_name in instance_properties:
    prop = person2.__class__.__dict__[prop_name]
    print prop._name, instance_properties[prop_name]
    try:
        prop.resetValue(person2)
    except ValueError as e:
        print "\t", e
    else:
        print "\t", prop._name, instance_properties[prop_name]
