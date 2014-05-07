class ExportMesh(object):
    from collections import namedtuple
    
    PolygonVertices = namedtuple('PolygonVertices', ['no', 'indices'])
    prototype_PolygonVertices = PolygonVertices(-1, None)
    
    PolygonUVs = namedtuple('PolygonUVs', ['tag', 'indices'])
    prototype_PolygonUVs = PolygonUVs(tag='', indices='')
    
    Polygon = namedtuple('Polygon', ['index', 'vertices', 'groups', 'uvlayers'])
    prototype_Polygon = Polygon(-1, None, None, uvlayers=None)
    # The following is causing problems
    #prototype_Polygon = Polygon(-1, None, [], [])
    
    def __init__(self):
        self._polygons = []

    def getPolygon(self, index):
        return self._polygons[index]
    
    # polygons property is a managed attribute for _polygons list
    @property
    def polygons(self):
        # generator expression
        return (polygon for polygon in self._polygons)
    
    @polygons.setter
    def polygons(self, polygon):
        self._polygons.append(polygon)

if __name__ == '__main__':
    mesh = ExportMesh()
  
    # First Polygon: index 0      
    vertices = ExportMesh.prototype_PolygonVertices._replace(no=4, indices='[0,1,2,3]')
    groups = ['all', 'DLV1', 'bottomMtl']
    polygon = ExportMesh.prototype_Polygon._replace(index=0, vertices=vertices, groups=groups, uvlayers=[])
  
    mesh.polygons = polygon
    
    polygon = mesh.getPolygon(0)
    uvlayer1 = ExportMesh.prototype_PolygonUVs._replace(tag='uv', indices='[0, 1, 2, 3]')
    uvlayer2 = ExportMesh.prototype_PolygonUVs._replace(tag='uv2', indices='[0, 1, 2, 3]')
    polygon.uvlayers.append(uvlayer1)
    polygon.uvlayers.append(uvlayer2)
  
    # Second Polygon: index 1
    vertices = ExportMesh.prototype_PolygonVertices._replace(no=3, indices='[3,2,4]')
    polygon = ExportMesh.prototype_Polygon._replace(index=1, vertices=vertices, groups=[], uvlayers=[])
    
    mesh.polygons = polygon
    
    polygon = mesh.getPolygon(1)
    
    groups = ['all', 'DLV0', 'topMtl']
    polygon.groups.extend(groups)
    
    uvlayer1 = ExportMesh.prototype_PolygonUVs._replace(tag='uv', indices='[3, 2, 4]')
    uvlayer2 = ExportMesh.prototype_PolygonUVs._replace(tag='uv2', indices='[5, 4, 6]')
    polygon.uvlayers.extend([uvlayer1, uvlayer2])
      
    # Generate RMesh
    print(type(mesh.polygons))
    for polygon in mesh.polygons:
        print(polygon.index, polygon.vertices.indices, polygon.groups, polygon.uvlayers)
