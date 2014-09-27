import time


class Class1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Class2(object):
    def __new__(cls, *args, **kwargs):
        self = super(cls,cls).__new__(cls, *args, **kwargs)
        self.created  = time.asctime()
        return self

    def __init__(self, name, age):
        self.name = name
        self.age = age


class DecorateWithNew(object):
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        cls = self.cls
        instance = super(cls, cls).__new__(cls, *args, **kwargs)
        instance.created = time.asctime()
        instance.__init__(*args, **kwargs)
        return instance


@DecorateWithNew
class Class3(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    ci1 = Class1('bugs', 100)
    ci2 = Class2('lola', 98)
    ci3 = Class3('mela', 1000)

    print set.symmetric_difference(*map(set, (map(dir, (ci1, ci2)))))

    print vars(ci1)
    print vars(ci2)
    print vars(ci3)
