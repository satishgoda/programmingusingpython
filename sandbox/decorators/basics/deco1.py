__author__ = 'satish goda'

from oopath import Path

def main():
    p = Path(__file__)
    print("Running {}".format(p.basename))

if __name__ == '__main__':
    main()
