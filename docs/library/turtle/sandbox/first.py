from turtle import *


setup(600,600)


macro = {}                                 


macro['l'] = left                          
macro['r'] = right
macro['f'] = forward
macro['b'] = backward


import random


for action in 'llrffbrlfb':
  macro[action](random.randint(0, 180))


home(); clear()


for action in 'llrffbrlfb':
  macro[action](random.randint(-45, 45))


for action in 'llrffbrlfblflflfrbbbrlf':
  macro[action](random.randint(-45, 45))


home(); clear()


def homeclear():
  home()
  clear()


homeclear()


for action in 'fblfb':
  macro[action](45)


homeclear()


for action in 'fblfb':
  macro[action](90)


def homeclear():
  actions = getattr(homeclear, 'actions', None)
  if actions:
    for action in actions:
      action()
  else:
    home()
    clear()


homeclear.actions = [clear, home]


homeclear()


for action in 'fblfb':
  macro[action](90)


homeclear()


del homeclear.actions


del homeclear
