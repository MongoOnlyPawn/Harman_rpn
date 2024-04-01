import sys
import argparse
import readline  # noqa: F401, brings in up-arrow history

# local imports
import rpn_calc
import menu


def interactive_mode():
    error_counter = 0
    while True:
        try:
            try:
                expression = input(" > ")
            except KeyboardInterrupt:
                exit(0)

            expression = expression.strip().split()

            result = rpn_calc.evaluate_rpn(expression)

            if result is None:
                error_counter += 1
                if error_counter > 5:
                    menu.ask_for_help()
                    error_counter = 0

            print_stack = " ".join(
                str(int(x)) if isinstance(x, float) and x.is_integer() else str(x)
                for x in rpn_calc.stack
            )
            print(f"{print_stack}", end="")

        except EOFError:
            exit(0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", nargs="*")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        expression = sys.stdin.read().strip().split()
    elif args.expression:
        expression = args.expression
    else:
        interactive_mode()
        return

    result = rpn_calc.evaluate_rpn(expression)
    if result is not None:
        if len(rpn_calc.stack) > 1:
            print("Incomplete expression, remaining stack: ", end='')
        print_stack = " ".join(
            str(int(x)) if isinstance(x, float) and x.is_integer() else str(x)
            for x in rpn_calc.stack
        )
        print(f"{print_stack}")
    else:
        print("Expression did not evaluate. Try 'rpn help' for more info")


if __name__ == "__main__":
    main()
