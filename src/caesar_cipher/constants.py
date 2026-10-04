## @file constants.py
#  @brief Constants used by the Caesar cipher.

## Lowercase alphabet used to look up letter positions.
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

## Direction keyword for encoding.
DIRECTION_ENCODE = "encode"
## Direction keyword for decoding.
DIRECTION_DECODE = "decode"

## Prompt for the direction.
PROMPT_DIRECTION = "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
## Prompt for the message.
PROMPT_TEXT = "Type your message:\n"
## Prompt for the shift number.
PROMPT_SHIFT = "Type the shift number:\n"
## Prompt to continue.
PROMPT_AGAIN = "Type 'yes' if you want to go again. Otherwise type 'no'.\n"

## Name of the environment file holding tokens.
ENV_FILE = ".env"

## ASCII art title shown at start-up.
TITLE = r"""
  ____    _    _____ ____    _    ____
 / ___|  / \  | ____/ ___|  / \  |  _ \
| |     / _ \ |  _| \___ \ / _ \ | |_) |
| |___ / ___ \| |___ ___) / ___ \|  _ <
 \____/_/   \_\_____|____/_/   \_\_| \_\
  ____ ___ ____  _   _ _____ ____
 / ___|_ _|  _ \| | | | ____|  _ \
| |    | || |_) | |_| |  _| | |_) |
| |___ | ||  __/|  _  | |___|  _ <
 \____|___|_|   |_| |_|_____|_| \_\
"""

## ANSI escape code for bright cyan text.
COLOR_TITLE = "\033[96m"
## ANSI escape code that resets text colour.
COLOR_RESET = "\033[0m"
