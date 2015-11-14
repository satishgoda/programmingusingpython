# import pdb
# pdb.set_trace()

class Property(object):
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, self.default)
        
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __repr__(self):
        s = super(Property, self).__repr__()
        return self.name + " " + s
    
class IntProperty(Property):
    default = 0
    
class FloatProperty(Property):
    default = 0.0
    
class StringProperty(Property):
    default = "You did not specify anything"

class Properties(tuple):
    pass

class ClassWithProperties(type):

    def __new__(mcs, name, bases, namespace):
        properties = []
        for var, value in namespace.iteritems():
            if isinstance(value, Property):
                value.name = var
                properties.append(value)
        namespace['properties'] = property(lambda cls: tuple(properties[:]))
        cls = super(mcs, mcs).__new__(mcs, name, bases, namespace)
        return cls

class PropertyGroup(Property):
    __metaclass__ = ClassWithProperties

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            per_instance_group = instance.__dict__.get(self.name)
            if per_instance_group is None:
                instance.__dict__[self.name] = per_instance_group = self.__class__()
            return per_instance_group

    def __set__(self, instance, value):
        raise ValueError("You cannot set a PropertyGroup")
    
class AppClass(object):
    __metaclass__ = ClassWithProperties
    
    def resetToDefaults(self):
        for prop in self.properties:
            value = self.__dict__.get(prop.name, None)
            if value and value != prop.default:
                del self.__dict__[prop.name]
    
    def saveAsPreset(self, name):
        props = []
        
        for prop in self.properties:
            value = self.__dict__.get(prop.name, None)
            if value and value != prop.default:
                props.append((prop.name, value))
        
        if props:
            return (name, props)
        
        raise UserWarning("Nothing to be saved")
    
    def applyPreset(self, preset):
        for attr, value in preset[1]:
            setattr(self, attr, value)
        
class SettingsGroup(PropertyGroup):
    age = IntProperty()
    author = StringProperty()

class FoldersGroup(PropertyGroup):
    folder1 = SettingsGroup()
    folder2 = SettingsGroup()
    
class Foo(AppClass):
    x = IntProperty()
    y = FloatProperty()
    z = StringProperty()
    settings = SettingsGroup()
    folders = FoldersGroup()

