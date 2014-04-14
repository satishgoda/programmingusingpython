The numbers module defines a hierarchy of numeric abstract base classes which progressively define more operations. None of the types defined in this module can be instantiated.


* [import numbers] (https://docs.python.org/dev/library/numbers.html)
* [PEP: A Type Hierarchy for Numbers] (http://legacy.python.org/dev/peps/pep-3141/)


```python
>>> import numbers
>>> trace(numbers.Integral)

__builtin__.object()
numbers.Number(__builtin__.object)
numbers.Complex(numbers.Number)
numbers.Real(numbers.Complex)
numbers.Rational(numbers.Real)
numbers.Integral(numbers.Rational)
```
