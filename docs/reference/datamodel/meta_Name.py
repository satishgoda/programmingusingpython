

class AddClassName(type):
    def __new__(cls, name, bases, classdict):
        class_object = type.__new__(cls, name, bases, classdict)
        return class_object

    def __init__(cls, name, bases, classdict):
        setattr(cls, cls.__name__, cls.__name__)


class Base(metaclass=AddClassName):
    pass


class Name(Base):
    pass


if __name__ == '__main__':
    print(Name)
    print(vars(Name))
    print(Name.Name)
    print(vars(Base))
