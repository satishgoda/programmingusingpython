import networkx as nx

nxdg = nx.DiGraph()
nxdg.add_node('a')
nxdg.add_node('b')
nxdg.nodes()
nxdg.nodes(data=True)
nxdg.node

class AppClass(object):
    def __init__(self, name):
        self.name = name

class GraphNodeAttrs(object):
    """
    Provides an simple interface to the netwrokx node 
    attributes structure
    """
    def __init__(self, noderef):
        self.__dict__['noderef'] = noderef
    
    @property
    def node(self):
        noderef = self.__dict__['noderef']
        graph = noderef.graph
        return graph.node[noderef]
    
    def __getattr__(self, attr):
        return self.node[attr]
    
    def __setattr__(self, attr, value):
        self.node[attr] = value
    
class GraphNode(object):
    def __init__(self, data, graph):
        self.data = data
        self.graph = graph
        self._attrs = GraphNodeAttrs(self)
    
    @property
    def name(self):
        return self.data.name

    @property
    def attrs(self):
        return self._attrs

class Graph(object):
    def __init__(self):
        self.graph = nx.DiGraph(name="Yeah")
    
    def add_node(self, node):
        self.graph.add_node(node)
        node.attrs.label = node.name
    
    @property
    def node(self):
        return self.graph.node

    @property
    def nodes(self):
        return self.graph.nodes(data=False)
    
a1 = AppClass('Apple')
a2 = AppClass('Ball')

dg = Graph()

a1gn = GraphNode(a1, dg)
a2gn = GraphNode(a2, dg)

print(a1gn.attrs.node)

dg.add_node(a1gn)
dg.add_node(a2gn)

print(a2gn.attrs.node)

a1gn.attrs.style = 'filled, bold'
a1gn.attrs.fillcolor = 'green'


print dg.node

print dg.nodes
