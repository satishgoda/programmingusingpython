
class Space(object):
    def __init__(self):
        self.tag = self.__class__.__name__

    def __repr__(self):
        return "{0}: {1}".format(self.__class__.__bases__[0].__name__, self.tag)

    
class View3D(Space):
    def draw(self, area):
        print("Drawing view3d {0}".format(area.dimensions))

        
class Console(Space):    
    def draw(self, area):
        print("Drawing console {0}".format(area.dimensions))


class Collection(object):
    def __init__(self):
        self.items = {}
        self.active = None    

    def new(self, item):
        self._create_and_set(item)

    def set(self, item):
        if item in self.items:
            self._set_active(item)
        else:
            self.new(item)
    
    def _create(self, item):
        self.items[item] = eval(item)()
        
    def _set_active(self, item):
        self.active = self.items[item]

    def _create_and_set(self, item):
        self._create(item)
        self._set_active(item)    
        
    def __repr__(self):
        return ' '.join(self.items.keys()) + '\n  ' + str(self.active)


class Area(object):
    dimensions = (400, 300)
    def __init__(self, space='View3D'):
        self.spaces = Collection()
        self.spaces.new(space)

    def draw(self):
        self.spaces.active.draw(self)
        
    def set_space(self, space):
        self.spaces.set(space)


if __name__ == '__main__':
    a = Area()
    
    print(a.spaces)
    
    a.draw()
    
    a.set_space('Console')
    
    print(a.spaces)
    
    a.draw()
