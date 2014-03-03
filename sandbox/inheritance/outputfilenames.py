import os

class OutputFilename(object):
    filename = 'untitled'
    ext = 'blend'
    suffix = None
    suffix_char = '_'
    dirname = os.getcwd()
    
    def __init__(self, context):
        import bpy
        import os
        _filepath = context.blend_data.filepath
        self.filename = bpy.path.display_name_from_filepath(_filepath)
        self.dirname = os.path.dirname(_filepath)

    def getSuffix(self):
        return self.suffix_char + self.suffix
    
    @property
    def filepath(self):
        import os
        filename = self.filename
        if self.suffix:
            filename += self.getSuffix()
        filename += '.' + self.ext
        return os.path.join(self.dirname, filename)


class OutputImageFilename(OutputFilename):
    ext = 'png'
    def __init__(self, context):
        super(OutputImageFilename, self).__init__(context)    
    
        
if __name__ == '__main__':
    import bpy
    context = bpy.context
    ofn1 = OutputFilename(context)
    print(ofn1.filepath)
    oifn1 = OutputImageFilename(context)
    print(oifn1.filepath)
