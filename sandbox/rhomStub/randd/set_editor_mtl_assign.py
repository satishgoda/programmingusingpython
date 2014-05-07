import bpy

object = bpy.context.active_object

if object.mode == 'EDIT':
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)

mesh = object.data

groups = sorted(mesh.polygon_layers_int.keys())
groups_mtl = filter(lambda group: group.endswith('Mtl'), groups)

for group_mtl in groups_mtl:
    # Create a material slot
    bpy.ops.object.material_slot_add()
    
    # Add a new material to the database 
    material = bpy.data.materials.new('xxx_' + group_mtl)
    
    # Set this material to the active mateiral slot
    object.material_slots[object.active_material_index].material = material
    
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
    
    if object.data.total_face_sel:
        bpy.ops.mesh.select_all(action='TOGGLE')
    
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
    
    for polygon in object.data.polygons:
        if object.data.polygon_layers_int[group_mtl].data[polygon.index].value == 1:
            polygon.select = True
    
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
    bpy.ops.object.material_slot_assign()
    
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
