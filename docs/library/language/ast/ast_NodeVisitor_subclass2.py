import ast
  
code = """x = 2
y = 3
"""
  
class CustomNodeVisitor(ast.NodeVisitor):
    def visit(self, node):
        print node, node._fields
        super(CustomNodeVisitor, self).visit(node)
     
    def visit_Num(self, node):
        print "\t", node.n
        super(CustomNodeVisitor, self).generic_visit(node)
     
    def visit_Name(self, node):
        print "\t", node.id, node.ctx
        super(CustomNodeVisitor, self).generic_visit(node)
     
    def visit_Assign(self, node):
        print "\t", node.targets
        print "\t", node.value
        super(CustomNodeVisitor, self).generic_visit(node)
        print "\n"
 
    def visit_Module(self, node):
        print node.body, "\n"
        super(CustomNodeVisitor, self).generic_visit(node)
  
module  = ast.parse(code)
  
CustomNodeVisitor().visit(module)
 
"""
<_ast.Module object at 0x2d4d790> ('body',)
    [<_ast.Assign object at 0x1d10b50>, <_ast.Assign object at 0x2d625d0>]
 
<_ast.Assign object at 0x1d10b50> ('targets', 'value')
    [<_ast.Name object at 0x1d10d90>]
    <_ast.Num object at 0x2d62790>
<_ast.Name object at 0x1d10d90> ('id', 'ctx')
    x <_ast.Store object at 0x1d06ed0>
<_ast.Store object at 0x1d06ed0> ()
<_ast.Num object at 0x2d62790> ('n',)
    2
 
<_ast.Assign object at 0x2d625d0> ('targets', 'value')
    [<_ast.Name object at 0x2d62810>]
    <_ast.Num object at 0x2d62850>
<_ast.Name object at 0x2d62810> ('id', 'ctx')
    y <_ast.Store object at 0x1d06ed0>
<_ast.Store object at 0x1d06ed0> ()
<_ast.Num object at 0x2d62850> ('n',)
    3
"""
