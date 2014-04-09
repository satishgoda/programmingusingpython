#!/usr/bin/env python

from turtle import *

from time import sleep


class Action:
  action_list = []
  
  def __call__(self):
    for action in self.action_list:
      action()


def close(x, y):
    import sys
    sys.exit(0)


if __name__ == '__main__':
    clearhome = Action()
    clearhome.action_list = [clear, home]
    
    homeclear = Action()
    homeclear.action_list = [home, clear]
    
    setup(600, 600)
    onclick(close)
    
    homeclear()
    
    forward(100)
    
    sleep(2)
    
    clearhome()
    
    sleep(2)
    
    left(90)
    forward(100)
    
    sleep(2)
    
    homeclear()

    input()

