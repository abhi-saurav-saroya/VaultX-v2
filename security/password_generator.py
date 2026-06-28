import secrets
import string


LETTERS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = "@_."

CHARACTERS = LETTERS + DIGITS + SYMBOLS


def generate_password(length=16):
    return "".join(
        secrets.choice(CHARACTERS)
        for _ in range(length)
    )