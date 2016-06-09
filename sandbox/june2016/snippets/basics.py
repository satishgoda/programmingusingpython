class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

ad  = AttrDict()

ad.x
ad.x = 10
ad['x'] = 20


class Version(object):

    def __setattr__(self, *args):
        raise TypeError("can't modify immutable instance")

    __delattr__ = __setattr__

    def __init__(self, num):
        super(Version, self).__setattr__('number', num)
        
v1 = Version(1)

del v1.number


class ReadOnlyX:
    def __setattr__(self, attr, value):
        if attr == "x":
            raise AttributeError("X is immutable")
        super().__setattr__(attr, value)
