"""Инженерный калькулятор"""


import operator


def calculate(expression1):
    """
    Calculates a mathematical expression.

    Args:
        expression1: a string with a mathematical expression.

    Returns:
        calculation result or error message.
    """
    try:
        tokens = expression1.split()

        if len(tokens) < 3 or len(tokens) % 2 == 0:
            raise ValueError("Invalid expression")

        operands = []
        operations = []

        for token in tokens:
            if token in ["+", "-", "*", "/", "**"]:
                while (operations and operations[-1]
                       in ["**", "*", "/"] and token in ["+", "-"]):
                    op = operations.pop()
                    b = operands.pop()
                    a = operands.pop()
                    operands.append(operator_funcs[op](a, b))
                operations.append(token)
            else:
                operands.append(float(token))

        while operations:
            op = operations.pop()
            b = operands.pop()
            a = operands.pop()
            operands.append(operator_funcs[op](a, b))

        return operands[0]

    except ValueError as e:
        return str(e)
    except ZeroDivisionError:
        return "Error: division by zero"
    except (TypeError, IndexError):
        return "Error: invalid expression"


operator_funcs = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow,
}

while True:
    expression = input("~ ")
    if expression.lower() == "exit":
        break
    result = calculate(expression)
    print(result)
