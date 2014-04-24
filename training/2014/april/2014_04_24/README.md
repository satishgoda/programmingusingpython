```python
%history
%history -r
%history 


%history -r
%save?
%save -r foo
ls
!kwrite foo.py



pwd






set


l = [1, 2, 4, 6]
l1 = [1, 2, 4, 6]
l2 = [1, 2, 4, 6]
l2 = [1, 3, 4, 6]
l2 = [1, 3, 4, 7]

l1
l2

l2 = [1, 3, 4, 6, 1, 6]
l1 = [1, 2, 4, 6, 2, 4]

l1
l2


s1 = set(l1)
s1
s2 = set(l2)

s2
set.difference(s1, s2)
set.difference(s2, s1)


s1 - s2
s2 - s1


s1 +  s2
s1 | s2
s1 ^ s2
s1 & s2


2 in s1
10 in s2
l1

for indez, item in enumerate(l1):
    print("{0} -> {1}".format(index, item))
for index, item in enumerate(l1):
    print("{0} -> {1}".format(index, item))
l1.sort()
l1
l2
l3 = sorted(l2)
l2
l3
set(l2) - set(l3)
set(l2) ^ set(l3)

s1.difference(s2)
s2.difference(s1)
s1 - s2
s2 - s1




set("one two one three one".split())



res = set("one two one three one".split())

res[0]
l1
1 in l1
l1.index(1)
l21
l2

l2.index(1)
l2[0+1:]
l2[0+1:].index(1)


import turtle


turtle??
turtle?
turtle.Screen??
turtle.Turtle.color??
turtle.Screen??



turtle._Screen??
turtle.Turtle??






!date

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
%history -r
%history -r 10000
!date
range(11)
import array
array?
list
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




%history -r 10000
unzip
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


%history -r 10000
%save -r session8 1-212
!kwrite session8.py


%save?
%save??
%save?
bin?
bin??
import matplotlib
matplotlib?
l = 10
l
%save -r session8 1-260
```
