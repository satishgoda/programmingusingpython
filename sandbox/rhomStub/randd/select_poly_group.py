import bpy

object = bpy.context.active_object

if object.mode == 'EDIT':
    # If there are selected faces, deselect all
    if object.data.total_face_sel:    
        bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)

mesh = object.data

groups = sorted(mesh.polygon_layers_int.keys())

view_group = 'leftMtl'

for polygon in mesh.polygons:
    if mesh.polygon_layers_int[view_group].data[polygon.index].value == 1:
        polygon.select = True
        
if object.mode == 'OBJECT':
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
