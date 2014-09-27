__author__ = 'satish goda'

class StackList(object):
    def __init__(self):
        self._items = []

    def __get__(self, instance, cls):
        if self is None:
            raise Exception("Must be accessed via a Stack instance")
        else:
            return self

    def __set__(self, instance, value):

class Stack(object):
    def __init__(self):
        self._stack = {}
        self._stack['run'] = []
        self._stack['fix'] = []

    # Decorator
    def extrafix(self, func):
        self.fix = func
        return func

    # Decorator
    def extrarun(self, func):
        self.run = func
        return func

    @property
    def fix(self):
        return self._stack['fix']

    @fix.setter
    def fix(self, func):
        self._stack['fix'].append(func)

    @property
    def run(self):
        return self._stack['run']

    @run.setter
    def run(self, func):
        self._stack['run'].append(func)

    def __get__(self, instance, cls):
        if instance is None:
            raise Exception("Must be accessed via an instance")
        else:
            return self

class BaseTest(object):

    def __init__(self, name):
        self.name = name

    def fix(self):
        for fixer in self.stack.fix:
            fixer(self)

    def run(self):
        pass

class Test1(BaseTest):
    stack = Stack()

    def __init__(self, name):
        BaseTest.__init__(self, name)

    @stack.extrafix
    def fix1(self):
        print "fix 1 {0}".format(self.name)

    @stack.extrafix
    def fix2(self):
        print "fix 2 {0}".format(self.name)

    def fix(self):
        print "Main Fix"
        BaseTest.fix(self)

    def run(self):
        print "Running {0}".format(self.name)

class Test2(BaseTest):
    stack = Stack()

    def __init__(self, name):
        BaseTest.__init__(self, name)

    @stack.extrafix
    def fix1(self):
        print "fix 1 {0}".format(self.name)

    def run(self):
        print "Running {0}".format(self.name)

if __name__ == '__main__':
    t = Test1("FOO GOO")
    t.run()
    t.fix()

    t = Test2("MOO FOO")
    t.run()
    t.fix()
