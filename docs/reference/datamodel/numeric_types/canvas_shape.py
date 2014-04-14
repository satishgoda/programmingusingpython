class Canvas(object):
    def __init__(self):
        self.shapes = []

    def __add__(self, shape):
        self.shapes.append(shape)

    def __radd__(self, shape):
        self.shapes.append(shape)


class Shape(object):             
    pass


if __name__ == '__main__':
    c = Canvas()
    
    s = Shape()
    s.name = 'square'
    s.size = 2
    
    c + s
    
    s = Shape()
    s.name = 'circle'
    s.size = 2
    
    s + c
    
    for shape in c.shapes:
        print("{0} {1}".format(shape.name, shape.size))
