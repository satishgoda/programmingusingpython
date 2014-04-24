> exec(object[, globals[, locals]])

* https://docs.python.org/dev/library/functions.html?highlight=exec#exec

This function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). [1] If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input (see the section “File input” in the Reference Manual). Be aware that the return and yield statements may not be used outside of function definitions even within the context of code passed to the exec() function. The return value is None.

In all cases, if the optional parts are omitted, the code is executed in the current scope. If only globals is provided, it must be a dictionary, which will be used for both the global and the local variables. If globals and locals are given, they are used for the global and local variables, respectively. If provided, locals can be any mapping object. Remember that at module level, globals and locals are the same dictionary. If exec gets two separate objects as globals and locals, the code will be executed as if it were embedded in a class definition.

If the globals dictionary does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key. That way you can control what builtins are available to the executed code by inserting your own __builtins__ dictionary into globals before passing it to exec().

Note The built-in functions globals() and locals() return the current global and local dictionary, respectively, which may be useful to pass around for use as the second and third argument to exec().
Note The default locals act as described for function locals() below: modifications to the default locals dictionary should not be attempted. Pass an explicit locals dictionary if you need to see effects of the code on locals after function exec() returns.

# Example

```python
>>> i
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined

>>> exec('i = 1 + 2')

>>> i
3
>>> del i

>>> env = {}
>>> env['i'] = 0
>>> env['a'] = 10
>>> env['b'] = 20

>>> env
{'i': 0, 'a': 10, 'b': 20}

>>> exec('i = a + b', env)

>>> i
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined

>>> env.keys()
['i', 'a', 'b', '__builtins__']

>>> env['i']
30
```
