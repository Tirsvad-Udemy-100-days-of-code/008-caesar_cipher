## @file main.py
#  @brief Interactive command line interface.

from caesar_cipher import constants as c
from caesar_cipher.cipher import encrypt


def main() -> None:
    ## @brief Ask for a message and a shift, then print the encrypted text.
    text = input(c.PROMPT_TEXT)
    try:
        shift = int(input(c.PROMPT_SHIFT))
    except ValueError:
        print("The shift must be a whole number.")
        return
    print(f"Here's the encoded result: {encrypt(text, shift)}")


if __name__ == "__main__":
    main()
