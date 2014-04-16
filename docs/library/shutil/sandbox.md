```ipython
In [37]: shutil.os.path.exists(shutil.abspath('bapp'))
Out[37]: True

In [38]: shutil.os.path.islink(shutil.abspath('bapp'))
Out[38]: True

In [39]:
    
In [40]: shutil.os.rea(shutil.abspath('bapp'))

    
In [40]: shutil.os.readlink(shutil.abspath('bapp'))
Out[40]: '/home/satishg/education/python/library/subprocess/bapp/bapp.py'
    
In [41]: shutil.os.path.exists(shutil.abspath('blender'))
Out[41]: False
```
