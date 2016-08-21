

--------------------------------------------
Tinkering with AttributesGroupDefinition
--------------------------------------------
``aug 21, sun 2016``

.. code:: python
    
    for attribute in item1.attributes:
        print attribute.name
        if isinstance(attribute, AttributeDefinition):
            attr = getattr(item1, attribute.name)
            print attr.name, attr.value, attr.default, attr.path
         else:
            attrgrp = getattr(item1, attribute.name)
            for grattr in attrgrp.attributes:
                attr = getattr(attrgrp, grattr.name)
                print attr.name, attr.value, attr.default, attr.path

    id
    id 345 345 /items/item1.id
    display
    color grey grey /items/item1.display.color
    shape box box /items/item1.display.shape
