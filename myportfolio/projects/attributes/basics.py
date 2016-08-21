## 

class Version(object):
    def __init__(self, value="0.1"):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

##

version = Version("0.1")

print version.value

version.value = 0.2

print version.value

##

class IntAttribute(object):
    def __init__(self, name, default):
        self.name = name
        self._default = default 
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Version1(object):
    value = IntAttribute('value', '0.0')
    
    def __init__(self, value="0.1"):
        self.value = value

##

version1 = Version1("0.1")

print version1.value

version1.value = "0.2"

print version1.value

"""
In [1]: (executing lines 2 to 13 of "version.py")

In [2]: (executing lines 16 to 23 of "version.py")
0.1
0.2

In [3]: (executing lines 26 to 44 of "version.py")

In [4]: (executing lines 47 to 54 of "version.py")
0.1
0.2
"""
