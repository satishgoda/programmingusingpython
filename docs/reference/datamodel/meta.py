

class AppMeta(type):
    def __new__(cls, name, bases, classdict, *args):
        class_object = type.__new__(cls, name, bases, classdict)
        print("Created class object {} using metaclass {}".format(class_object, cls))
        return class_object
    
    def __init__(cls, name, bases, classdict, *args):
        print("Initializing class object {}".format(cls))


class AppType1(metaclass=AppMeta):
    def __init__(self):
        print("Initializing instance object {}".format(self))


if __name__ == '__main__':
    ati1 = AppType1()
