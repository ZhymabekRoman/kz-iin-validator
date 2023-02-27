from kz_iin_validator import validate_iin, generate_iin, IINValidateError
import pytest


def test_valid_iin():
    for _ in range(20000):
        iin = generate_iin()
        validate_iin(iin)

    validate_iin(iin)

    for _ in range(20000):
        iin = generate_iin()
        validate_iin(iin, weak_fast_check=True)


def test_non_valid_iin():
    non_valid_iin_list = ["0000000", 868795643215, "sdf867", "/*-/*-gd098j6435"]
    for iin in non_valid_iin_list:
        with pytest.raises(IINValidateError):
            validate_iin(iin)
            validate_iin(iin, weak_fast_check=True)

        iin, err = validate_iin(iin, raise_exception=False)

        assert err != None
