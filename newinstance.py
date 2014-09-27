"""
"""

"""
In this interactive tutorial we are going to take a look at the process of the
creation of an instance object by calling an user-defined class.
"""

"""
We will be running the sample program via the ipython interpreter and in a
debugging mode.

class WoD(object):
    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls)
        self.created  = True
        return self

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    class WoD(object):
    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls)
        self.created  = True
        return self

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    a = WoD('bugs', 100)

Save the above piece of code in a file called newinstance.py
""" 

In[3]: run -d newinstance.py
Breakpoint 1 at /home/nerd/learnpython/concepts/newinstance.py:1
NOTE: Enter 'c' at the ipdb>  prompt to continue execution.
> /home/nerd/learnpython/concepts/newinstance.py(1)<module>()
1---> 1 class WoD(object):
      2     def __new__(cls, *args, **kwargs):
      3         self = object.__new__(cls)

"""
We will setup a breakpoint where we create an instance of class WoD

a = WoD('bugs', 100)

In my case, it happens to be on line 12, so we break the debugger at that line.
"""

ipdb> >? break 12
Breakpoint 2 at /home/nerd/learnpython/concepts/newinstance.py:12

"""
Type the 'continue' debugger command so that Python can start interpreting the class definition
and create the class object WoD so that we can call it to create instance objects.

Remember that in Python classes are objects instantiated from a metaclass.
"""

ipdb> >? continue
> /home/nerd/learnpython/concepts/newinstance.py(1)WoD()
1---> 1 class WoD(object):
      2     def __new__(cls, *args, **kwargs):
      3         self = object.__new__(cls)

"""
With the WoD class object in place (breakpoint 1), we can continue to the breakpoint that we set.
"""

ipdb> >? continue
> /home/nerd/learnpython/concepts/newinstance.py(12)<module>()
     10 
     11 if __name__ == '__main__':
2--> 12     a = WoD('bugs', 100)

"""
So the debugger stopped at line 12 and since we want to trace the birth of an instance of class
WoD, we must "step" into the breakpoint.
"""

ipdb> >? step
--Call-- """A METHOD CALL"""
> /home/nerd/learnpython/concepts/newinstance.py(2)__new__()
1     1 class WoD(object):
----> 2     def __new__(cls, *args, **kwargs):
      3         self = object.__new__(cls)

"""
So, you will notice that stepping into WoD('bugs', 100) directed the debugger into the
WoD.__new__ @classmethod. What actually happened is the following

a = WoD('bugs', 100)
    WoD.__class__.__call__(WoD, 'bugs', 100)
        self = object.__new__(WoD)
            self = WoD.__class__.__bases__[0].__new__(WoD)
        self.__init__('bugs', 100)
        return self
a = self
"""

"""
Before stepping into the __new__ classmethod, let us inspect the actual arguments that were passed.

Type and execute the "args" pdb debugger command.
"""
ipdb> >? args
cls = <class '__main__.WoD'>
args = ('bugs', 100)
kwargs = {}
"""
You can now be assured that the actual arguments are the arguments that were passed on line 12

a = WoD('bugs', 100)

The cls argument is inserted by the Python interpreter from within __call__
"""

"""
Let the debugger execute the statements inside the __new__ classmethod.

Type 'next' and press enter so that we can get ready to execute first statement.
"""
ipdb> >? next
> /home/nerd/learnpython/concepts/newinstance.py(3)__new__()
      2     def __new__(cls, *args, **kwargs):
----> 3         self = object.__new__(cls)
      4         self.created  = True
"""
We must first create an instance of the WoD class (cls).

All memory for instances is allocated by the __new__ classmethod that is implemented by the mother class,
called 'object'.
"""

"""
Type 'next' and press enter again to create the instance.
"""
ipdb> >? next
> /home/nerd/learnpython/concepts/newinstance.py(4)__new__()
      3         self = object.__new__(cls)
----> 4         self.created  = True
      5         return self

"""
Inspect the value of 'self' instance variable by just typing the name of the instance.
"""
ipdb> >? self
<__main__.WoD object at 0x02D4DC70>
"""
You can also type the following pdb debugger command and pass any program variable name

p self
"""

"""
Classes are abstractions over data and operations, and instances are created by their corresponding
classes. Instances carry the state around as instance variables. Instance variables are stored as a
dictionary in Python.

You can inspect the instance variables by using the 'vars' Python builtin function.
"""
ipdb> >? vars(self)
{}
"""
Since we have not initialized the instance (__init__ method of WoD class), the dictionary looks empty.
"""

"""
But, in reality the 'self' instance of class WoD has instance variables. These instance variables were
added by the base class of WoD class, the mother class 'object'

You can always get a list of all instance variables by using the 'dir' Python builtin function.
"""
ipdb> >? dir(self)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
 '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__']
"""
You can also directly access the __dict__ instance variable to print the instance dictionary

TODO: Since the instance dictionary could potentially contain.. pretty printing pdb debugger command

p self.__dict__
"""

"""
Let us now execute the next statement in the __new__ classmethod and attach an instance variable called
'created'
"""
ipdb> >? next
> /home/nerd/learnpython/concepts/newinstance.py(5)__new__()
      4         self.created  = True
----> 5         return self
      6 

"""
Check out the instance variable's dictionary
"""
ipdb> >? vars(self)
{'created': True}

"""
And create a directory listing of all the instance variables, including the instance variables inherited from
the base class 'object'
"""
ipdb> >? dir(self)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
'__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', 'created']
"""
You will notice the 'created' instance variable as well!
"""


"""
Type 'next' to return from the __new__ classmethod
"""
ipdb> >? next
--Return--
<__main_...02D4DC70>
> /home/nerd/learnpython/concepts/newinstance.py(5)__new__()
      4         self.created  = True
----> 5         return self
      6
"""
Notice the return value of the __new__ classmethod

<__main_...02D4DC70>

The newly created instance of class WoD.
"""


"""
Now, the Python machinery will invoke the initialization method on the instance.

That is, the __init__ method is called with the arguments that were passed to __call__ method of class object
WoD.
"""
ipdb> >? next
--Call--
> /home/nerd/learnpython/concepts/newinstance.py(7)__init__()
      6 
----> 7     def __init__(self, name, age):
      8         self.name = name

"""
Inspect the arguments passed to the __init__ method call
"""
ipdb> >? args
self = <__main__.WoD object at 0x02D4DC70>
name = bugs
age = 100

"""
Start executing the instance variable creation and initialization statements inside __init__ method
"""
ipdb> >? next
> /home/nerd/learnpython/concepts/newinstance.py(8)__init__()
      7     def __init__(self, name, age):
----> 8         self.name = name
      9         self.age = age
"""
Exercise: List the instance variables

p ????(self)
"""

ipdb> >? next
> /home/nerd/learnpython/concepts/newinstance.py(9)__init__()
      8         self.name = name
----> 9         self.age = age
     10

"""
Check the instance variables on 'self'
"""
ipdb> >? vars(self)
{'name': 'bugs', 'created': True}

ipdb> >? next
--Return--
None
> /home/nerd/learnpython/concepts/newinstance.py(9)__init__()
      8         self.name = name
----> 9         self.age = age
     10 

ipdb> >? next
--Return--
None
> /home/nerd/learnpython/concepts/newinstance.py(12)<module>()
     10 
     11 if __name__ == '__main__':
2--> 12     a = WoD('bugs', 100)