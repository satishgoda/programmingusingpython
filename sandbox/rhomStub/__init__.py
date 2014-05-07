print("Importing rhom stub module")

from . import mesh

# Classes, Functions, Data exported by this package
__all__ = [
    "Mesh",
    "Point",
    "Normal",
    "TexCoord",
    "writeMesh",
]


def Mesh():
    '''Returns a new rhom.mesh.Mesh object'''
    return mesh.Mesh()


def writeMesh(filepath, mesh):
    '''Write's out a rhom python script to disk'''
    
    if mesh.hasPoints():
        # Start writing data to the py file
        print('Writing obn file {0}'.format(filepath))
        print('\n'.join(mesh.commands))
        print('rhom.writeMesh("{0}", mesh)'.format(filepath))
    else:
        print('ERROR: rhom.writeMesh: Mesh has no points')
        mesh.exportError = "ERROR: rhom.writeMesh: Mesh has no points"


def Point(x, y, z):
    '''returns a rhom.Point string to the caller'''
    return 'rhom.Point({0}, {1}, {2})'.format(x, y, z)


def Normal(nx, ny, nz):
    '''returns a rhom.Normal string to the caller'''
    return 'rhom.Normal({0}, {1}, {2})'.format(nx, ny, nz)


def TexCoord(u, v):
    '''returns a rhom.TexCoord string to the caller'''
    return 'rhom.TexCoord({0}, {1})'.format(u, v)



