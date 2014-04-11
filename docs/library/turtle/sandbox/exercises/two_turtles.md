```python
>>> from turtle import *

>>> setup(600, 600)

>>> home()

>>> turtles()                                                                                        
[<turtle.Turtle object at 0x18d9d50>] 

>>> t0 = turtles()[0]

>>> t0
<turtle.Turtle object at 0x18d9d50>

>>> t0.                                 
Display all 155 possibilities? (y or n) 
t0.DEFAULT_ANGLEOFFSET  t0._goto(               t0.currentLine          t0.radians(
t0.DEFAULT_ANGLEORIENT  t0._hidden_from_screen  t0.currentLineItem      t0.reset(  
t0.DEFAULT_MODE         t0._mode                t0.degrees(             t0.resizemode(
t0.START_ORIENTATION    t0._newLine(            t0.distance(            t0.right(     
t0.__class__(           t0._orient              t0.dot(                 t0.rt(        
t0.__delattr__(         t0._outlinewidth        t0.down(                t0.screen     
t0.__dict__             t0._pen                 t0.drawingLineItem      t0.screens    
t0.__doc__              t0._pencolor            t0.end_fill(            t0.seth(      
t0.__format__(          t0._pensize             t0.end_poly(            t0.setheading(
t0.__getattribute__(    t0._poly                t0.fd(                  t0.setpos(    
t0.__hash__(            t0._polytrafo(          t0.fill(                t0.setposition(
t0.__init__(            t0._position            t0.fillcolor(           t0.settiltangle(
t0.__module__           t0._reset(              t0.forward(             t0.setundobuffer(
t0.__new__(             t0._resizemode          t0.get_poly(            t0.setx(         
t0.__reduce__(          t0._rotate(             t0.getpen(              t0.sety(         
t0.__reduce_ex__(       t0._screen              t0.getscreen(           t0.shape(        
t0.__repr__(            t0._setDegreesPerAU(    t0.getturtle(           t0.shapesize(    
t0.__setattr__(         t0._setmode(            t0.goto(                t0.showturtle(   
t0.__sizeof__(          t0._shown               t0.heading(             t0.speed(        
t0.__str__(             t0._speed               t0.hideturtle(          t0.st(           
t0.__subclasshook__(    t0._stretchfactor       t0.home(                t0.stamp(        
t0.__weakref__          t0._tilt                t0.ht(                  t0.stampItems    
t0._angleOffset         t0._undo(               t0.isdown(              t0.tilt(         
t0._angleOrient         t0._undobuffersize      t0.isvisible(           t0.tiltangle(    
t0._cc(                 t0._undogoto(           t0.items                t0.towards(      
t0._clear(              t0._update(             t0.left(                t0.tracer(       
t0._clearstamp(         t0._update_data(        t0.lt(                  t0.turtle        
t0._color(              t0._write(              t0.onclick(             t0.turtlesize(   
t0._colorstr(           t0.back(                t0.ondrag(              t0.undo(         
t0._creatingPoly        t0.backward(            t0.onrelease(           t0.undobuffer
t0._degreesPerAU        t0.begin_fill(          t0.pd(                  t0.undobufferentries(
t0._delay(              t0.begin_poly(          t0.pen(                 t0.up(
t0._drawing             t0.bk(                  t0.pencolor(            t0.width(
t0._drawturtle(         t0.circle(              t0.pendown(             t0.window_height(
t0._fillcolor           t0.clear(               t0.pensize(             t0.window_width(
t0._fillitem            t0.clearstamp(          t0.penup(               t0.write(
t0._fillpath            t0.clearstamps(         t0.pos(                 t0.xcor(
t0._fullcircle          t0.clone(               t0.position(            t0.ycor(
t0._go(                 t0.color(               t0.pu(

>>> t0.shape()
'classic'

>>> t0.shape('circle')

>>> t1 = t0.clone()

>>> t1.shape()
'circle'

>>> t1.shape('classic')

>>> t1.forward(100)
>>> t0.backward(100)

>>> t1.color()
('black', 'black')

>>> t1.color('red')

>>> t0.color('green')


>>> t0.color()
('green', 'green')

>>> t1.color()
('red', 'red')

```
