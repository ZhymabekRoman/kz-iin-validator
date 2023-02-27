import re

DIGIT_STRING = re.compile(r"^\d+$")


def is_digit_string(input_string: str, fast: bool = True):
    if fast:
        return bool(DIGIT_STRING.match(input_string))
    else:
        return all(char.isdigit() for char in input_string)
