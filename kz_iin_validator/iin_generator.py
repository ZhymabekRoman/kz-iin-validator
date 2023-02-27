import random


def generate_iin():
    # year = random.randint(1800, 2099)
    year = random.randint(0, 99)
    month = random.randint(1, 12)

    # TODO: manually generate gender instead generating with centry
    # gender = random.choice(list(IINGender))

    centry_and_gender_list = {1: 18, 2: 18, 3: 19, 4: 19, 5: 20, 6: 20}
    centry_and_gender_code = random.choice(list(centry_and_gender_list))
    centry_code = centry_and_gender_list[centry_and_gender_code]

    month_dict = {4: 30, 6: 30, 9: 30, 11: 30, 2: 28}
    day_bound = month_dict.get(month, 31)

    year_centry = int(f"{centry_code}{year:02}")

    if day_bound == 28 and ((year_centry % 4 == 0 and year_centry % 100 != 0) or year_centry % 400 == 0):
        day_bound = 29

    day = random.randint(1, day_bound)

    # zfill
    year_str = '{:02d}'.format(year)
    month_str = '{:02d}'.format(month)
    day_str = '{:02d}'.format(day)

    dob = f"{year_str}{month_str}{day_str}"

    individual_number = f"{random.randint(1, 9999):04d}"

    iin = f"{dob}{centry_and_gender_code}{individual_number}"

    # Calculate control digit
    checksum_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    checksum_2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2]
    checksum_1_result = 0
    checksum_2_result = 0
    for i in range(11):
        checksum_1_result += int(iin[i]) * checksum_1[i]
        checksum_2_result += int(iin[i]) * checksum_2[i]
    checksum_1_mod = checksum_1_result % 11
    checksum_2_mod = checksum_2_result % 11
    control_digit = checksum_1_mod
    if checksum_1_mod == 10:
        if checksum_2_mod % 11 == 10:
            # IIN is not active and usable, regenerate IIN
            return generate_iin()
        if checksum_2_mod in range(0, 10):
            control_digit = checksum_2_mod

    return f"{iin}{control_digit}"

