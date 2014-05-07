import bpy
import rhomstub as rhom

object = bpy.context.active_object

bmesh = object.data

# In line preprocessing to create export_mesh structure

mesh = rhom.Mesh()

for vertex in bmesh.vertices:
    x, y, z = vertex.co
    mesh.addPoint(rhom.Point(x, y, z))

for uvtag in export_mesh['uv_layers'].keys():
    for uv in export_mesh['uv_layers'][uvtag]['table']:
        mesh.addTexCoord(uvtag, rhom.TexCoord(uv[0], uv[1]))

for group_name in export_mesh['groups']['names']:
    mesh.addGroup(group_name)

for polygon_index, polygon in export_mesh['polygons'].items():
    element = mesh.addElement(polygon['vertices']['no'])
    mesh.setPointIndices(element, polygon['vertices']['array'])
    for uvtag in export_mesh['uv_layers']:
        mesh.setTexCoordIndices(uvtag, element, polygon['uvlayers'][uvtag])
    for group_name in polygon['groups']:
        mesh.addElementToGroup(mesh.getElement(polygon_index), group_name)
        if group_name.endswith('Mtl'):
            mesh.setMaterial(mesh.getElement(polygon_index), 'xxx_' + group_name)
