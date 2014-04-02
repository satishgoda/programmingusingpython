inp = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'


fmt = "{:%d} {}" % (len(str(len(input))))

for index, char in enumerate(input):
    print(fmt.format(index, char))

