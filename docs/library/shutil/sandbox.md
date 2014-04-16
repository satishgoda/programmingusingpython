```python
In [37]: shutil.os.path.exists(shutil.abspath('bapp'))
Out[37]: True

In [38]: shutil.os.path.islink(shutil.abspath('bapp'))
Out[38]: True

In [40]: shutil.os.readlink(shutil.abspath('bapp'))
Out[40]: '/home/satishg/education/python/library/subprocess/bapp/bapp.py'
    
In [41]: shutil.os.path.exists(shutil.abspath('blender'))
Out[41]: False
```

In Python 3.3

```python
>>> shutil.which('bapp')
'/home/satishg/bin/bapp'

>>> shutil.os.path.islink(shutil.which('bapp'))
True

>>> shutil.os.readlink(shutil.which('bapp'))
'/home/satishg/education/python/library/subprocess/bapp/bapp.py'
```
