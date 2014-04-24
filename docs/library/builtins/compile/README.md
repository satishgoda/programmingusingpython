> compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). source can either be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how to work with AST objects.

The filename argument should give the file from which the code was read; pass some recognizable value if it wasn’t read from a file ('<string>' is commonly used).

The mode argument specifies what kind of code must be compiled; it can be 'exec' if source consists of a sequence of statements, 'eval' if it consists of a single expression, or 'single' if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something other than None will be printed).

* https://docs.python.org/dev/library/functions.html#compile

# Example

```python
>>> env = {}
>>> env['i'] = 0
>>> env['a'] = 10
>>> env['b'] = 20

>>> env
{'i': 0, 'a': 10, 'b': 20}
   
>>> stmt = 'i = a + b'

>>> code = compile(stmt, '<string>', 'single')

>>> code
<code object <module> at 0x1e57918, file "<string>", line 1>

>>> exec(code)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'a' is not defined

>>> exec(code, env)

>>> env.keys()
['i', 'a', 'b', '__builtins__']

>>> env['i']
30
```
