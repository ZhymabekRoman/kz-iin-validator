import datetime as dt
from dataclasses import dataclass
from enum import Enum, auto
from typing import Union

from .exceptions import IINValidateError
from .utils import is_digit_string


@dataclass
class BornDate:
    day: int
    month: int
    year: int
    datetime: dt.datetime


class IINGender(Enum):
    male = auto()
    female = auto()


@dataclass
class IIN:
    iin: str
    is_person: bool
    gender: IINGender
    born_date: BornDate


class ValidatedIIN(IIN):
    is_validated: bool = True


def safe_validate_iin(iin: Union[str, IIN]):
    """
    Golang like function for IIN validation
    """
    try:
        result = validate_iin(iin)
    except Exception as ex:
        exception_msg = f"During validating IIN exception was caught: {str(ex)}"
        return None, exception_msg
    else:
        return result, None


# TODO: refactor into separate functions
def validate_iin(iin: Union[str, IIN]) -> ValidatedIIN:
    if isinstance(iin, IIN):
        iin = iin.iin
    elif not isinstance(iin, str):
        raise IINValidateError(f"Parametr 'iin' must be string, not {type(iin).__name__}")

    if not is_digit_string(iin):
        raise IINValidateError("IIN must contains only numbers")

    if len(iin) != 12:
        raise IINValidateError("IIN must be 12 length")

    # iin helper functions
    def iin_int(index):
        return int(iin[index])

    def iin_int_range(x, y):
        return int(iin[x:y])

    is_person = (iin_int(6) != 0)
    if is_person:
        if iin_int(6) % 2 == 1:
            gender = IINGender.male
        else:
            gender = IINGender.female
    else:
        raise IINValidateError("Can't parse gender information")

    centry_born_code = iin_int(6)
    centry_born_codes_list = {1: 18, 2: 18, 3: 19, 4: 19, 5: 20, 6: 20}
    centry_born = centry_born_codes_list.get(centry_born_code)
    if centry_born is None:
        raise IINValidateError("Can't parse centry from IIN: unknown centry information")

    year = int(f"{centry_born}{iin[0:2]}")
    month = iin_int_range(2, 4)
    day = iin_int_range(4, 6)

    if month not in range(1, 13):
        raise IINValidateError("Month is not valid")

    month_dict = {4: 30, 6: 30, 9: 30, 11: 30, 2: 28}
    day_bound = month_dict.get(month, 31)

    if day_bound == 28 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        day_bound = 29

    if day not in range(1, day_bound + 1):
        raise IINValidateError("Invalid day")

    date_string = f"{year}{month}{day}"
    date_format = dt.datetime.strptime(date_string, "%Y%m%d")

    born_date = BornDate(date_format.day, date_format.month, date_format.year, date_format)

    checksum_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    checksum_2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2]

    checksum_1_result = 0
    checksum_2_result = 0
    for i in range(11):
        checksum_1_result += iin_int(i) * checksum_1[i]
        checksum_2_result += iin_int(i) * checksum_2[i]

    checksum_1_mod = checksum_1_result % 11
    checksum_2_mod = checksum_2_result % 11

    control_digit = checksum_1_mod

    if checksum_1_mod == 10:
        if checksum_2_mod % 11 == 10:
            raise IINValidateError("This IIN is not active and usable!")

        if checksum_2_mod in range(0, 10):
            control_digit = checksum_2_mod

    if control_digit != iin_int(11):
        raise IINValidateError("Not correct control checksum")

    return ValidatedIIN(iin=iin, is_person=is_person, gender=gender, born_date=born_date)
