
```python        
        cl.addFlag('-procs <num>', 'Number of processors to use.', convert=float, default='3.1315')
        cl.addFlag('-users <str> <str>', 'Number of users to process.', paramCount=2)
```

```python

In [1]: emailTemplate = "{0}.{1}@burger.com"

In [2]: emailTemplate.format('victor', 'qin')
Out[2]: 'victor.qin@burger.com'

In [3]: emailTemplate = "{fname}.{lname}@burger.com"

In [4]: emailRow = {'fname': 'victor', 'lname': 'qin'}

In [5]: email
emailRow       emailTemplate 

In [5]: emailTemplate.format(**email)
emailRow       emailTemplate 

In [5]: emailTemplate.format(**emailRow)
Out[5]: 'victor.qin@burger.com'

In [6]: emailTemplate.format(emailRow)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

KeyError: 'fname'

In [7]: emailTemplate.format(*emailRow)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

KeyError: 'fname'

In [8]: emailTemplate.format(**emailRow)
Out[8]: 'victor.qin@burger.com'

In [9]: emailRow = {'fname': 'victor'}

In [10]: emailTemplate.format(**emailRow)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/qjia/Desktop/scripts/<ipython console> in <module>()

KeyError: 'lname'
```
