import ast

code = """
x = 1

y = 2

z = x + y

x, y, z
"""

module = ast.parse(code)

module.body

ast.dump(module, annotate_fields=False, include_attributes=False)

# "Module([Assign([Name('x', Store())], Num(1)), Assign([Name('y', Store())], Num(2)), Assign([Name('z', Store())], BinOp(Name('x', Load()), Add(), Name('y', Load()))), Expr(Tuple([Name('x', Load()), Name('y', Load()), Name('z', Load())], Load()))])"

ast.dump(module, annotate_fields=True, include_attributes=False)

# "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], value=Num(n=1)), Assign(targets=[Name(id='y', ctx=Store())], value=Num(n=2)), Assign(targets=[Name(id='z', ctx=Store())], value=BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Name(id='y', ctx=Load()))), Expr(value=Tuple(elts=[Name(id='x', ctx=Load()), Name(id='y', ctx=Load()), Name(id='z', ctx=Load())], ctx=Load()))])"

class MyNodeVisitor(ast.NodeVisitor):
    def visit(self, node):
        print node
        return super(MyNodeVisitor, self).visit(node)

# import pdb
# pdb.set_trace()

MyNodeVisitor().visit(module)

"""
<_ast.Module object at 0x045ADF70>
<_ast.Assign object at 0x04C842B0>
<_ast.Name object at 0x04C84510>
<_ast.Store object at 0x040C0290>
<_ast.Num object at 0x04C84430>
<_ast.Assign object at 0x04C844D0>
<_ast.Name object at 0x04C844F0>
<_ast.Store object at 0x040C0290>
<_ast.Num object at 0x04C843F0>
<_ast.Assign object at 0x04C84470>
<_ast.Name object at 0x04C84330>
<_ast.Store object at 0x040C0290>
<_ast.BinOp object at 0x04C84410>
<_ast.Name object at 0x04C84370>
<_ast.Load object at 0x040C01D0>
<_ast.Add object at 0x040C0C90>
<_ast.Name object at 0x04C844B0>
<_ast.Load object at 0x040C01D0>
<_ast.Expr object at 0x04C84530>
<_ast.Tuple object at 0x04C84550>
<_ast.Name object at 0x04C84570>
<_ast.Load object at 0x040C01D0>
<_ast.Name object at 0x04C84590>
<_ast.Load object at 0x040C01D0>
<_ast.Name object at 0x04C845B0>
<_ast.Load object at 0x040C01D0>
<_ast.Load object at 0x040C01D0>
"""
