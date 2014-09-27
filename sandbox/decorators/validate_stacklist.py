__author__ = 'satish goda'

class StackList(object):
    def __init__(self):
        self._items = []

    def __get__(self, instance, cls):
        if instance is None:
            raise Exception("Must be accessed via a Stack instance")
        else:
            return self

    def append(self, func):
        self.callbacks.append(func)

    def __set__(self, instance, func):
        self._items.append(func)

    @property
    def callbacks(self):
        return self._items

class Stack(object):
    def __init__(self):
        self.fix = StackList()
        self.run = StackList()

    # Decorator
    def extrafix(self, func):
        self.fix.append(func)
        return func

    # Decorator
    def extrarun(self, func):
        self.run.append(func)
        return func

    def __get__(self, instance, cls):
        if instance is None:
            raise Exception("Must be accessed via an instance")
        else:
            return self

class BaseTest(object):

    def __init__(self, name):
        self.name = name

    def fix(self):
        for callback in self.stack.fix.callbacks:
            callback(self)

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
