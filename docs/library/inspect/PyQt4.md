```python

>>> from classtree import trace  
>>> from PyQt4 import QtGui


>>> trace(QtGui.QWidget)
-------------------------------------------------------------------------------
<class 'PyQt4.QtGui.QWidget'>

object()
simplewrapper(object)
QPaintDevice(simplewrapper)
wrapper(simplewrapper)
QObject(wrapper)
QWidget(QObject, QPaintDevice)


>>> trace(QtGui.QPushButton)
-------------------------------------------------------------------------------
<class 'PyQt4.QtGui.QPushButton'>

object()
simplewrapper(object)
QPaintDevice(simplewrapper)
wrapper(simplewrapper)
QObject(wrapper)
QWidget(QObject, QPaintDevice)
QAbstractButton(QWidget)
QPushButton(QAbstractButton)


>>> trace(QtGui.QVBoxLayout)
-------------------------------------------------------------------------------
<class 'PyQt4.QtGui.QVBoxLayout'>

object()
simplewrapper(object)
wrapper(simplewrapper)
QObject(wrapper)
QLayout(QObject, QLayoutItem)
QBoxLayout(QLayout)
QVBoxLayout(QBoxLayout)
QLayoutItem(wrapper)


>>> trace(QtGui.QTreeWidget)
-------------------------------------------------------------------------------
<class 'PyQt4.QtGui.QTreeWidget'>

object()
simplewrapper(object)
QPaintDevice(simplewrapper)
wrapper(simplewrapper)
QObject(wrapper)
QWidget(QObject, QPaintDevice)
QFrame(QWidget)
QAbstractScrollArea(QFrame)
QAbstractItemView(QAbstractScrollArea)
QTreeView(QAbstractItemView)
QTreeWidget(QTreeView)

```
