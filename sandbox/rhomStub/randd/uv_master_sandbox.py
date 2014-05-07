>>> d = {polygon.index:[]  for polygon in m.polygons}
>>> d
{0: [], 1: [], 2: [], 3: []}

>>> 
>>> [d[polygon.index].append(m.polygon_layers_int[group_name].data[polygon.index].value) for polygon in m.polygons for group_name in m.polygon_layers_int.keys()]
[None, None, None, None, None, None, None, None, None, None, None, None]

>>> d
{0: [1, 1, 1], 1: [1, 1, 1], 2: [1, 1, 1], 3: [1, 1, 1]}

# Generate Master UV Vertex Table using the polygons
for polygon in mesh.polygons:
    # The following will index into the original uv layers list
    orig_uv_index = 0
    uvlayer = export_mesh['uv_layers']['uv']
    uvpt = uvlayer['points']
    uvind = uvlayer['indices']
    
    # This will be stored in the polygons.index.vertices list as a string
    vertex_indices = []

    for vindex in polygon.vertices:
        vertex_indices.append(vindex)

        vhash = export_mesh[vertices][vindex]
        
        # Is this Uv new
        if len(vhash) == 0:
            uvpt = uvlayer['points']
            # Add this uv point to
            uvpt.append("({uv.x}, {uv.y})".format(uv=mesh.uv_layers['uv'].data[orig_uv_index]))
            uvon = UvOldNew(orig_uv_index, (len(uvpt)-1))
            vhash.append(uvoldnew)
        # If the already contains
        else:
            pass

        # We will fetch the next uv
        orig_uv_index += 1
    
