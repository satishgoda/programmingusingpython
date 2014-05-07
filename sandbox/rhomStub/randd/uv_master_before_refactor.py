if not False:
    fd = open("UVTest.py", mode='w')
    
    # Start writing data to the py file
    _shebang = '#/usr/bin/python\n'
    _imports = 'import rhom\nimport rml\n'
    _mesh = 'mesh = rhom.Mesh()\n\n'

    fd.write(_shebang)
    fd.write(_imports)
    fd.write(_mesh)
    
    # Write PointTable
    pointTableStr = str([vertex.co.to_tuple() for vertex in mesh.vertices])
    fd.write('#PointTable\nfor x, y, z in {0}:\n\tmesh.addPoint(rhom.Point(x, y, z))\n\n'.format(pointTableStr))
    del pointTableStr
    
    # Write TexCoord Table    
    for uvlayer in export_mesh['uv_layers']:
        uvtag = uvlayer
        texCoordTableStr = str(export_mesh['uv_layers'][uvtag]['table'])
        fd.write('#TexCoords.{1}\nfor u, v in {0}:\n\tmesh.addTexCoord("{1}", rhom.TexCoord(u,v))\n\n'.format(texCoordTableStr, uvtag))
    del texCoordTableStr
    
    # Add Groups
    groupNames = [group_name for group_name in export_mesh['groups']['names']]
    fd.write('#Groups\nfor group_name in {0}:\n\tmesh.addGroup(group_name)\n\n'.format(str(groupNames)))
    
    # Add Material Groups
    materialGroupNames = list(filter(lambda group_name: group_name.endswith('Mtl'), groupNames))
    fd.write('#Material Groups\nfor material_group_name in {0}:\n\tmesh.addMaterial(material_group_name)\n\n'.format(str(materialGroupNames)))
    
    # Write Polygon elements and uvs (TODO: and groups)
    polygons = export_mesh['polygons']
    for poly_index in polygons:
        polygon = polygons[poly_index]
        fd.write('element = mesh.addElement({0})\n'.format(polygon['vertices']['no']))
        fd.write('mesh.setPointIndices(element, {0})\n'.format(polygon['vertices']['array']))
        for uvlayer in export_mesh['uv_layers']:
            fd.write('mesh.setTexCoordIndices("{0}", element, {1})\n'.format(uvlayer, polygon['uvlayers'][uvlayer]))
        for group_name in polygon['groups']:
            fd.write('mesh.addElementToGroup(mesh.getElement({0}), "{1}")\n'.format(poly_index, group_name))
            if group_name.endswith('Mtl'):
                fd.write('mesh.setMaterial(mesh.getElement({0}), "{1}")\n'.format(poly_index, 'xxx_'+group_name))

    fd.write("rhom.writeMesh('{0}', mesh)\n".format("UVTest.obn"))
    fd.write("print('Exporting of \"{0}\" is done')\n".format("UVTest.obn"))
    
    fd.flush()
    fd.close()
        
    # Time to run the rhom python script that was generated previously
    if not False:
        import subprocess

        process = None
        data = None
        
        program = '/usr/bin/python'
        process = subprocess.Popen([program, "UVTest.py"], stdout=subprocess.PIPE)
        
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
