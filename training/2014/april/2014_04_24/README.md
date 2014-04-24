# Introduction to ```set``` datatype


```python
set


l1 = [1, 2, 4, 6, 2, 4]
l2 = [1, 3, 4, 6, 1, 6]


l1
l2


s1 = set(l1)
s1
s2 = set(l2)
s2

set.difference(s1, s2)
set.difference(s2, s1)

s1.difference(s2)
s2.difference(s1)


s1 - s2
s2 - s1

set(l1) - set(l2)
set(l2) ^ set(l1)


s1 +  s2 # TypeError

s1 | s2
s1 ^ s2
s1 & s2


2 in s1
10 in s2

set("one two one three one".split())
res = set("one two one three one".split())
res[0] # Set objects do not support indexing
```

# Operations on ```list``` data types

```python
l1.sort()
l1

l2
l3 = sorted(l2)
l2
l3


l1
1 in l1

l1.index(1)

l2

l2.index(1)
l2[0+1:]
l2[0+1:].index(1)

import array
array?
```

# Operations on ```dict``` datatype

```python
env = {}

env['i']

env.get('i')
env.get('i', 'satishg')
if env.get('i'):
    print("Exists")
else:
    print("Does not exist")
None
None == False
bool(None)
env['i'] = 10


if env.get('i'):
    print("Exists")
else:
    print("Does not exist")
```

# ```functional``` programming in Python

```python
range(11)

0 % 2
4 % 2
5 % 2
numbers = range(56)


evens = [number for number in numbers if number%2 == 0]
enves
evens
odds = set(numbers) - set(evens)

odds
odds
odds = list(set(numbers) - set(evens))
odds

del evens
del odds

evens = []
for number in numbers:
    if number%2 == 0:
        evens.append(number)
evens
l1
l2
set(l1)
set(l2)
set.difference(*map(set, [l1, l2]))
s1 = set(l1)
s2 = set(l2)
s1 - s2
set.difference(map(set, [l1, l2]))
!date


l1 = [1, 2, 3]
l2 = [1, 4, 9]

zip?
zipped = zip(l1, l2)
zipped
zipped[0]
zipped[1]
zipped[2]
x = zipped[0]
x
x = zipped[0][0]
y = zipped[0][1]
x, y = zipped[0]
x
y
```

# More ```builtins``` in Python

```python
ord('A')
chr(65)
hex(16)
hex(255)
bin
bin?
bin(16)
bin(255)
int(bin(255))
int(bin(255), base=2)

int(hex(255), base=16)
```

# ```ipython``` Notebook and QtConsole

```python
import matplotlib
matplotlib?
```

# ```ipython``` tips

```python
%history
%history -r
%save?
%save -r foo 1-30
ls
!kwrite foo.py
pwd

import turtle
turtle??
turtle?
turtle.Screen??
turtle.Turtle.color??
turtle.Screen??
turtle._Screen??
turtle.Turtle??


%history -r
%history -r 10000
!date
%history -r 10000
%save -r session8 1-212
!kwrite session8.py
%save?
%save??
%save?
bin?
bin??
```

# How do i?

```python
for index, item in enumerate(l1):
    print("{0} -> {1}".format(index, item))
```
