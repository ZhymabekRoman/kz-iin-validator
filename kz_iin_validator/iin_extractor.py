import re

IIN_REGEX = re.compile(r"((0[48]|[2468][048]|[13579][26])0230[1-5]|000230[34]|\d\d((0[13578]|1[02])(0[1-9]|[12]\d|3[01])|(0[469]|11)(0[1-9]|[12]\d|30)|02(0[1-9]|[1-2]\d)))[0-6]\d{5}")


def extract_iin(text: str) -> list:
    matches = IIN_REGEX.findall(text)
    return matches
