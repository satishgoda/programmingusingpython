import networkx as nx

from PySide import QtGui
from PySide import QtCore

## Directed Graph

nxdg = nx.DiGraph()

nxdg.add_node('Int1')
nxdg.add_node('Int2')
nxdg.add_node('Add1')
nxdg.add_node('Add2')
nxdg.add_node('Sub1')
nxdg.add_node('Mul1')
nxdg.add_node('Div1')

nxdg.add_edge('Int1', 'Add1')
nxdg.add_edge('Int1', 'Add2')
nxdg.add_edge('Int2', 'Add2')
nxdg.add_edge('Add1', 'Sub1')
nxdg.add_edge('Int1', 'Sub1')
nxdg.add_edge('Add2', 'Mul1')
nxdg.add_edge('Sub1', 'Div1')
nxdg.add_edge('Mul1', 'Div1')

## Graphics scene and view

scene = QtGui.QGraphicsScene()

view = QtGui.QGraphicsView(scene)

view.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

view.show()

view.setMinimumSize(500, 500)

## Layout nodes

nxdg_l = nx.drawing.nx_pydot.pydot_layout(nxdg, prog='dot')

## Draw edges

for fromNode in nxdg.nodes():
    toNodes = nxdg.edge[fromNode]
    
    if not toNodes:
        continue
    
    x1, y1 = nxdg_l[fromNode]
    
    for toNode in toNodes:
        x2, y2 = nxdg_l[toNode]
        pen = QtGui.QPen()
        pen.setWidth(2)
        line = scene.addLine(x1+10, -y1+20, x2+10, -y2, pen)
        line.setToolTip("{0} -> {1}".format(fromNode, toNode))

## Draw nodes

for node_l, pos in nxdg_l.iteritems():
    x, y = pos
    y = -1*y
    rect = scene.addRect(0, 0, 20, 20)
    rect.setToolTip(node_l)
    text = scene.addText(node_l)
    text.setPos(x, y)
    rect.setParentItem(text)
