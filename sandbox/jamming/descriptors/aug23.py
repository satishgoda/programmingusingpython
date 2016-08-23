def printPrimitive(appentity, attribute, collect):
    attr = getattr(appentity, attribute.name)
    collect[attr.name] = (attr.path, attr.value)


def printAttributes(appentity, collect):
    for attribute in appentity.attributes:
        if isinstance(attribute, AttributeDefinition):
            printPrimitive(appentity, attribute, collect)
        else:
            group = collect[attribute.name] = dict()
            attrgrp = getattr(appentity, attribute.name)
            printAttributes(attrgrp, group)
    return result


result = dict()
collect = result[item1.name] = dict()
printAttributes(item1, collect)

pprint(result, indent=1)

item2 = Item("item2")

item2.display.link.source.value = 100
item2.display.link.destination.value = 50
item2.display.shape.value = 'ellipse'

result = dict()
collect = result[item2.name] = dict()
printAttributes(item2, collect)

pprint(result, indent=1)


"""
{'item1': {'display': {'color': ('/items/item1.display.color', 'red'),
                       'link': {'destination': ('/items/item1.display.link.destination',
                                                1),
                                'source': ('/items/item1.display.link.source',
                                           0)},
                       'shape': ('/items/item1.display.shape', 'circle')},
           'id': ('/items/item1.id', 345)}}

{'item2': {'display': {'color': ('/items/item2.display.color', 'grey'),
                       'link': {'destination': ('/items/item2.display.link.destination',
                                                50),
                                'source': ('/items/item2.display.link.source',
                                           100)},
                       'shape': ('/items/item2.display.shape', 'ellipse')},
           'id': ('/items/item2.id', 345)}}

"""
