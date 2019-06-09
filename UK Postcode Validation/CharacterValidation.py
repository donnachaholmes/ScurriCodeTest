import re
# This class validates the data in the postcode
# There are certain letters only found in certain positions

FIRST_POSITION_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z'
]
SINGLE_FIRST_POSITION_LETTERS = ["B", "E", "G", "L", "M", "N", "S", "W"]
SECOND_POSITION_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y'
]
THIRD_POSITION_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
    'K', 'P', 'S', 'T', 'U', 'W'
]
FOURTH_POSITION_LETTERS = [
    'A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y'
]
INWARD_CODE_LETTERS = [
    'A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'N', 'P',
    'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z'
]

SINGLE_DIGIT_DISTRICTS = [
    'BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM',
    'SR', 'WN', 'ZE'
]
DOUBLE_DIGIT_DISTRICTS = ['AB', 'LL', 'SO']
ZERO_DISTRICTS = ['BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS']


class CharacterValidator:
    # To test the postcodes we need to split the post codes into the different
    # sections below. The flow of testing is that the inward code is tested
    # and if it is validated the outward code is then tested we return True if
    # it gets to the end of val, otherwise we return 'Invalid Postcode'
    def __init__(self, postcode):
        self.postcode = postcode
        self.outward_code = postcode[:len(postcode) - 3]
        self.inward_code = self.postcode[-3::]
        
        self.single_digit_area_letter = "".join(self.outward_code[:1])
        self.district_check = "".join(self.outward_code[:2])

        self.postcode_first_position = "".join(self.outward_code[:1])
        self.postcode_second_position = "".join(self.outward_code[1:2])
        self.postcode_third_position = "".join(self.outward_code[2:])
        self.postcode_fourth_position = "".join(self.outward_code[3:])

    def validate_postcode_entries(self):
        if self.check_outward_code() and self.check_inward_code():
            return True

    def check_outward_code(self):
        if len(self.outward_code) == 2:
            return self.two_character_outward_code()
        elif len(self.outward_code) == 3:
            return self.three_character_outward_code()
        else:
            return self.four_character_outward_code()

    # Next we validate Outward Code - First is two character long inward code
    def two_character_outward_code(self):
        if re.match(
                r"^%s\d$" % SINGLE_FIRST_POSITION_LETTERS,
                self.outward_code
        ):
            return True
        raise ValueError("Invalid Postcode")

    # Next is three character long validation, we test the format and the
    # letters are acceptable and the district is correct if it is double digit
    def three_character_outward_code(self):
        if re.match(
                r"^%s\d%s$" % (FIRST_POSITION_LETTERS, THIRD_POSITION_LETTERS),
                self.outward_code
        ):
            return True

        elif re.match(
                r"^%s\d{2}$" % SINGLE_FIRST_POSITION_LETTERS,
                self.outward_code
        ):
            return True

        elif re.match(
                r"^%s%s\d$" % (FIRST_POSITION_LETTERS, SECOND_POSITION_LETTERS),
                self.outward_code) \
                and self.district_check not in DOUBLE_DIGIT_DISTRICTS:
            zero_district_check = int(self.outward_code[2])
            if zero_district_check == 0 \
                    and self.district_check not in ZERO_DISTRICTS:
                raise ValueError("Invalid Postcode")
            else:
                return True

        raise ValueError("Invalid Postcode")

    # The final validation is against the four character inward codes
    # The two formats are tested and we test the districts are acceptable
    # whether it is double or single digit
    def four_character_outward_code(self):
        if re.match(
                r"^%s%s\d%s$" % (FIRST_POSITION_LETTERS, SECOND_POSITION_LETTERS, FOURTH_POSITION_LETTERS),
                self.outward_code
        ):
            if self.district_check not in DOUBLE_DIGIT_DISTRICTS:
                return True
            raise ValueError("Invalid Postcode")

        elif re.match(
                r"^%s%s\d{2}$" % (FIRST_POSITION_LETTERS, SECOND_POSITION_LETTERS),
                self.outward_code
        ):
            if self.district_check not in SINGLE_DIGIT_DISTRICTS:
                return True

        raise ValueError("Invalid Postcode")

    # The first method inspects the Inward Code - this is the final three
    # entries in a postcode - The format expected is Number Letter Letter
    # along with the correct letters being used
    def check_inward_code(self):
        last_three_entries = self.postcode[-3::]
        try:
            int(last_three_entries[0])
        except ValueError:
            raise ValueError("Invalid Postcode")
        else:
            if last_three_entries[1] in INWARD_CODE_LETTERS and \
                     last_three_entries[2] in INWARD_CODE_LETTERS:
                return True
            raise ValueError("Invalid Postcode")
