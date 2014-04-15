class CustomRepr:
    def __repr__(self):
        repr = object.__repr__(self)
        return repr.replace('<','[').replace('>', ']')


class A(CustomRepr):
    pass


if __name__ == '__main__':
    a = A()
    print(a)
