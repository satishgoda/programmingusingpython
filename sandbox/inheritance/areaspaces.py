
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


class Area(object):
    dimensions = (400, 300)
    def __init__(self, space='View3D'):
        self.spaces = {}
        self._create_set_space(space)
        
    def _create_set_space(self, space):
        self._create_space(space)
        self._set_active_space(space)
    
    def _create_space(self, space):
        self.spaces[space] = eval(space)()

    def _set_active_space(self, space):
        self.active_space = self.spaces[space]
    
    def draw(self):
        self.active_space.draw(self)
        
    def set_space(self, space):
        if space in self.spaces:
            self._set_active_space(space)
        else:
            self._create_set_space(space)

            
if __name__ == '__main__':
    a = Area()
    
    print(a.spaces)
    
    a.draw()
    
    a.set_space('Console')
    
    print(a.active_space)
    
    print(a.spaces)
    
    a.draw()
