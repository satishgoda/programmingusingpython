"""
A
B
C
ABC
{'a': 'A', 'c': 'C', 'b': 'B', 'abc': 'ABC'}
"""
class A(object):
    def __init__(self):
        super(A, self).__init__()
        self.a = 'A' #self.__class__.__name__''
        print self.a


class B(object):
    def __init__(self):
        super(B, self).__init__()
        self.b = 'B' #self.__class__.__name__
        print self.b


class C(object):
    def __init__(self):
        super(C, self).__init__()
        self.c = 'C' #self.__class__.__name__
        print self.c


class ABC(C, B, A):
    def __init__(self):
        super(ABC, self).__init__()
        self.abc = self.__class__.__name__
        print self.abc


if __name__ == '__main__':
    abc = ABC()
    print(vars(abc))
