class AppClass(object):
    def __init__(self, name):
        self.name = name

class GraphNodeAttrs(object):
    def __getattr__(self, attr):
        return self.__dict__.get(attr)
    
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
    
class GraphNode(object):
    def __init__(self, data, graph):
        self.data = data
        self.graph = graph
    
    @property
    def name(self):
        return self.data.name

    @property
    def attrs(self):
        return self.graph.node[self]
    
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value

class Graph(object):
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node):
        self.nodes[node] = GraphNodeAttrs()
        node.attrs.label = node.name
    
    @property
    def node(self):
        return self.nodes

a1 = AppClass('Apple')
a2 = AppClass('Ball')

dg = Graph()

a1gn = GraphNode(a1, dg)
a2gn = GraphNode(a2, dg)

dg.add_node(a1gn)
dg.add_node(a2gn)

a1gn.attrs.style = 'filled'

print a2gn.attrs.label

