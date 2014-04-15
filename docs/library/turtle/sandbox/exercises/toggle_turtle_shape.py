#!/usr/bin/env python

from turtle import *


class MyTurtle(Turtle):
    def __init__(self, *args, **kwargs):
        super(MyTurtle, self).__init__(*args, **kwargs)
        self.onclick(self.cb_switch_shapes)
        
    def cb_switch_shapes(self, x, y):
        shapes = self.screen.getshapes()
        shapes_count = len(shapes)

        shape_current_index = shapes.index(self.shape())
        shape_next_index = (shape_current_index + 1)%shapes_count
        shape_next = shapes[shape_next_index]

        if  shape_next == 'blank':
            shape_next_index = (shape_next_index + 1)%shapes_count
            shape_next = shapes[shape_next_index]
            
        self.shape(shape_next)


if __name__ == '__main__':
    screen = Screen()
    screen.setup(400, 400)
    
    turtle = MyTurtle('triangle')
    
    try:
        input("Press any key to exit program")
    except:
        pass
