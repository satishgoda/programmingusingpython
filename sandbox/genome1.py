input = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4


"""
>>> import genome
>>> 
>>> genome.input
'ACGTTGCATGTCGCATGATGCATGAGAGCT'
>>>
>>> genome.k
4
>>> 'CATG' in genome.input
True
>>>
>>> genome.input.count('CATG')
3

>>> s = 'CATG'
>>> genome.input.find(s)
6

>>> from viz_string import Viz
>>> 
>>> Viz.String(genome.input)
A C G T T G C A T G T  C  G  C  A  T  G  A  T  G  C  A  T  G  A  G  A  G  C  T 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
>>>
>>> si = genome.input.find(s)
>>> si = genome.input.find(s, si+1)
>>> si
13
>>>
>>> si = genome.input.find(s, si+1); si
20
"""
