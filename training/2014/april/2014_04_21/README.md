# About 
In this session we are going to take a look at the process of solving a problem by using Object Oriented Programming techniques using Python.

The default turtle object that we create using the turtle.Turtle class has certain behavior.

The behavior that we would like to bestow upon it is the following
By default when the turtle.Turtle object is created, it will be black in color (default)
Our turtle object will remember if it has been clicked or not
By default it is not clicked
If it was clicked, it will turn "green" else "red"

# Examples


## Example used to illustrate the difference between "input()" and "raw_input()"

The following only applies to Python 2.x. In Python 3.x, the existing functionality of ```input()``` is replaces by that of ```raw_input()``` and the latter is removed altogether. 

```python
In [1]: input("Enter something: ")
Enter something: 1+2
Out[1]: 3

In [2]: raw_input("Enter something: ")
Enter something: 1+2
Out[3]: '1+2'

In [3]: eval(raw_input('linux:~> '))
linux:~> 1+2
Out[3]: 3
```

## Example used to illustrate the concept of "self" as used in methods in a class definition

```python
In [1]: s = 'earth'

In [2]: s.capitalize()
Out[2]: 'Earth'

In [3]: type(s)
Out[3]: <type 'str'>

In [4]: str.capitalize(s)
Out[4]: 'Earth'
```


## Refer to turtleonoff_*.py

def handleClick(self, x, y)  => turtle1.handleClick(x, y) => ToggleTurtle.handleClick(turtle1, x, y)

The handleClick mrthod that we defined in ToggleTurtle class is called by the "screen" on the instance of the turtle that we clicked on. It is the "screen" that also passes the x, y coordinates to the handleClick method

# Development Environment
## Kate
* https://pypi.python.org/pypi/Kate-plugins
* http://kate-editor.org/2012/06/26/python-plugin-user-guide/
