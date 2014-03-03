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
    suffix_num = 0
    
    def __init__(self, context, suffix=''):
        super(OutputImageFilename, self).__init__(context)
        if suffix:
            self.suffix=suffix    
    
    def getSuffix(self):
        suffix_base = super(OutputImageFilename, self).getSuffix()
        return '.'.join([suffix_base, str(self.suffix_num)])
        
if __name__ == '__main__':
    import bpy
    context = bpy.context
    ofn1 = OutputFilename(context)
    print(ofn1.filepath)
    oifn1 = OutputImageFilename(context, 'AREA')
    print(oifn1.filepath)
