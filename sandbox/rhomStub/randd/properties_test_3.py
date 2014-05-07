import sys
sys.path.append('/home/satishg/learning/soc/obnblender/blender/io_scene_obn')

import rhomstub as rhom
import bpy
from collections import namedtuple

# The following datatypes are used to store Processed Data
Groups = namedtuple('Groups', 'names')

UVLayers = namedtuple('UVLayers', ['tag', 'table', 'uvindex'])

# The following datatypes are used to store Data about Polygons

PolygonVertices = namedtuple('PolygonVertices', ['no', 'indices'])
prototype_PolygonVertices = PolygonVertices(no=-1, indices=None)

PolygonUVs = namedtuple('PolygonUVs', ['tag', 'indices'])
prototype_PolygonUVs = PolygonUVs(tag=None, indices=None)

Polygon = namedtuple('Polygon', ['index', 'vertices', 'groups', 'uvlayers'])
prototype_Polygon = Polygon(index=-1, vertices=None, groups=None, uvlayers=None)
    
###############################################################################
class ExportMesh(object): 
    def __init__(self, bmesh):
        self.bmesh = bmesh
        
        self._uvlayers  = []
        self._groups = Groups(names=[])
        self._polygons = []
        
        self._process()
        
        # We do not need this anymore
        del self._vertexUVmapping

    def _isPolygonInGroup(self, polygon, group):
        return self.bmesh.polygon_layers_int[group].data[polygon.index].value == 1

    def _process(self):
        # Temporary storage to remove duplicate storage of shared uv's   
        self._vertexUVmapping = { v.index: { 
                            uvlayer.name: {} for uvlayer in self.bmesh.uv_layers } 
                            for v in self.bmesh.vertices 
                          }
        
        #list of groups assigned by user using Set Editor
        for group in sorted(self.bmesh.polygon_layers_int.keys()):
            self.groups = group

        for layer in self.bmesh.uv_layers:
            self.uvlayers = UVLayers(tag=layer.name, table=[], uvindex=[0])       
 
        # Process the data
        for bpolygon in iter(self.bmesh.polygons):
            # VertexTable Indices
            pvertices = bpolygon.vertices
            vertices = prototype_PolygonVertices._replace(no=len(pvertices), indices=str(list(pvertices)))
            
            # Groups
            groups = [group for group in self.groups if self._isPolygonInGroup(bpolygon, group)]
        
            # prototype_PolygonUVs
            polyuvlayers=[]
            
            for lindex, layer in enumerate(self.bmesh.uv_layers):
                uvindices = []
                for vindex in pvertices:
                    # Get the UV value corresponding to this vertex
                    uv = layer.data[self._uvlayers[lindex].uvindex[0]].uv.to_tuple()
                    # Is this a new uv coming in
                    if self._vertexUVmapping[vindex][layer.name].get(uv) is None:
                        # Get the index from master uv table
                        table = self._uvlayers[lindex].table
                        index = len(table)
                        # Insert into the master uv table
                        table.append(uv)
                        # Log the uv in the vertices hash, so that when a shared uv comes by, we can just use this
                        self._vertexUVmapping[vindex][layer.name][uv] = index
                    else:
                        # This uv is shared, so reuse the index
                        index = self._vertexUVmapping[vindex][layer.name][uv]
                    
                    # Add to the polygons master uv index
                    uvindices.append(index)
                    # Ready to fetch the next raw uv
                    self._uvlayers[lindex].uvindex[0] += 1
                polyuvlayers.append(prototype_PolygonUVs._replace(tag=layer.name, indices=str(uvindices)))

            # Accumulate all the data for this Polygon
            polygon = prototype_Polygon._replace(index=bpolygon.index, vertices=vertices, groups=groups, uvlayers=polyuvlayers)
            
            # Append the Polygon to the list
            self.polygons = polygon
            
    # 'vertices' property (READ ONLY)
    @property
    def vertices(self):
        return (vertex.co for vertex in self.bmesh.vertices)
    
    # 'groups' property
    @property
    def groups(self):
        return iter(self._groups.names)
    @groups.setter
    def groups(self, value):
        self._groups.names.append(value)

    # 'uvlayers' property
    @property
    def uvlayers(self):
        return iter(self._uvlayers)
    @uvlayers.setter
    def uvlayers(self, layer):
        self._uvlayers.append(layer)
    
    # 'polygons' property
    @property
    def polygons(self):
        return (polygon for polygon in self._polygons)
    @polygons.setter
    def polygons(self, polygon):
        self._polygons.append(polygon)

###############################################################################
if __name__ == '__main__':
    vrs = vars(ExportMesh)
    from inspect import isgetsetdescriptor
    props = filter(isgetsetdescriptor, vrs.values())
    for prop in props:
        print(prop)

if False and __name__ == '__main__':
    object = bpy.context.active_object
    if object.type != 'MESH':
        raise Exception('MESH object must be selected')    
    else:
        # Blender Mesh
        bmesh = object.data
        
        # Processed Mesh
        pmesh = ExportMesh(bmesh)
        
        # rhom  Mesh
        mesh = rhom.Mesh()
        
        # PointTable
        for x, y, z in pmesh.vertices:
            mesh.addPoint(rhom.Point(x, y, z))

        # TexCoordTable
        for layer in pmesh.uvlayers:
            for u,v in layer.table:
                mesh.addTexCoord(layer.tag, rhom.TexCoord(u,v))
        
        # GroupTable, Material Table
        for group_name in pmesh.groups:
            mesh.addGroup(group_name)
        
        # ElementList, 
        for polygon in pmesh.polygons:
            element = mesh.addElement(polygon.vertices.no)
            mesh.setPointIndices(element, polygon.vertices.indices)
            for uvlayer in polygon.uvlayers:
                mesh.setTexCoordIndices(uvlayer.tag, element, uvlayer.indices)
            for group in polygon.groups:
                mesh.addElementToGroup(mesh.getElement(polygon.index), group)
                if group.endswith('Mtl'):
                    mesh.setMaterial(mesh.getElement(polygon.index), 'xxx_'+group)

        rhom.writeMesh('.'.join([object.name, 'obn']), mesh)
