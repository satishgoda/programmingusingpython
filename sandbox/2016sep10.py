def build_dg(dg, items):

    def set_node_attrs(dg, item):
        node = dg.node[item]
        node['name'] = item.name
        node['pos'] = item.pos().toTuple()

    for item in items:
        if isinstance(item, Arrow):
            si = item.myStartItem
            ei = item.myEndItem        
            dg.add_edge(si, ei)
            set_node_attrs(dg, si)
            set_node_attrs(dg, ei)
        elif isinstance(item, DiagramItem):
            if not item in dg.node:
                dg.add_node(item)
                set_node_attrs(dg, item)
        else:
            pass

def dump_dg(dg):
    for item, data in dg.node.iteritems():
        print data['name']
        for ei in dg.edge[item]:
            print "\t", dg.node[ei]['name'],
        print
