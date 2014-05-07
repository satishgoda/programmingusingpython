print("Importing rhom.mesh stub module")

from inspect import stack

# Classes, Functions, Data exported by this package
__all__ = [
    'Mesh',
]

class Mesh(object):
    '''A stub class implementing the interface provided by rhom.mesh.Mesh'''

    def __init__(self):
        '''Initializes an empty mesh'''
        self.points = 0

        # The following list will contain all the rhom commands that are executed
        # by the exporter operator
        self.commands = []

        # We start populating the commands list with
        ##  shebang
        ##  rhom import
        ##  Creating mesh
        self._command = '#/usr/bin/python'
        self._command = 'import rhom'
        self._command = 'mesh = rhom.Mesh()'

    @property
    def _command(self):
        #import inspect
        #import pprint
        #pprint.pprint(inspect.stack())
        raise Exception('Cannot be read.. Only to be written to')

    @_command.setter
    def _command(self, pycommand):
        '''is called when a new rhom command is assigned'''
        self.commands.append(pycommand)

    def _methodName(self):
        '''Dynamically generate the method call signature using introspection'''
        classInstanceName = self.__class__.__name__.lower()
        callerName = stack()[1][3]
        return '.'.join([classInstanceName, callerName])

    def addPoint(self, point):
        '''Add a point (of type rml.geom.Point3) to the Mesh'''
        self._command = '{method}({args})'.format(method=self._methodName(), args=point)
        self.points += 1

    def addTexCoord(self, uvtag, texcoord):
        '''Add a uv point (of type rml.geom.Point2) to the Mesh'''
        self._command = 'mesh.addTexCoord("{0}", {1})'.format(uvtag, texcoord)

    def addGroup(self, name):
        '''Add an empty group to the mesh'''
        self._command = 'mesh.addGroup("{0}")'.format(name)

        # TODO: Could be controlled by an exporter operator property.
        if name.endswith('Mtl'):
            self.addMaterial(name)

    def addMaterial(self, name):
        '''Add an empty material group to the mesh'''
        self._command = 'mesh.addMaterial("{0}")'.format('xxx_' + name)

    def addElement(self, point_count):
        '''Add an element to the mesh'''
        # TODO: Factor different element types (point, line, face)
        self._command = 'element = mesh.addElement({0})'.format(point_count)

    def setPointIndices(self, element, indices):
        self._command = 'mesh.setPointIndices(element, {0})'.format(indices)

    def setTexCoordIndices(self, uvtag, element, indices):
        self._command = 'mesh.setTexCoordIndices("{0}", element, {1})'.format(uvtag, indices)

    def getElement(self, index):
        return 'mesh.getElement({0})'.format(index)

    def addElementToGroup(self, element, group_name):
        self._command = 'mesh.addElementToGroup({0}, "{1}")'.format(element, group_name)

    def setMaterial(self, element, material_name):
        self._command = 'mesh.setMaterial({0}, "{1}")'.format(element, material_name)

    def hasPoints(self):
        return self.points > 0

