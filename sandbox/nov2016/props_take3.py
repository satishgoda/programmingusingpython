propTypeDefn = {
    int: ('value', 'minValue', 'maxValue'),
    float: ('value', 'minValue', 'maxValue'),
    str: ('value', )
}

def intPropPrint(value, minValue, maxValue):
    print "{0} <= {1} <= {2}".format(minValue, value, maxValue)

def floatPropPrint(value, minValue, maxValue):
    print "{0} <= {1} <= {2}".format(minValue, value, maxValue)

def strPropPrint(value):
    print "{0}".format(value)

propTypePrint = {
    int: intPropPrint,
    float: floatPropPrint,
    str: strPropPrint
}

props = dict((
            ('a', (int, 'An integral A', 1, -1, 1)), 
            ('b', (float, "It's a floating B", 0.5, -5.0, 5.0)),
            ('c', (str, "I am a C string", 'Object 1'))
        ))

for propName in props:
    propType, description = props[propName][:2]
    propDefn = propTypeDefn[propType]
    attrs = props[propName][2:(2+len(propDefn))]
    propTypePrint[propType](*attrs)

##

#[1,2,3,4,5][:2]
#[1,2,3,4,5][2:5]

# print propName, propType
# print "{0} <= {1} <= {2}".format(minValue, value, maxValue)
