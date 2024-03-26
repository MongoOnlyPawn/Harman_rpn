import sys
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

    for token in expression.split():
        if is_valid_number(token):
            stack.append(float(token))
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
            handle_constant(token)
        elif token in OTHER:
            handle_other(token)
        else:
            print("Error: Invalid token", token)
            return None

    if len(stack) != 1:
        stack.clear()
        return None

    return stack[0]


def handle_constant(token):
    if token == "pi":
        stack.append(math.pi)
    elif token == "e":
        stack.append(math.e)
    elif token == "rand":
        float_min = sys.float_info.min
        float_max = sys.float_info.max
        stack.append(random.uniform(float_min, float_max))


def handle_other(token):
    if token == "help":
        menu.display_help()
    elif token == "exit":
        exit(0)
    elif token == "clr":
        stack.clear()
    elif token == "dump":
        print(stack)


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
        return perform_unary_operation(perform_factorial_operation)


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
    stack.append(operation(operand))
    return True


def perform_binary_operation(operation):
    if len(stack) < 2:
        menu.show_error()
        return False
    operand2 = stack.pop()
    operand1 = stack.pop()
    stack.append(operation(operand1, operand2))
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
    operand1 = stack.pop()
    if operand2 == 0:
        print("Error: Division by zero")
        return False
    stack.append(operand1 / operand2)
    return True


def perform_factorial_operation():
    if len(stack) < 1:
        menu.show_error()
        print("Error: Insufficient operands for operator !")
        return False
    operand = stack.pop()
    if operand < 0 or not operand.is_integer():
        print("Error: Factorial undefined for negative numbers or non-integers")
        return False
    stack.append(math.factorial(int(operand)))
    return True


def is_valid_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False
