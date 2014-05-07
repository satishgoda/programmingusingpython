import bpy
import rhomstub as rhom

object = bpy.context.active_object

bmesh = object.data

# In line preprocessing to create export_mesh structure

mesh = rhom.Mesh()

for x, y, z in export_mesh.vertices:
    mesh.addPoint(rhom.Point(x, y, z))

for uvlayer in export_mesh.uvlayers:
    for u, v in export_mesh.UVs(uvlayer):
        mesh.addTexCoord(uvlayer.tag, rhom.TexCoord(u, v))

for group_name in export_mesh.groups:
    mesh.addGroup(group_name)

for polygon in export_mesh.polygons:
    vertices = polygon.vertices

    element = mesh.addElement(vertices.no)
    mesh.setPointIndices(element, vertices.array)

    for uvlayer in export_mesh.polygon.uvlayers:
        mesh.setTexCoordIndices(uvlayer.tag, element, uvlayer.array)

    for group in polygon.groups:
        mesh.addElementToGroup(mesh.getElement(polygon.index), group)
        if group.endswith('Mtl'):
            mesh.setMaterial(mesh.getElement(polygon.index), 'xxx_' + group)
