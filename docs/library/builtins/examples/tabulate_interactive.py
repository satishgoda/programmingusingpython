
def table(n, extent=10):
    tabulate = lambda n: lambda times: "{:3} x {:3} = {:4}".format(n, times, n*times)
    template = tabulate(n)
    extents = range(1, extent+1)
    return tuple(map(template, extents))


def table_inputs():
    n = input("n: ")
    extent = input("extent: ")
    return map(int,(n, extent))


def table_print(n, extent):
    result = table(n, extent)
    print("-"*30)
    print("\n".join(result))


if __name__ == '__main__':
    
    n, extent = table_inputs()
    
    table_print(n, extent)
    
    n, extent = table_inputs()
    
    table_print(n, extent)
