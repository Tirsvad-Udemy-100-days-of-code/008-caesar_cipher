## @file cipher.py
#  @brief Caesar cipher: one shared function for encoding and decoding.

from caesar_cipher.constants import ALPHABET, DIRECTION_DECODE, DIRECTION_ENCODE


def caesar(text: str, shift: int, direction: str) -> str:
    ## @brief Encode or decode a text with the Caesar cipher.
    #  @param text      Text to transform.
    #  @param shift     Positions to move each letter (may be negative or > 26).
    #  @param direction DIRECTION_ENCODE or DIRECTION_DECODE.
    #  @return The transformed text; non-letters are kept, case is preserved.
    #  @throws ValueError If direction is not a known direction.
    if direction == DIRECTION_DECODE:
        shift = -shift
    elif direction != DIRECTION_ENCODE:
        raise ValueError(f"Unknown direction: {direction!r}")

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


def encrypt(text: str, shift: int) -> str:
    ## @brief Encrypt a text with the Caesar cipher.
    #  @param text  Original text.
    #  @param shift Number of positions to shift forward.
    #  @return The encrypted text.
    return caesar(text, shift, DIRECTION_ENCODE)


def decrypt(text: str, shift: int) -> str:
    ## @brief Decrypt a Caesar-cipher text.
    #  @param text  Encrypted text.
    #  @param shift Shift that was used to encrypt.
    #  @return The original text.
    return caesar(text, shift, DIRECTION_DECODE)
