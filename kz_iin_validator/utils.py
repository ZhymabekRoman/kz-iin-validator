from typing import Union


def is_int(num: Union[int, str]) -> bool:
    try:
        int(num)
    except Exception:
        return False
    else:
        return True
