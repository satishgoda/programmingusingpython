import bpy
import sys
sys.path.append('/home/satishg/learning/soc/obnblender/blender/io_scene_obn')
import rhomstub as rhom
import time

class ProcessBMesh(object):
    from collections import namedtuple
    VertexIndices = namedtuple('VertexIndices', ['array', 'no'])
    prototype_VertexIndices = VertexIndices('', -1)
    
    Polygon = namedtuple('Polygon', ['index', 'vertices', 'uvlayers', 'groups'])
    prototype_Polygon = Polygon(-1, None, [], [])
    
    def __init__(self, bmesh):
        self.bmesh = bmesh
        
        # Container for processed polygons
        # @polygons will return a generator method that provides this container
        self._polygons = []
        
        # This method proprocesses bmesh and sets up all data structures
        self._preprocess()
        
    # Preprocessing Methods
    def _preprocess(self):
        for polygon in self.bmesh.polygons:
            vertexIndices = {}
            vertexIndices['array'] = str(list(polygon.vertices))
            vertexIndices['no'] = len(polygon.vertices)
            self.polygon = vertexIndices
    
    def _preprocess_group_membership(self):
        pass
    
    def _preprocess_uv_layers(self):
        pass
    
    # Properties 
    
    @property
    def vertices(self):
        for vertex in self.bmesh.vertices:
            yield vertex.co
    
    @property
    def polygons(self):
        pass
    
    @polygons.setter
    def polygons(self, value):
        self.polygons.append(Polygon(**value))
    
        
if __name__ == '__main__':
    before = time.ctime(time.time())
    
    object = bpy.context.active_object
    bmesh = object.data
    
    export_mesh = ProcessBMesh(bmesh)
    
    # Create a rhom mesh
    mesh = rhom.Mesh()
    
    # Generate the PointTable values
    for x, y, z in export_mesh.vertices:
        mesh.addPoint(rhom.Point(x, y, z))
    
    # Write the mesh to disk
    rhom.writeMesh('Foo.obn', mesh)
    
    after = time.ctime(time.time())
    
    print(before)
    print(after)
    
