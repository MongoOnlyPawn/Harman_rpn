import sys
import readline

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

            result = rpn_calc.evaluate_rpn(expression)
            if result is not None:
                readline.add_history(expression)
                print(f"{result}", end="")
            else:
                error_counter += 1
                if error_counter > 5:
                    menu.ask_for_help()
                    error_counter = 0
        except EOFError:
            exit(0)


def main():
    args = sys.argv[1:]
    expression = " ".join(args)

    if expression:
        result = rpn_calc.evaluate_rpn(expression)
        if result is not None:
            print(" => ", result)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
