from itertools import chain


class aobject:
    whatsit = 'application base object'

    def _init__message(self):
        print("Inititlizing instance {} of class {}".format(self, type(self)))


class MyMeta(type):
    def __new__(cls, name, bases, classdict, **args):
        _args = (cls, name, bases, classdict, args)
        _args_str = "{}.__new__(...)  creating {}\n\tbases: {}\n\tclassdict: {}\n\targs: {}"
        print(_args_str.format(*_args))
        
        bases = tuple(chain.from_iterable((bases, (aobject,))))
        
        print("\tCustomizing\n\t\tbases: {}".format(bases))
        
        result = type.__new__(cls, name, bases, classdict)
        
        print("\tReturned\n\t\t{}".format(result))
        
        return result


class A(metaclass=MyMeta):
    """My custom meta class"""
    def __init__(self):
        self._init__message()        


if __name__ == '__main__':
    print("class {} of type {}".format(A, type(A)))
    
    a = A()

    print(a.whatsit)

