from kz_iin_validator import validate_iin

list_of_valid_iin = ["030616550688"]


def test_basic():
    for valid_iin in list_of_valid_iin:
        validate_iin(valid_iin)
