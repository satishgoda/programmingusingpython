In [1]: l1 = [1, 2, 3]

In [2]: hex(id(l1))
Out[2]: '0x1d01098'

In [3]: 

In [4]: l2 = l1

In [5]: 

In [6]: hex(id(l2))
Out[6]: '0x1d01098'

In [7]:

In [8]: l1 is l2
Out[8]: True

In [9]:

In [10]: l1 == l2
Out[10]: True

In [11]:

In [12]: l1[2] = 30

In [13]: l1
Out[13]: [1, 2, 30]

In [14]: l2
Out[14]: [1, 2, 30]


In [16]: l3 = l2[:]

In [17]: l3 is l2
Out[17]: False

In [18]: l2 is l1
Out[18]: True

In [19]: l2[:] = [100, 200, 300]

In [20]:

In [21]: l2
Out[21]: [100, 200, 300]

In [22]: l1
Out[22]: [100, 200, 300]

In [23]: l3
Out[23]: [1, 2, 30]

In [24]: hex(id(l2))
Out[24]: '0x1d01098'

In [25]: hex(id(l1))
Out[25]: '0x1d01098'
