__author__ = 'satish goda'

from oopath import Path

from functools import wraps

def path_header(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        p = Path(__file__)
        print("Running {}".format(p.basename))
        r = wrapped(*args, **kwargs)
        return r
    return wrapper

@path_header
def main(*args, **kwargs):
    print "Decorators are nice"

if __name__ == '__main__':
    print main
    main()
