import bpy
import rhomstub as rhom

object = bpy.context.active_object

bmesh = object.data

# In line preprocessing to create export_mesh structure

mesh = rhom.Mesh()

for x, y, z in export_mesh.getVertices():
    mesh.addPoint(rhom.Point(x, y, z))

for uvlayer in export_mesh.getUVLayers():
    for u, v in export_mesh.UVs(uvlayer):
        mesh.addTexCoord(uvlayer.tag, rhom.TexCoord(u, v))

for group_name in export_mesh.getGroups():
    mesh.addGroup(group_name)

for polygon in export_mesh.getPolygons():
    vertices = export_mesh.getVertices(polygon)

    element = mesh.addElement(vertices.no)
    mesh.setPointIndices(element, vertices.array)

    for uvlayer in export_mesh.getUVLayers(polygon_index):
        mesh.setTexCoordIndices(uvlayer.tag, element, uvlayer.array)

    for group in export_mesh.getGroups(polygon_index):
        mesh.addElementToGroup(mesh.getElement(polygon_index), group.name)
        if group.name.endswith('Mtl'):
            mesh.setMaterial(mesh.getElement(polygon_index), 'xxx_' + group.name)
