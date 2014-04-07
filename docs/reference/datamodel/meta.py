
class AppMeta(type):
    def __new__(cls, name, bases, classdict, *args):
        class_object = type.__new__(cls, name, bases, classdict)
        print("Created class object {} using metaclass {}".format(class_object, cls))
        return class_object

    def __init__(cls, name, bases, classdict, *args):
        print("Initializing class object {}".format(cls))


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
