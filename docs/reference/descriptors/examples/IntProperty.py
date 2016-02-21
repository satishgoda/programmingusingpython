######## 

class Property(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def __set__(self, inst, value):
        if inst is None:
            return self
        else:
            inst.__dict__[self._name] = value

    def __get__(self, inst, cls):
        raise NotImplementedError("Sub classes must implement this")
    
    def resetValue(self, inst):
        if not inst.__dict__.get(self._name, None):
            raise ValueError("Property has never been initialized")
        inst.__dict__[self._name] = self._default

class IntProperty(Property):
    def __init__(self, name, description, default):
        super(IntProperty, self).__init__(name, description)
        self._default = default
    
    def __get__(self, inst, cls):
        if inst is None:
            return self
        else:
            value = inst.__dict__.get(self._name, None)
            if not value:
                return self._default
            return value
########

class Person(object):
    age = IntProperty('age', "Age of the person", -1)

########

print Person.age._name
print Person.age._description

########

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
