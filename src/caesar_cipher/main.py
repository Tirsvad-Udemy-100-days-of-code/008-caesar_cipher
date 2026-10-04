## @file main.py
#  @brief Interactive command line interface.

import os
import sys

from caesar_cipher import constants as c
from caesar_cipher.cipher import caesar


def print_title() -> None:
    ## @brief Print the ASCII title, in colour when the terminal supports it.
    if sys.stdout.isatty() and "NO_COLOR" not in os.environ:
        os.system("")  # enables ANSI escape sequences on older Windows consoles
        print(f"{c.COLOR_TITLE}{c.TITLE}{c.COLOR_RESET}")
    else:
        print(c.TITLE)


def main() -> None:
    ## @brief Run the interactive encode/decode loop until the user stops.
    print_title()
    while True:
        direction = input(c.PROMPT_DIRECTION).strip().lower()
        if direction not in (c.DIRECTION_ENCODE, c.DIRECTION_DECODE):
            print("Please type 'encode' or 'decode'.")
            continue
        text = input(c.PROMPT_TEXT)
        try:
            shift = int(input(c.PROMPT_SHIFT))
        except ValueError:
            print("The shift must be a whole number.")
            continue

        print(f"Here's the {direction}d result: {caesar(text, shift, direction)}")

        if input(c.PROMPT_AGAIN).strip().lower() != "yes":
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
