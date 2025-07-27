import re

def evaluate_expression(expr):
    """
    Recursively evaluate a mathematical expression with +, -, *, /, and parentheses.
    """
    expr = expr.replace('  ', '')

    # Handle parentheses 
    while '(' in expr:
        inner_most = re.search(r'\(([^()]+)\)', expr)
        if not inner_most:
            raise ValueError("Mismatched parentheses")
        sub_expr = inner_most.group(1)
        value = evaluate_expression(sub_expr)
        expr = expr[:inner_most.start()] + str(value) + expr[inner_most.end():]

    # Now evaluate without parentheses
    return eval_no_parentheses(expr)


def eval_no_parentheses(expr):
    """
    Evaluate expression without parentheses, handling operator precedence.
    """
    tokens = re.findall(r'-?\d+\.?\d*|[+\-*/]', expr)

    # Handle * and /
    i = 0
    while i < len(tokens):
        if tokens[i] in ('*', '/'):
            left = float(tokens[i - 1])
            right = float(tokens[i + 1])
            result = left * right if tokens[i] == '*' else left / right
            tokens[i - 1:i + 2] = [str(result)]
            i = 0  # Restart since list changed
        else:
            i += 1

    # Now handle + and -
    result = float(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = float(tokens[i + 1])
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        i += 2

    return result
