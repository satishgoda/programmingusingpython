
class Viz:
    class String:
        def __init__(self, string):
            self._str = string
        def __repr__(self):
            string = self._str
            row1 = []
            row2 = []
            fmt = "{:%d} {}" % (len(str(len(string))))
            for index, char in enumerate(string):
                i2s = str(index)
                width = len(i2s)
                row1.append(char+' '*(width-1))
                row2.append(i2s)
            return ' '.join(row1) + '\n' + ' '.join(row2)


if __name__ == '__main__':
    print()
    
    vstr1 = Viz.String('When the going gets tough.')
    print(vstr1)
    
    print()
    
    vstr2 = Viz.String('Python.')
    print(vstr2)
