import re
from dataclasses import dataclass
from typing import Union, Optional
from enum import Enum, auto
from warnings import warn

IIN_REGEX_WEAK_FAST = re.compile("^[0-9]{12}$")
IIN_REGEX_WEAK = re.compile("^((0[48]|[2468][048]|[13579][26])0229[1-6]|000229[34]|\d\d((0[13578]|1[02])(0[1-9]|[12]\d|3[01])|(0[469]|11)(0[1-9]|[12]\d|30)|02(0[1-9]|1\d|2[0-8]))[0-6])\d{5}$")


class IINGender(Enum):
    male = auto()
    female = auto()


@dataclass
class IIN:
    iin: str
    # gender: IINGender


class ValidatedIIN(IIN):
    ...


def validate_iin(iin: Union[str, int, IIN]):
    # Sanitize input iin
    if isinstance(iin, IIN):
        iin = iin.iin
    elif isinstance(iin, str):
        iin_regex_fast = IIN_REGEX_WEAK_FAST.match(iin)
        if iin_regex_fast is None:
            raise ValueError("Not valid IIN!")
    elif isinstance(iin, int):
        warn("Do not use integer type for iin, leading zeros in decimal integer literals are not permitted")
        iin = str(iin)
    else:
        raise TypeError("Not valid IIN format!")

    iin_regex_weak = IIN_REGEX_WEAK.match(iin)
    if iin_regex_weak is None:
        raise ValueError("Not correct integers range")

    return ValidatedIIN(iin=iin)
