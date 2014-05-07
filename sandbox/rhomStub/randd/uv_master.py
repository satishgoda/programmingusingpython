import bpy

# Get a handle to the active object
object = bpy.context.active_object

# If the object is in edit mode, come out of it
if object.mode == 'EDIT':
    bpy.ops.object.mode_set(mode='OBJECT', toggle=True)

# Get a handle to the active object's mesh data
bmesh = object.data

#########################################################################################

class ProcessBMeshForrhom(object):
    '''This classes takes as input a Blender Mesh and creates an IR
    (Intermediate Representation) to be used by rhom. Processing
    includes figuring out group membership of polygons, removing
    redundant data in Blender's uv point tables. Apart from the
    processing, this class provides a clean API to be used by the
    exporter.'''
    def __init__(self, mesh):
        self._export_mesh = {}
    
    
# MasterDict
export_mesh = {}

# this will be used to hash the uv's when processing the polygons one by one.
# Information from here is used to update polygons and uv_layers
# Can be deleted once pre-processing is done
export_mesh['vertices'] = { v.index: { 
                            uvlayer.name: {} for uvlayer in bmesh.uv_layers } 
                            for v in bmesh.vertices 
                          }

# Unique uvs as a result of pre-processing the polygons
export_mesh['uv_layers'] = { uvlayer.name: {
                                'uvindex': 0, 'table': []}  
                                for uvlayer in bmesh.uv_layers
                           }

# This will hold the vertices and uv indices for all the polygons
# as part of the pre-processing
export_mesh['polygons'] = { p.index: {
                                'vertices': {'no': -1, 'array': ''}, 
                                'uvlayers': {uvlayer.name: '' for uvlayer in bmesh.uv_layers},
                                'groups': [],
                                } 
                                for p in bmesh.polygons 
                          }

# This data is used by the per polygon pre-processing step to figure out 
export_mesh['groups'] = {'names': [group_name for group_name in sorted(bmesh.polygon_layers_int.keys())], 
                         'table': {p.index: [] for p in bmesh.polygons}
                        }

for polygon in bmesh.polygons:
    for group_name in export_mesh['groups']['names']:
        export_mesh['groups']['table'][polygon.index].append(bool(bmesh.polygon_layers_int[group_name].data[polygon.index].value))

####################### Start Pre-Processing ########################

def process_uv_layer(polygon, layer, export_mesh):
    uvtag = layer.name
    uvdata = layer.data
    uv_layer = export_mesh['uv_layers'][uvtag]
    uvindices = []
    
    for vindex in polygon.vertices:
        # Get the uv value corresponding to this vertex
        uv = uvdata[uv_layer['uvindex']].uv.to_tuple()
        
        # Is this a new uv coming in
        if export_mesh['vertices'][vindex][uvtag].get(uv) is None:
            # Get the index from master uv table
            index = len(export_mesh['uv_layers'][uvtag]['table'])
            # Insert into the master uv table
            export_mesh['uv_layers'][uvtag]['table'].append(uv)
            # Log the uv in the vertices hash, so that when a shared uv comes by, we can just use this
            export_mesh['vertices'][vindex][uvtag][uv] = index
        else:
            # This uv is shared, so reuse the index
            index = export_mesh['vertices'][vindex][uvtag][uv]
        # Add to the polygons master uv index
        uvindices.append(index)
        # Ready to fetch the next raw uv
        uv_layer['uvindex'] += 1
    # Store the uv index loop as  a ready to use list for rhom
    export_mesh['polygons'][polygon.index]['uvlayers'][uvtag] = '{0}'.format(str(uvindices))

# Group membership data for each polygon
def process_group_membership(polygon, export_mesh):
    polygon_groups = export_mesh['polygons'][polygon.index]['groups']
    groups_table = export_mesh['groups']['table']
    groups_names = export_mesh['groups']['names']
    for (group_index, is_present) in enumerate(groups_table[polygon.index]):
        if is_present:
            polygon_groups.append(groups_names[group_index])

# PRE PROCESSING OF THE MESH
for polygon in bmesh.polygons:
    # This data will be used for generating the Vertex Table
    vertices = export_mesh['polygons'][polygon.index]['vertices']
    vertices['no'] = len(polygon.vertices)
    vertices['array'] = '{0}'.format(str(list(polygon.vertices)))

    for layer in bmesh.uv_layers:
        process_uv_layer(polygon, layer, export_mesh)
        
    process_group_membership(polygon, export_mesh)

####################### End Pre-Processing ###########################

#from pprint import pprint
#pprint(export_mesh)

#################### Use rhom Stub to Create Obn ##################

if not False:
    import sys
    sys.path.append('/muse/satishg/learning/soc/obnblender/blender/io_scene_obn')
    import rhomstub as rhom

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
    
    rhom.writeMesh('Foo.obn', mesh)
