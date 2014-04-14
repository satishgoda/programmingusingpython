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

```
