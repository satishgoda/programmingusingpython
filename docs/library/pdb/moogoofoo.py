#!/usr/bin/python

def moo():
    moo.count = 0

def goo():
    foo()

def foo():
    moo()

goo()
