def show_error():
    print("Input is not RPN")


def ask_for_help():
    print("Do you need help? Type 'help' in interactive mode for usage information")


def display_help():
    print(
        """
=============================================================
|                                                           |
|          Reverse Polish Notation (RPN) Calculator         |
|                                                           |
=============================================================
Usage:
  rpn [expression]
  rpn
  > [interactive mode]

Description:
  RPN is a mathematical notation where every operator follows
  all of its operands. This command-line tool evaluates
  arithmetic expressions provided in Reverse Polish Notation.

  Supported operators:
    +, -, *, /, !, !=, %, ++, --,
    ceil, floor, round, ip(integer part),
    fp(floating part), sign, abs(absolute value),
    max, min,

  Bitwise operators:
    &, |, ^, ~, <<, >>

  Supported constants:
    pi, e

  Other:
    rand(random number)

Examples:
  To evaluate the expression "(3 + 4) * 5", run:
  $ rpn 3 4 + 5 *

  To evaluate the expression "pi / 2", run:
  $ rpn pi 2 /


Interactive Mode:
  If no expression is provided, the tool enters interactive mode
  where you can continuously input RPN expressions. To exit
  interactive mode, type 'exit' and press Enter.

Notes:
  - Separate each token in the expression with spaces.
  - Do not enclose the expression in quotes.
  - Use "clr" to clear the calculator stack in interactive mode
"""
    )
