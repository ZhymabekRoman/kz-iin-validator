from kz_iin_validator import validate_iin, generate_iin, IINValidateError, _validate_iin
from kz_iin_validator.utils import is_digit_string
import pytest
import random


def test_valid_iin():
    for _ in range(20000):
        iin = generate_iin()
        validate_iin(iin)

    for _ in range(20000):
        iin = generate_iin()
        iin = _validate_iin(iin)
        validate_iin(iin)

    for _ in range(20000):
        iin = generate_iin()
        validate_iin(iin, weak_fast_check=True)


def test_non_valid_iin():
    non_valid_iin_list = ["0000000", 868795643215, "sdf867", "ajd85gt6h5yj", "/*-/*-gd098j6435", "821214240092"]

    _iin = list(generate_iin())
    _iin[6] = str(random.randint(7, 9))
    non_correct_centry_iin = "".join(_iin)
    non_valid_iin_list.append(non_correct_centry_iin)

    _iin = list(generate_iin())
    _iin[11] = str(int(_iin[11]) - 1)
    non_correct_control_sum_iin = "".join(_iin)
    non_valid_iin_list.append(non_correct_control_sum_iin)

    _iin = list(generate_iin())
    _iin[2:4] = str(random.randint(13, 99))
    non_correct_month_iin = "".join(_iin)
    non_valid_iin_list.append(non_correct_month_iin)

    _iin = list(generate_iin())
    _iin[4:6] = str(random.randint(32, 99))
    non_correct_date_iin = "".join(_iin)
    non_valid_iin_list.append(non_correct_date_iin)

    _iin = list(generate_iin())
    _iin[6] = str(0)
    non_correct_gender_iin = "".join(_iin)
    non_valid_iin_list.append(non_correct_gender_iin)

    for iin in non_valid_iin_list:
        with pytest.raises(IINValidateError):
            validate_iin(iin)
        with pytest.raises(IINValidateError):
            validate_iin(iin, weak_fast_check=True)

        iin_result, err = validate_iin(iin, raise_exception=False, full_error_info=False)
        assert err is not None

        iin_result, err = validate_iin(iin, raise_exception=False, full_error_info=True)
        assert err is not None


def test_utils():
    assert is_digit_string("1316456513")
    assert is_digit_string("sdfkjdsf") is False
    assert is_digit_string("656543413", fast=False)
    with pytest.raises(ValueError):
        assert is_digit_string("656543413", fast=True, weak_fast_check=True)
    assert is_digit_string("656543413", fast=False, weak_fast_check=True)
    assert is_digit_string("grarthaeg", fast=False) is False
