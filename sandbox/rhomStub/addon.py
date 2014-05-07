bl_info = {
    "name": "RH OBN format",
    "author": "Satish Goda (satishgoda@gmail.com)",
    "blender": (2, 6, 5),
    "location": "File > Import-Export",
    "description": "Import-Export OBN with groups, material_groups, multiple uv's",
    "warning": "Heaviliy in development since March 18th, 2013",
    "wiki_url": "http://wiki.rh.com/mediawiki/Technology/SOC/Blog/Satishg/Obn_Import_Export_for_Blender",
    "tracker_url": "",
    "support": 'OFFICIAL',
    "category": "Import-Export"
    }

# My previous assumption was not correct!! Need to dig in more.. 
if "bpy" in locals():
    import imp
    if "import_obn" in locals():
        imp.reload(import_obn)
        print("imp.reload(import_obn)")
    if "export_obn" in locals():
        imp.reload(export_obn)
        print("imp.reload(export_obn)")


##############################################################################
import bpy
import bl_ui
from bpy.props import ( StringProperty,
                        BoolProperty,
                      )
import sys
sys.path.append('/home/satishg/learning/soc/obnblender/blender/io_scene_obn')

import rhomstub as rhom

# Set Editor Operators (bpy.ops.mesh.set_editor_*)

##############################################################################
class RHSetEditorCreateGroup(bpy.types.Operator):
    bl_idname = 'mesh.set_editor_create_group'
    bl_label = 'Create Group'
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        object = context.active_object
        return (object and object.data.total_face_sel)
    
    group_name = bpy.props.StringProperty(
                    name='Name of Group',
                    default='',
                    description='The name of the Polygon Group/Set that you want to create'    
                )
    
    def invoke(self, context, event):
        wm = context.window_manager    
        return wm.invoke_props_dialog(self)
    
    def execute(self, context):
        if self.group_name.strip() == '':
            self.report({'ERROR'}, "Empty group name.")
            return {'CANCELLED'}
        
        object = context.active_object

        edit_to_object = False
        if object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='EDIT', toggle=True)
            edit_to_object = True

        mesh = object.data

        if self.group_name in mesh.polygon_layers_int:
            if edit_to_object:
                bpy.ops.object.mode_set(mode='EDIT', toggle=True)
                edit_to_object = False
                context.scene.update()
            self.report({'ERROR'}, 'Group name "{0}" already exists'.format(self.group_name))
            return {'CANCELLED'}
        
        pli = mesh.polygon_layers_int.new(self.group_name.strip())

        for polygon in mesh.polygons:
            mesh.polygon_layers_int[self.group_name.strip()].data[polygon.index].value = polygon.select
            
        if edit_to_object:
            bpy.ops.object.mode_set(mode='EDIT', toggle=True)
            edit_to_object = False
        
        self.report({'INFO'}, 'Created group {0}'.format(self.group_name.strip()))
        return {'FINISHED'}
    
##############################################################################
class RHSetEditorRenameGroup(bpy.types.Operator):
    bl_idname = 'mesh.set_editor_rename_group'
    bl_label = 'Rename Group'
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        object = context.active_object
        return (object and len(object.data.polygon_layers_int))
    
    #group_enum = bpy.props.EnumProperty(
    #                update=
    #                name='Name of Group',
    #                default='',
    #                description='Existing groups in this model'    
    #            )
    
    group_to_rename = bpy.props.StringProperty(name="Group to Rename")
    
    group_new_name = bpy.props.StringProperty(name="Name of new Group")
    
    def invoke(self, context, event):
        wm = context.window_manager    
        return wm.invoke_props_dialog(self)
    
    def execute(self, context):
        object = context.active_object

        if object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='EDIT', toggle=True)

        mesh = object.data

        groups_existing = mesh.polygon_layers_int.keys()

        if (self.group_to_rename not in groups_existing):
            self.report({'ERROR'}, "Specified group does not exist")
            return {'CANCELLED'}
        elif (self.group_new_name.strip() == ''):
            self.report({'ERROR'},"Enter a name for renaming")
            return {'CANCELLED'}
        elif (self.group_new_name in groups_existing):
            self.report({'ERROR'},"Renamed group clashes with existing group")
            return {'CANCELLED'}

        mesh.polygon_layers_int[self.group_to_rename].name = self.group_new_name
        self.report({'INFO'}, 'Renamed group "{0}" to "{1}"'.format(self.group_to_rename, self.group_new_name))
        return {'FINISHED'}

