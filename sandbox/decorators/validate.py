__author__ = 'satish goda'

class FixerStack(object):
    def __init__(self):
        self._stack = []

    def first(self, func):
        self._stack.insert(0, func)

    def add(self, func):
        self._stack.append(func)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return self._stack

class BaseTest(object):

    def __init__(self, name):
        self.name = name

    def fix(self):
        for fixer in self.fixers:
            fixer(self)

    def run(self):
        pass

class Test1(BaseTest):
    fixers = FixerStack()

    def __init__(self, name):
        BaseTest.__init__(self, name)

    @fixers.add
    def fix1(self):
        print "fix 1 {0}".format(self.name)

    @fixers.add
    def fix2(self):
        print "fix 2 {0}".format(self.name)

    def run(self):
        print "Running {0}".format(self.name)

    @fixers.first
    def fixTest1(self):
        print "Fixing"

class Test2(BaseTest):
    fixers = FixerStack()

    def __init__(self, name):
        BaseTest.__init__(self, name)

    @fixers.add
    def fix1(self):
        print "fix 1 {0}".format(self.name)

    def run(self):
        print "Running {0}".format(self.name)

    @fixers.first
    def fixTest2(self):
        print "Fixing"


if __name__ == '__main__':
    t = Test1("FOO GOO")
    t.run()
    t.fix()

    t = Test2("MOO FOO")
    t.run()
    t.fix()