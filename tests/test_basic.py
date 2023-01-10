from kz_iin_validator import validate_iin

def test_basic():
    with open("tests/iin_list.txt") as file:
        while (line := file.readline().rstrip()):
            validate_iin(line)
