
tabulate = lambda n: lambda times: "{:3} x {:3} = {:4}".format(n, times, n*times)

template = tabulate(20)
extents = range(1, 21)

print("\n".join(map(template, extents)))


"""
20 x  1 =   20
20 x  2 =   40
20 x  3 =   60
20 x  4 =   80
20 x  5 =  100
20 x  6 =  120
20 x  7 =  140
20 x  8 =  160
20 x  9 =  180
20 x 10 =  200
20 x 11 =  220
20 x 12 =  240
20 x 13 =  260
20 x 14 =  280
20 x 15 =  300
20 x 16 =  320
20 x 17 =  340
20 x 18 =  360
20 x 19 =  380
20 x 20 =  400
"""
