import networkx as nx

from collections import namedtuple

DiagramType = namedtuple("DiagramType", "Step Conditional StartEnd Io")._make(range(4))
# DiagramType._fields[item.diagramType]
# DiagramType._asdict()[DiagramType._fields[item.diagramType]]

def build_dg(dg, items):

    def set_node_attrs(dg, item):
        node = dg.node[item]
        node['name'] = item.name
        node['pos'] = item.pos().toTuple()
        node['diagramType'] = item.diagramType

    for item in items:
        if isinstance(item, Arrow):
            si = item.myStartItem
            ei = item.myEndItem        
            dg.add_edge(si, ei)
            set_node_attrs(dg, si)
            set_node_attrs(dg, ei)
        elif isinstance(item, DiagramItem):
            print DiagramType._fields[item.diagramType]
            if not item in dg.node:
                dg.add_node(item)
                set_node_attrs(dg, item)
        else:
            pass

##

def dump_dg(dg):
    for item, data in dg.node.iteritems():
        print data['name'], data['pos']
        for ei in dg.edge[item]:
            print "\t", dg.node[ei]['name'],
        print

##

item_index = dict()

scene_to_serialize = dict()
sitems = scene_to_serialize['items'] = []
sarrows = scene_to_serialize['arrows'] = []

for index, (item, data) in enumerate(dg.node.iteritems(), 1):
    item_index[item] = index
    sitems.append(data)
    
for sitem in dg.node:
    sindex = item_index[sitem]
    for eitem in dg.edge[sitem]:
        eindex = item_index[eitem]
        sarrows.append((sindex, eindex))


import json
fil = open("F:\\diagramscene.json", mode='w')
json.dump(scene_to_serialize, fil)
fil.close()

##

items = scene.items()

dg = nx.DiGraph()

build_dg(dg, items)

dump_dg(dg)

##

{'arrows': [(1, 7), (2, 6), (3, 7), (4, 1), (5, 1), (5, 6), (6, 3)],
 'items': [{'name': u'Render2', 'pos': (3224.0, 2614.0)},
  {'name': u'Sim1', 'pos': (2242.0, 2240.0)},
  {'name': u'Render1', 'pos': (2482.0, 2872.0)},
  {'name': u'Sim3', 'pos': (3288.0, 2254.0)},
  {'name': u'Sim2', 'pos': (2734.0, 2238.0)},
  {'name': u'Merge1', 'pos': (2476.0, 2592.0)},
  {'name': u'Farm', 'pos': (2906.0, 3098.0)}]}
