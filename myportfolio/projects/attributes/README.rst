-----
About
-----

By making use of Python's descriptor protocol, I have implemented a custom attributes system.

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
