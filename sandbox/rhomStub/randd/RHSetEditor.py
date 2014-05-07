import bpy

object = bpy.context.active_object

edit_to_object = False
if object.mode == 'EDIT':
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
    edit_to_object = True

mesh = object.data

polyset_name = 'smoo2'

if polyset_name not in mesh.polygon_layers_int:
    pli = mesh.polygon_layers_int.new(polyset_name)

for polygon in mesh.polygons:
    mesh.polygon_layers_int[polyset_name].data[polygon.index].value = polygon.select
    
if edit_to_object:
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
    edit_to_object = False
