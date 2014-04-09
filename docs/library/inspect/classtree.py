#!/usr/bin/env python


from inspect import getmro, getclasstree
from pprint import pprint
import turtle

mro = getmro(turtle.Turtle)

tree = getclasstree(mro, unique=1)

pprint(tree)
