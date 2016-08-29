for item in scene.items():
    itemType = item.__class__.__name__
    pos = item.pos()
    print itemType, pos.x(), pos.y()
    print '\t', hex(id(item))
    if isinstance(item, Arrow):
        print '\t\t', hex(id(item.myStartItem))
        print '\t\t', hex(id(item.myEndItem))

item.transform()
item.type()
type(item)
isinstance(item, Arrow)

pos = item.pos()
pos.x(), pos.y()


##

class ItemPos(AttributesGroupDefinition):
    x = FloatAttributeDefinition(0.0, min=-10000.0, max=1000000.0)
    y = FloatAttributeDefinition(0.0, min=-10000.0, max=10000000.0)

class Item(AppObjectBase):
    itemClass = StringAttributeDefinition()
    itemPos = ItemPos()
    
    @property
    def optype(self):
        return '/items'
    
##

item1 = Item('item1')
item1.itemClass.value = item.__class__.__name__
item1.itemPos.x.value = -100.0 #pos.x()
item1.itemPos.y.value = 300.0 # pos.y()

##

serialized = printAttributes(item1, {})

print serialized

##

item2 = Item("item2")

print printAttributes(item2, {})

##

itemClass = serialized.pop('itemClass')

item2.itemClass.value = itemClass[1]

##

for attrName, data in serialized.iteritems():
    attr = getattr(item2, attrName)
    if isinstance(attr, AttributesGroupDefinition):
        print attr
        for attrName, data in data.iteritems():
            gattr = getattr(attr, attrName)
            gattr.value = data[1]
    else:
        path, value = data
        print attr, path, value

##

print printAttributes(item2, {})

print printAttributes(item1, {})
