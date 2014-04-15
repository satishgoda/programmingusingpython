# Overview of terms and concepts covered today

> __ipython__

* ```ipython``` is an interactive Python interpreter. It enables you to query the documentation and source code for various objects in a very user-friendly manner.

* There is also a smart history mode, wherein code blocks (like for loops) can be re-edited.


# Coding Examples

## String formatting

```python
>>> "{0} {1}".format("bugs", "bunny")
"bugs bunny" 

>>> "{1} {0}".format("bugs", "bunny")
"bunny bugs"
```


## String manipulation

```python
>>> s = "   one two three   "

>>> s.strip()
"one two three"

>>> s.split()
["one", "two", "three"]

>>> words = s.split()

>>> words[0], words[2]

>>> for word in words:
...     print("Word is {0}".format(word))
...
"one"
"two"
"three"

>>> separator = ", "

>>> js = separator.join(words)

>>> js
"one, two, three"

```

## Opening and Reading Files on Disk

```python

f = open('text.txt')

lines = f.readlines()

f.close()


for line in lines:
    print line


for index, line in enumerate(lines):
    print("{0}) {1}".format(index, line))


for index, line in enumerate(lines, start=1):
    if len(line.strip()) > 0:
        print("{0}) {1}".format(index, line))


line_count = len(lines)


for index, line in enumerate(reversed(lines), start=1):
    if len(line.strip()) > 0:
        print("{0}) {1}".format(line_count - index + 1, line))
```


# Summary

* ```ipython```
* everything is an object, including ```str```, ``file```
* ```str?``` and ```str??```
* ```turtle?``` and ```turtle??```
* ```str.strip()```, ```str.split()```, ```str.join(list)```
* ```str.format```, ```"{0} {1}".format("one", "two")```
* Iterating over lists ```for-in-iterable```
* Creating a text file with some text
* Creating ```file``` object using ```open```
* ```file.?```, ```file.readlines?```
* Funcation composition f(g(h(input)))
* ```for-in-lines```, ```if len(line.strip()) > 0```
* ```enumerate``` and ```reversed```

# Checkout

* http://ipython.org
* http://pythontutor.com
* https://docs.python.org
* http://pyth0n.org

