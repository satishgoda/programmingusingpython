
class ListWithLength(list):
    def __init__(self, *args):
        super(ListWithLength, self).__init__(*args)
    
    @property
    def length(self):
        return len(self)


if __name__ == '__main__':
    
    print ListWithLength.mro()
    
    l1 = ListWithLength((1,2,3))
    
    print l1
    print l1.length
    print(len(l1))
    
    l1.append(10)
    
    print l1
    print l1.length
    print(len(l1))
    
    l1.pop()
    
    print l1
    print l1.length
    print(len(l1))
