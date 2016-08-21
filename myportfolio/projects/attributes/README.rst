-----
About
-----

By making use of ``Python's descriptor protocol``, I have prototyped a very basic ``custom attributes system``. The attributes can also be saved and loaded back as presets. 

Attributes are defined on a class that is a subtype of ``DefinesAttributes``. At attribute definition stage, one can also mark them as read-only. When an instance of the ``DefinesAttributes`` subtype accesses the ``AttributeDefinition`` subtype, Python invokes the customized descriptor machinery and gets and sets the values.

The ``OperatorPresets`` class supports operators for adding and applying presets on ``Operator`` instances. My implementation of the custom descriptor attributes makes the job of serializing and serializing attribute name and values an easy process.


.. code:: Python

    class Operator(AppObjectBase):
        optype = "/ops"
        id = IntAttributeDefinition(123).asReadOnly()
        label = StringAttributeDefinition('An Example Operator')
        count = IntAttributeDefinition(0, min=0, max=10)


    oppresets = OperatorPresets()

    op1 = Operator("op1")

    oppresets.add(op1, 'defaults')

    try:
        oppresets.add(op1, 'defaults')
    except ValueError as e:
        print e

    try:
        op1.count.value = 100
    except ValueError as e:
        print e
    
    op1.count.value = 9

    op1.label.value = "My first operator"

    oppresets.add(op1, 'preset1')

    try:
       oppresets.apply(op1, 'preset2')
    except NameError as e:
        print e
    
    oppresets.apply(op1, 'defaults')

    oppresets.apply(op1, 'preset1')

    op2 = Operator("op2")

    oppresets.apply(op2, 'preset1')

-------------------
Classes Implemented
-------------------

  AttributeDefinition
  
  IntAttributeDefinition(AttributeDefinition)
  
  StringAttributeDefinition(AttributeDefinition)
  
  Attribute
  
  IntAttribute(Attribute)
  
  StringAttribute(Attribute)
  
  DefinesAttributes(type)
  
  AppObjectBase(__metaclass__ = DefinesAttributes )
  
  Operator(AppObjectBase)
  
  OperatorPresets

-------------
Class Diagram
-------------

.. image:: attributes.png

__________________
Program in Action
__________________


    In [220]: oppresets = OperatorPresets()

    In [221]: (executing line 193 of "attributes.py")

    In [222]: (executing line 195 of "attributes.py")

    Operator preset 'defaults' saved for '/ops/op1'

    {'count': 0, 'id': 123, 'uid': '0x123', 'label': 'An Example Operator'}

    In [223]: (executing lines 197 to 200 of "attributes.py")

    Operator preset 'defaults' already exists

    In [224]: (executing lines 202 to 205 of "attributes.py")

    Illegal value: 0 <= 100 && 100 <= 10

    In [225]: (executing line 207 of "attributes.py")

    In [226]: (executing line 209 of "attributes.py")

    In [227]: (executing line 211 of "attributes.py")

    Operator preset 'preset1' saved for '/ops/op1'

    {'count': 9, 'id': 123, 'uid': '0x123', 'label': 'My first operator'}

    In [228]: (executing lines 213 to 216 of "attributes.py")

    Operator preset 'preset2' does not exist

    In [229]: (executing line 218 of "attributes.py")

    Operator preset 'defaults' applied to '/ops/op1'

    {'count': 0, 'id': 123, 'uid': '0x123', 'label': 'An Example Operator'}

    In [230]: (executing line 220 of "attributes.py")

    Operator preset 'preset1' applied to '/ops/op1'

    {'count': 9, 'id': 123, 'uid': '0x123', 'label': 'My first operator'}

    In [231]: (executing line 222 of "attributes.py")

    In [232]: (executing line 224 of "attributes.py")

    Operator preset 'preset1' applied to '/ops/op1'

    {'count': 9, 'id': 123, 'uid': '0x123', 'label': 'My first operator'}


_______________
References
_______________
* https://docs.python.org/2/howto/descriptor.html

* http://martyalchin.com/2007/nov/23/python-descriptors-part-1-of-2

* http://www.informit.com/articles/printerfriendly/1309289
