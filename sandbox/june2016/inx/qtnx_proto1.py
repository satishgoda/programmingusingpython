import networkx as nx

from PySide import QtGui
from PySide import QtCore

## 

nxdg = nx.DiGraph()

nxdg.add_node('A')
nxdg.add_node('B')
nxdg.add_node('C')
nxdg.add_node('D')
nxdg.add_node('E')
nxdg.add_node('F')

nxdg.add_edge('A', 'E')
nxdg.add_edge('A', 'C')
nxdg.add_edge('D', 'B')
nxdg.add_edge('B', 'F')

## 

scene = QtGui.QGraphicsScene()

view = QtGui.QGraphicsView(scene)

view.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

view.show()

## 
#
# nxdg_l = nx.layout.circular_layout(nxdg, dim=2, scale=50)
# nxdg_l = nx.layout.fruchterman_reingold_layout(nxdg, dim=2, center=[0,0], scale=100)

nxdg_l = nx.layout.spring_layout(nxdg, dim=2, center=[0,0], scale=100)

for node_l, pos in nxdg_l.iteritems():
    x, y = pos
    rect = scene.addRect(0, 0, 20, 20)
    rect.setToolTip(node_l)
    text = scene.addText(node_l)
    text.setPos(x, y)
    rect.setParentItem(text)

## 
# nxdg_l = nx.layout.circular_layout(nxdg, dim=2, scale=100)
# nxdg_l = nx.layout.fruchterman_reingold_layout(nxdg, dim=2, center=[0,0], iterations=300, scale=150)

nxdg_l = nx.layout.spring_layout(nxdg, dim=2, center=[0,0], scale=150)
    
for item in scene.items():
    if isinstance(item, QtGui.QGraphicsTextItem):
        text = item.toPlainText()
        x, y = nxdg_l[text]
        item.setPos(x, y)
