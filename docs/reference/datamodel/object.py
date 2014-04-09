class Object:
    def __repr__(self):
        repr = super(A, self).__repr__()
        return repr.replace('<','[').replace('>', ']')


class A(Object):
    pass


if __name__ == '__main__':
    a = A()
    print(a)
