## @file cipher.py
#  @brief Caesar cipher encryption and decryption.

from caesar_cipher.constants import ALPHABET


def encrypt(text: str, shift: int) -> str:
    ## @brief Encrypt a text with the Caesar cipher.
    #  @param text  Original text.
    #  @param shift Positions to move each letter (may be negative or > 26).
    #  @return The encrypted text; non-letters are kept, case is preserved.
    result = []
    for char in text:
        lower = char.lower()
        if lower in ALPHABET:
            new_position = (ALPHABET.index(lower) + shift) % len(ALPHABET)
            new_char = ALPHABET[new_position]
            result.append(new_char.upper() if char.isupper() else new_char)
        else:
            result.append(char)
    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    ## @brief Decrypt a Caesar-cipher text.
    #  @param text  Encrypted text.
    #  @param shift Shift that was used to encrypt.
    #  @return The original text.
    return encrypt(text, -shift)
