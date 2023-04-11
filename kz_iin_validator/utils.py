import re

DIGIT_STRING = re.compile(r"^\d+$")


def is_digit_string(input_string: str, fast: bool = True, weak_fast_check: bool = False) -> bool:
    if fast and weak_fast_check:
        raise ValueError("weak_fast_check and fast can't be specified at one time")
     
    if weak_fast_check:
        return bool(DIGIT_STRING.match(input_string))
    elif fast:
        return input_string.isdigit()
    else:
        return all(char.isdigit() for char in input_string)