##############################################################################
class RHSetEditorSelectGroup(bpy.types.Operator):
    bl_idname = 'mesh.set_editor_select_group'
    bl_label = 'Select Group'
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        object = context.active_object
        return (object and len(object.data.polygon_layers_int))

    group_name = StringProperty()

    def execute(self, context):
        object = context.active_object
        
        if object.mode == 'EDIT':
            if object.data.total_face_sel:
                bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.mode_set(mode='EDIT', toggle=True)

        mesh = object.data

        for polygon in mesh.polygons:
            if mesh.polygon_layers_int[self.group_name].data[polygon.index].value == 1:
                polygon.select = True

        bpy.ops.object.mode_set(mode='EDIT', toggle=True)

        return {'FINISHED'}

##############################################################################
class RHSetEditorAssignMaterialsFromGroups(bpy.types.Operator):
    bl_idname = 'mesh.set_editor_assign_material'
    bl_label = 'Assign pfx_*Mtl from *Mtl'
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        object = context.active_object
        return (object and
                 len(list(filter(lambda g: g.endswith('Mtl'), object.data.polygon_layers_int.keys())))
                 )
    
    def execute(self, context):
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

        self.report({'INFO'}, "Created material slots and materials")
        return {'FINISHED'}

##############################################################################
# RH Set Editor PANEL
class DATA_PT_poly_groups(bl_ui.properties_data_mesh.MeshButtonsPanel, bpy.types.Panel):
    bl_label = "R&H Set Editor"
    COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME', 'CYCLES'}
    
    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type == 'MESH')
    
    def draw(self, context):
        layout = self.layout
        object = context.object
        split = layout.split()
        split.operator('mesh.set_editor_create_group')
        split.operator('mesh.set_editor_rename_group')
        split.operator('mesh.set_editor_assign_material')
        
        if not len(object.data.polygon_layers_int):
            self.layout.label('This mesh does not contain Polygon sets')
        else:
            self.layout.label('This mesh has the following polygon sets')
            layout.prop(context.scene, 'set_editor_groups_filter')
            split = layout.split(percentage=0.88)
            column1 = split.column(align=True)
            column2 = split.column(align=True)

            poly_groups = object.data.polygon_layers_int.keys()
            groups_filter = context.scene.set_editor_groups_filter
            if context.scene.set_editor_groups_filter.strip() not in ('*', ''):
                poly_groups = tuple(filter(lambda g: g.endswith(groups_filter), poly_groups))
                poly_groups_filtered = list(set(object.data.polygon_layers_int.keys())-set(poly_groups))
            
            for poly_group in sorted(poly_groups):
                group_name = object.data.polygon_layers_int[poly_group].name
                column1.operator('mesh.set_editor_select_group', text=group_name).group_name = group_name
                column2.operator('mesh.set_editor_rename_group', text='Rename').group_to_rename = group_name
                
            if 'poly_groups_filtered' in locals():
                layout.label('Not displayed: {0} groups'.format(len(poly_groups_filtered)))

