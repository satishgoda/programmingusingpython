import bpy

object = bpy.context.active_object

if object.mode == 'EDIT':
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)

mesh = object.data

group_existing = 'foo'
group_existing_rename_to = 'DLV1'

groups_existing = mesh.polygon_layers_int.keys()

if (group_existing not in groups_existing):
    raise Exception("Specified group does not exist")
elif (group_existing_rename_to in groups_existing):
    raise Exception("Renamed group clashes with existing group")
else:
    mesh.polygon_layers_int[group_existing].name = group_existing_rename_to
