import time

class AppMeta(type):
    _instances = dict()
    def __new__(cls, name, bases, classdict):
        class_object = type.__new__(cls, name, bases, classdict)
        print("Created class object {} using metaclass {}".format(class_object, cls))
        cls._instances[name] = class_object
        return class_object

    def __init__(cls, name, bases, classdict):
        cls.toc = time.asctime()
        print("Initializing class object {} @ {}".format(cls, cls.toc))


class AppType1(metaclass=AppMeta):
    _instances = dict()

    def __new__(cls, **kwargs):
        oid = kwargs['id']
        otype = kwargs['type']
        name = "{}.{}".format(otype, oid)
        if name in cls._instances:
            instance_object = cls._instances[name]
        else:
            instance_object = super(AppType1, cls).__new__(cls)
            cls._instances[name] = instance_object
            instance_object.__dict__['toc'] = time.asctime()
            print("Created instance object {} using class {}".format(instance_object, cls))
        return instance_object
    
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        print("Initializing instance object {}".format(self))



if __name__ == '__main__':
    ati1 = AppType1(**{'id':1, 'type': 'Mesh'})
    ati2 = AppType1(**{'id':2, 'type': 'Mesh'})
    ati3 = AppType1(**{'id':1, 'type': 'Mesh'})
        
    from pprint import pprint as print
    
    print(vars(ati1))
    print(vars(ati2))
    print(vars(ati3))

    time.sleep(2)    

    def __init__(self, id, otype):
        self.id = id
        self.otype = otype
        
    def __repr__(self):
        return "<{}.{} object at {}>: {} {}".format(self.__class__.__module__, self.__class__.__qualname__, 
                                                    hex(id(self)), self.id, self.otype)

    AppType2 = AppMeta("AppType2", (), {'__init__': __init__, '__repr__': __repr__})
    
    print(AppType2)
    
    for cls in type.__subclasses__(type):
        meta_class_objects = getattr(cls, '_instances', None)
        if meta_class_objects:
            for name, clsobj in meta_class_objects.items():
                print("{} was created at {}".format(clsobj, clsobj.toc))

    ati21 = AppType2.__call__(1, 'Light')
    print(ati21)
