

class MyMeta(type):
    def __new__(cls, name, bases, classdict, **args):
        print("{}.__new__ called for creating {}\n\tbases: {}\n\tclassdict: {}\n\targs: {}".format(cls, name, bases, classdict, args))
        result = type.__new__(cls, name, bases, classdict)
        return result


class A(metaclass=MyMeta):
    pass


if __name__ == '__main__':
    a = A()
    print(A)
    print(a)
    print(type(A))
    print(type(a))
