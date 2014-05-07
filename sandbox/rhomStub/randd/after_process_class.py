import sys
import rhomstub as rhom

object = bpy.context.active_object

bmesh = object.data

export_mesh = PreprocessBmesh(bmesh)

mesh = rhom.Mesh()

for vertex in bmesh.vertices:
    x, y, z = vertex.co
    mesh.addPoint(rhom.Point(x, y, z))

for uvtag, uvdata in export_mesh.getUvLayers():
    for u, v in uvdata:
        mesh.addTexCoord(uvtag, rhom.TexCoord(u, v))

for group_name in export_mesh.getGroups():
    mesh.addGroup(group_name)

for polygon in export_mesh.getPolygon():
    element = mesh.addElement(polygon.vertex_size)
    mesh.setPointIndices(element, polygon.vertex_indices)
    for uvtag in polygon.getUvlayers():
        mesh.setTexCoordIndices(uvtag, element, polygon.getIndices(uvtag))
    for group_name in polygon.getGroupNames():
        mesh.addElementToGroup(mesh.getElement(polygon.index), group_name)
        if group_name.endswith('mtl'):
            mesh.setMaterial(mesh.getElement(polygon.index), 'xxx_'+group_name)
