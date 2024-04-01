import math
import random

# local import
import menu

stack = []

ARITHMETIC = {
    "+",
    "-",
    "*",
    "/",
    "!",
    "!=",
    "%",
    "++",
    "--",
}

NUM_UTILITIES = {
    "ceil",
    "floor",
    "round",
    "ip",
    "fp",
    "sign",
    "abs",
    "max",
    "min",
}

MATHMATIC_FUNCTIONS = {
    "exp",
    "fact",
    "sqrt",
    "ln",
    "log",
    "pow",
}

BITWISE = {
    "&",
    "|",
    "^",
    "~",
    ">>",
    "<<",
}

CONSTANTS = {"pi", "e", "rand"}

OTHER = {"help", "exit", "clr", "dump"}


def evaluate_rpn(expression):
    global stack

    for token in expression:
        #  only put numerical values in the stack
        if is_valid_number(token):
            stack.append(float(token))
        #  perform operation for non numeric values
        elif token in ARITHMETIC:
            if not perform_arithmetic_operation(token):
                return None
        elif token in NUM_UTILITIES:
            if not perform_numeric_utility(token):
                return None
        elif token in MATHMATIC_FUNCTIONS:
            if not perform_mathematic_function(token):
                return None
        elif token in BITWISE:
            if not perform_bitwise_function(token):
                return None
        elif token in CONSTANTS:
            if not handle_constant(token):
                return None
        elif token in OTHER:
            handle_other(token)
        else:
            print("Error: Invalid token", token)
            return None

    return stack


def handle_constant(token):
    if token == "pi":
        try:
            stack.append(math.pi)
        except Exception as e:
            print(f"Operational error: {e}")
            return False
    elif token == "e":
        try:
            stack.append(math.e)
        except Exception as e:
            print(f"Operational error: {e}")
            return False
    elif token == "rand":
        try:
            # import sys
            # float_min = sys.float_info.min  # way to big for practical use
            # float_max = sys.float_info.max
            float_min = -1000000000
            float_max = 1000000000
            stack.append(random.uniform(float_min, float_max))
        except Exception as e:
            print(f"Operational error: {e}")
            return False
    return True


def handle_other(token):
    if token == "help":
        menu.display_help()
    elif token == "exit":
        exit(0)
    elif token == "clr":
        stack.clear()


def perform_arithmetic_operation(token):
    if token == "+":
        return perform_binary_operation(lambda x, y: x + y)
    elif token == "-":
        return perform_binary_operation(lambda x, y: x - y)
    elif token == "*":
        return perform_binary_operation(lambda x, y: x * y)
    elif token == "/":
        return perform_division_operation()
    elif token == "!":
        return perform_factorial_operation()
    elif token == "!=":
        return perform_binary_operation(lambda x, y: x != y)
    elif token == "%":
        return perform_binary_operation(lambda x, y: x % y)
    elif token == "++":
        return increment()
    elif token == "--":
        return decrement()


def perform_numeric_utility(token):
    if token == "ceil":
        return perform_unary_operation(math.ceil)
    elif token == "floor":
        return perform_unary_operation(math.floor)
    elif token == "round":
        return perform_unary_operation(round)
    elif token == "ip":
        return perform_unary_operation(lambda x: int(x))
    elif token == "fp":
        return perform_unary_operation(lambda x: x - int(x))
    elif token == "sign":
        return perform_unary_operation(lambda x: 1 if x > 0 else -1 if x < 0 else None)
    elif token == "abs":
        return perform_unary_operation(abs)
    elif token == "max":
        return perform_binary_operation(lambda x, y: max(x, y))
    elif token == "min":
        return perform_binary_operation(lambda x, y: min(x, y))


def perform_mathematic_function(token):
    if token == "exp":
        return perform_unary_operation(math.exp)
    elif token == "fact":
        return perform_factorial_operation()


def perform_bitwise_function(token):
    if token == "&":
        return perform_binary_operation(lambda x, y: int(x) & int(y))
    if token == "|":
        return perform_binary_operation(lambda x, y: int(x) | int(y))
    if token == "^":
        return perform_binary_operation(lambda x, y: int(x) ^ int(y))
    if token == "~":
        return perform_unary_operation(lambda x: ~int(x))
    if token == ">>":
        return perform_binary_operation(lambda x, y: int(x) >> int(y))
    if token == "<<":
        return perform_binary_operation(lambda x, y: int(x) << int(y))


def perform_unary_operation(operation):
    if len(stack) < 1:
        menu.show_error()
        return False
    operand = stack.pop()
    try:
        stack.append(operation(operand))
    except Exception as e:
        stack.append(operand)
        print(f"Operational error: {e}")
        return False

    return True


def perform_binary_operation(operation):
    if len(stack) < 2:
        menu.show_error()
        return False
    operand2 = stack.pop()
    operand1 = stack.pop()
    try:
        stack.append(operation(operand1, operand2))
    except Exception as e:
        stack.append(operand1)
        stack.append(operand2)
        print(f"Operational error: {e}")
        return False
    return True


def increment():
    if len(stack) < 1:
        menu.show_error()
        return False
    stack[-1] += 1
    return True


def decrement():
    if len(stack) < 1:
        menu.show_error()
        return False
    stack[-1] -= 1
    return True


def perform_division_operation():
    if len(stack) < 2:
        menu.show_error()
        return False
    operand2 = stack.pop()
    if operand2 == 0:
        print("Error: Division by zero")
        return False
    # don't pop the stack completely until we are sure we can divide
    operand1 = stack.pop()
    try:
        stack.append(operand1 / operand2)
    except Exception as e:
        stack.append(operand1)
        stack.append(operand2)
        print(f"Operational error: {e}")
        return False
    return True


def perform_factorial_operation():
    if len(stack) < 1:
        menu.show_error()
        print("Error: Insufficient operands for operator !")
        return False
    operand = stack[-1]
    if operand < 0 or not operand.is_integer():
        print("Error: Factorial undefined for negative numbers or non-integers")
        return False
    if operand > 50:
        print(
            "Error: Factorial undefined for numbers greater "
            "than 50 - computational restraints"
        )
        return False
    try:
        stack.pop()
        stack.append(math.factorial(int(operand)))
    except Exception as e:
        stack.append(operand)
        print(f"Operational error: {e}")
        return False
    return True


def is_valid_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False
