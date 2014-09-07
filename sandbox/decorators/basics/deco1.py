__author__ = 'satish goda'

from oopath import Path

def path_header(wrapped):
    def wrapper(*args, **kwargs):
        p = Path(__file__)
        print("Running {}".format(p.basename))
        wrapped(*args, **kwargs)
    return wrapper

@path_header
def main(*args, **kwargs):
    print "Decorators are nice"

if __name__ == '__main__':
    print main
    main()
