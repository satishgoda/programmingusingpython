__author__ = 'satish goda'

def add_counter(cls):
    setattr(cls, 'counter', 0)
    return cls


@add_counter
class C(object):
    def __init__(self):
        self.__class__.counter += 1


def main():
    print dir(C)
    print C.counter
    c1 = C()
    print C.counter
    c2 = C()
    print C.counter



if __name__ == '__main__':
    main()