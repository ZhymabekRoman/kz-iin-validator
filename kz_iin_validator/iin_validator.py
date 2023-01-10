import re
from dataclasses import dataclass
from typing import Union, Optional
from enum import Enum, auto
from warnings import warn
import datetime as dt

IIN_REGEX_WEAK_FAST = re.compile("^[0-9]{12}$")
IIN_REGEX_WEAK = re.compile("^((0[48]|[2468][048]|[13579][26])0229[1-6]|000229[34]|\d\d((0[13578]|1[02])(0[1-9]|[12]\d|3[01])|(0[469]|11)(0[1-9]|[12]\d|30)|02(0[1-9]|1\d|2[0-8]))[0-6])\d{5}$")

# TODO: integrate Pydantic validation

@dataclass
class BornDate:
    day: int
    month: int
    year: int
    _datetime: dt.datetime


class IINGender(Enum):
    male = auto()
    female = auto()
    unspecified = auto()


@dataclass
class IIN:
    iin: str
    is_person: bool
    gender: IINGender
    born_date: BornDate


class ValidatedIIN(IIN):
    is_validated: bool = True


def validate_iin(iin: Union[str, int, IIN], weak_fast_check: bool = False):
    # Sanitize input iin
    if isinstance(iin, IIN):
        iin = iin.iin
    elif isinstance(iin, str):
        ...
    elif isinstance(iin, int):
        warn("Do not use integer type for iin, leading zeros in decimal integer literals are not permitted")
        iin = str(iin)
    else:
        raise TypeError("Not valid IIN format!")

    if weak_fast_check:
        iin_regex_fast = IIN_REGEX_WEAK_FAST.match(iin)
        if iin_regex_fast is None:
            raise ValueError("Not valid IIN!")

        iin_regex_weak = IIN_REGEX_WEAK.match(iin)
        if iin_regex_weak is None:
            raise ValueError("Not correct integers range")

    if len(iin) != 12:
        raise ValueError("IIN must be 12 lenght")

    iin_int = lambda index: int(iin[index])

    is_person = (iin_int(6) != 0)
    if is_person:
        if iin_int(6) % 2 == 1:
            gender = IINGender.male
        else:
            gender = IINGender.female
    else:
        gender = IINGender.unspecified

    centry_born_code = iin_int(6)
    centry_born_codes_list = {1: 18, 2: 18, 3: 19, 4: 19, 5: 20, 6: 20}
    centry_born = centry_born_codes_list.get(centry_born_code)
    if not centry_born_code:
        raise ValueError("Can't parse centry from IIN")

    try:
        date_string = f"{centry_born}{iin[0:6]}"
        date_format = dt.datetime.strptime(date_string, "%Y%m%d")
    except Exception as ex:
        raise ValueError(f"Can't parse date from IIN. Error: {str(ex)}")

    born_date = BornDate(date_format.day, date_format.month, date_format.year, date_format)

    checksum_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    checksum_2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2]

    checksum_1_result = 0
    checksum_2_result = 0
    for i in range(11):
        checksum_1_result += iin_int(i) * checksum_1[i];
        checksum_2_result += iin_int(i) * checksum_2[i];

    checksum_1_mod = checksum_1_result % 11
    checksum_2_mod = checksum_2_result % 11

    control_digit = checksum_1_mod

    if checksum_1_mod == 10:
        if checksum_2_mod % 11 == 10:
            raise ValueError("This is IIN is not usable!")

        if checksum_2_mod in range(0, 10):
            control_digit = checksum_2_mod

    if control_digit != iin_int(11):
        raise ValueError("Not correct control checksum")

    return ValidatedIIN(iin=iin, is_person=is_person, gender=gender, born_date=born_date)
