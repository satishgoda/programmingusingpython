from itertools import chain


class aobject:
    whatsit = 'application base object'


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
    pass


if __name__ == '__main__':
    a = A()
    print(A)
    print(a)
    print(type(A))
    print(type(a))
    print(a.whatsit)

