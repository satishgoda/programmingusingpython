__author__ = 'satish goda'

def add_counter(cls):
    setattr(cls, 'counter', 0)
    return cls

class C(object):
    pass


def main():
    c = C()
    print dir(C)


if __name__ == '__main__':
    main()