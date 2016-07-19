https://docs.python.org/2.7/library/ast.html

```python
import ast

code = """5"""

module = ast.parse(code)

module

# <_ast.Module at 0x4c95690>

module._fields

# ('body',)

ast.dump(module, annotate_fields=True, include_attributes=False)

# 'Module(body=[Expr(value=Num(n=5))])'

ast.dump(module, annotate_fields=True, include_attributes=True)

# 'Module(body=[Expr(value=Num(n=5, lineno=1, col_offset=0), lineno=1, col_offset=0)])'

ast.dump(module, annotate_fields=False, include_attributes=False)

# 'Module([Expr(Num(5))])'
```

```python
import ast

code = """x"""

module = ast.parse(code)

module

# <_ast.Module at 0x2d3b510>

ast.dump(module, annotate_fields=True, include_attributes=False)

# "Module(body=[Expr(value=Name(id='x', ctx=Load()))])"

ast.dump(module, annotate_fields=True, include_attributes=True)

# "Module(body=[Expr(value=Name(id='x', ctx=Load(), lineno=1, col_offset=0), lineno=1, col_offset=0)])"

ast.dump(module, annotate_fields=False, include_attributes=False)

# "Module([Expr(Name('x', Load()))])"

```
