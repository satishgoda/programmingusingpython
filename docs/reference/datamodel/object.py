
class A(object):
    def __repr__(self):
        repr = super(A, self).__repr__()
        return repr.replace('<','[').replace('>', ']')


if __name__ == '__main__':
    a = A()
    print(a)
