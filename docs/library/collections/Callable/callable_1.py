from collections import Callable


class Func(Callable):
    def __init__(self):
        super(Func, self).__init__()
        self.results = {}

    def __call__(self, x, y):
        result = self.results.get((x, y))

        if result:
            print "Cached result: ", result
            return

        result = x, y
        self.results[(x, y)] = result

        print "Computed result: ", result

func = Func()

try:
    func()
except Exception as e:
    print(e)

func(1, 2)

__USAGE__ ="""
func()

__call__() takes exactly 3 arguments (1 given)

func(1, 2)
Computed result:  (1, 2)
func(1, 2)
Cached result:  (1, 2)
func(1, 2)
Cached result:  (1, 2)
func(1, 2)
Cached result:  (1, 2)
func(1, 2)
Cached result:  (1, 2)
func(1, 2)
Cached result:  (1, 2)
func(1, 2)
Cached result:  (1, 2)
"""
