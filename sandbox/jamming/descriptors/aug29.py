id = 1
idMap = OrderedDict()

def getId(item):
    global id
    global idMap
    
    if item not in idMap:
        print "adding"
        idMap[item] = id
        id += 1
    else:
        print "exists"
    
    return idMap[item]

for item in scene.items():
    iid = getId(item)
    itemType = item.__class__.__name__
    pos = item.pos()
    print itemType, iid, pos.x(), pos.y()
    if isinstance(item, Arrow):
        print '\t\t', getId(item.myStartItem)
        print '\t\t', getId(item.myEndItem)

##
    
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
    id = IntAttributeDefinition()
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

serialized = printAttributes(item1, OrderedDict())

print serialized

item2 = Item("item2")

print printAttributes(item2, {})

itemClass = serialized.pop('itemClass')

item2.itemClass.value = itemClass

##

for attrName, data in serialized.iteritems():
    attr = getattr(item2, attrName)
    if isinstance(attr, AttributesGroupDefinition):
        print attr
        for attrName, value in data.iteritems():
            gattr = getattr(attr, attrName)
            gattr.value = value
    else:
        attr.value = data

##

print printAttributes(item2, {})

print printAttributes(item1, {})

##

# sitem = gscene.selectedItems()[0]
# titem = DiagramTextItem(sitem, gscene)
# titem.setPlainText('Sim1')
# tfont = titem.font()
# tfont.setPointSize(18)
# titem.setFont(tfont)

def parentTextItem(scene, item, text='Text'):
    titem = DiagramTextItem(item, scene)
    titem.setPlainText(text)
    tfont = titem.font()
    tfont.setPointSize(18)
    titem.setFont(tfont)

## 

sitem = gscene.selectedItems()[0]

sitem.childItems()
sitem.parentItem()