##############################################################################
class ImportOBN(bpy.types.Operator):
    bl_idname = "import_scene.obn"
    bl_label = "Import OBN"
    bl_options = {'PRESET', 'UNDO'}
    
    # fileselect modal dialog uses these properties
    filename_ext = "*.obn"
    filter_glob = StringProperty(
                    default="*.obn",
                    options={'HIDDEN'}
                    )
    
    # context.window_manager.fileselect_add(self) implicitly fills this 
    directory = StringProperty()
    filename = StringProperty()
    filepath = StringProperty()
    
    # User interface for the following properties will be generated
    notes = StringProperty(
                default="Created by satishg"
            )
    
    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
    def execute(self, context):
        _props = ('directory', 'filename', 'filepath', 'notes')
        prop_strings = [' -> '.join([prop, getattr(self, prop)]) for prop in _props]
        result_string = "Fileselect dialog returned\n\t{0}".format('\n\t'.join(prop_strings))
        
        self.report({'OPERATOR'}, result_string)
        print(result_string)
        
        import subprocess
        import os
        
        process = None
        data = None
        
        program = os.path.dirname(__file__) + os.path.sep + 'rhom/rhom_import_obn.py'
        process = subprocess.Popen([program, self.filepath], stdout=subprocess.PIPE)
        
        while True:
            import errno
            try:
                data = process.communicate()
                break
            except Exception as e:
                if e.errno == errno.EINTR:
                    continue
                else:
                    break
        
        datum, err = data
        datum = str(datum)
        
        print(datum.split('\\n')[1:-1], err)
        
        if datum == '':
            self.report({'OPERATOR'}, "Could not import")
        elif datum.startswith('ERROR'):
            self.report({'ERROR'}, datum)
        else:
            self.report({'OPERATOR'}, ', '.join(datum.split('\\n')[1:-1]))
        
        return {'FINISHED'}


