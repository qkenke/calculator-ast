import operator
import ast 
from pathlib import Path
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}
file_path = Path(__file__).parent / 'text.txt'
def eval_expr(expr):
    node = ast.parse(expr, mode = "eval").body
    return _eval(node)
def _eval(node):
    if isinstance(node,ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type( node.op)
        if op_type in operators:
            return operators[op_type](left,right)
        else:
            raise ValueError('Неразрешенный оператор')
    elif isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        return operators[op_type](operand)
    elif isinstance(node, ast.Constant):
        return node.value
    else:
        raise TypeError('Недопустимый элемент выражения')
with open(file_path,'r') as f:
    doks = f.read().strip()
    expr = eval_expr(doks)
    print('Zdez: ',doks)
    print('Rezult', expr)

