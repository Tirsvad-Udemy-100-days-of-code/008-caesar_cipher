# Caesar Cipher – documentation

Each letter is moved `shift` places through the alphabet:
`new_position = (ALPHABET.index(letter) + shift) % 26`.
The modulo keeps positions in range for shifts past `z`.
Non-letters are left untouched and letter case is preserved.

API reference: run `doxygen Doxyfile` from the repository root and open
`docs/doxygen/html/index.html`. The step-by-step plan is in [plan.md](plan.md).