##############################################################################
class ExportOBN(bpy.types.Operator):
    bl_idname = "export_scene.obn"
    bl_label = "Export OBN"
    bl_options = {'PRESET', 'UNDO'}

    # fileselect modal dialog uses these properties
    filename_ext = "*.obn"
    filter_glob = StringProperty(
                    default="*.obn",
                    options={'HIDDEN'}
                    )

    # context.window_manager.fileselect_add(self) implicitly fills this
    directory = StringProperty()
    filename = StringProperty()
    filepath = StringProperty()

   # User interface for the following properties will be generated
    notes = StringProperty(
                name="Notes",
                default="Created by satishg"
            )


    dump_only = BoolProperty(
                    name='Dump Script Only',
                    default=True
                )
    
    # Let the user choose where to save the exported OBN file
    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

    # Save the file
    def execute(self, context):
        object = context.active_object
        bmesh = object.data

        mesh = rhom.Mesh()

        for vertex in bmesh.vertices:
            x, y, z = vertex.co
            mesh.addPoint(rhom.Point(x, y, z))

        for uvtag in bmesh.uv_layers.keys():
            for datum in bmesh.uv_layers[uvtag].data:
                mesh.addTexCoord(uvtag, rhom.TexCoord(datum.uv.x, datum.uv.y))

        for group_name in ("all", "triangleMtl", "triangleDeform"):
            mesh.addGroup(group_name)

        if rhom.writeMesh('Foo.obn', mesh) == 0:
            self.report({"ERROR"}, mesh.exportError)

        return {'CANCELLED'}
        
        _filename = self.directory + object.name
        _rhom_py_file = _filename+'.py'

        fd = open(_rhom_py_file, mode='w')
        
        # Start writing data to the py file
        _shebang = '#/usr/bin/python\n'
        _imports = 'import rhom\nimport rml\n'
        _mesh = 'mesh = rhom.Mesh()\n'

        fd.write(_shebang)
        fd.write(_imports)
        fd.write(_mesh)

        # Write the Blender mesh vertices as rhom mesh points
        for vtx in bmesh.vertices:
            rml_point = 'rml.geom.Point3({co.x}, {co.y}, {co.z})'.format(co=vtx.co)
            rmeshpoint = 'mesh.addPoint({0})'.format(rml_point)
            fd.write(rmeshpoint+'\n')

        # Write the uv layers
        # TODO

        # Pre process groups for later usage
        poly_group_layer_names = sorted(bmesh.polygon_layers_int.keys())

        # The following dictionary contains key, value pairs corresponding to
        # Element index and a list of Boolean values that specify if an element
        # belongs to a polyGroup
        poly_groups_dict = {}
        for index in range(0, len(bmesh.polygons)):
            poly_groups_dict[index] = []
            for key in poly_group_layer_names:
                is_present = bool(bmesh.polygon_layers_int[key].data[index].value)
                poly_groups_dict[index].append(is_present)

        # Get a list of vertex loops that build elements
        vertTable = []
        for polygon in bmesh.polygons:
            temp = []
            for vertex in polygon.vertices:
                temp.append(str(vertex))
            vertTable.append('[{0}]'.format(','.join(temp)))
        elementTable = '[{0}]'.format(', '.join(vertTable))

        # Create elements from the data above
        fd.write('for vertices in {0}:\n'.format(elementTable))
        fd.write('    element = mesh.addElement(len(vertices))\n')
        fd.write('    mesh.setPointIndices(element, vertices)\n')

        # Create empty groups from polygon_layers_int
        for layername in poly_group_layer_names:
            fd.write('mesh.addGroup("{layername}")\n'.format(layername=layername))

        # Create material groups
        groups_materials = filter(lambda g: g.endswith('Mtl'), poly_group_layer_names)
        for group_material in groups_materials:
            fd.write('mesh.addMaterial("{0}")\n'.format('xxx_' + group_material))

        # Tag the elements with the polygroups that they belong to
        for findex in sorted(poly_groups_dict.keys()):
            poly_layer_status = poly_groups_dict[findex]
            for index, status in enumerate(poly_layer_status):
                if status:
                    group_name = poly_group_layer_names[index]
                    fd.write('mesh.addElementToGroup(mesh.getElement({0}), "{1}")\n'.format(findex, group_name))
                    if group_name.endswith('Mtl'):
                        fd.write('mesh.setMaterial(mesh.getElement({0}), "{1}")\n'.format(findex, 'xxx_'+group_name))

        # Finalize rhom script generation
        _obn_filename = _filename + '.obn'
        fd.write("rhom.writeMesh('{0}', mesh)\n".format(_obn_filename))
        fd.write("print('ExportOBN:Success. rhom created {0}')".format(_obn_filename))

        fd.flush()
        fd.close()

        self.report({'OPERATOR'}, ' '.join(['Exported', _rhom_py_file]))

        if self.dump_only == True:
            return {'FINISHED'}

        # Time to run the rhom python script that was generated previously
        import subprocess

        process = None
        data = None
        
        program = '/usr/bin/python'
        process = subprocess.Popen([program, _rhom_py_file], stdout=subprocess.PIPE)
        
        while True:
            import errno
            try:
                data = process.communicate()
                break
            except Exception as e:
                if e.errno == errno.EINTR:
                    continue
                else:
                    break
        
        datum, err = data
        datum = str(datum)

        print(datum)
        self.report({'OPERATOR'}, datum)
        
        return {'FINISHED'}


##############################################################################
# Menu Registration Callbacks
def menu_func_import(self, context):
    self.layout.operator(ImportOBN.bl_idname, text="R&H (.obn)")

def menu_func_export(self, execute):
    self.layout.operator(ExportOBN.bl_idname, text="R&H (.obn)")


##############################################################################
# Called when the user enables the add-on
def register():
    #print("Registering {0} and Menus".format(__name__))
    
    bpy.utils.register_module(__name__)

    bpy.types.Scene.set_editor_groups_filter = StringProperty(
                                                name="Filter",
                                                description="Specify which groups to view",
                                                default='*'
                                                )
    
    bpy.types.INFO_MT_file_import.append(menu_func_import)
    bpy.types.INFO_MT_file_export.append(menu_func_export)

# Called when the user disables the add-on
def unregister():
    #print("Unregistering {0} and Menus".format(__name__))

    del bpy.types.Scene.set_editor_groups_filter

    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

# We need this to make use of the Live-Edit feature in the Blender Text Editor
if __name__ == "__main__":
    register()
