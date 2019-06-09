import re
# This class validates the data in the postcode
# There are certain letters only found in certain positions

VALID_FIRST_POSITION_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z'
]
SINGLE_FIRST_POSITION_LETTERS = ["B", "E", "G", "L", "M", "N", "S", "W"]
VALID_SECOND_POSITION_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y'
]
VALID_THIRD_POSITION_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
    'K', 'P', 'S', 'T', 'U', 'W'
]
VALID_FOURTH_POSITION_LETTERS = [
    'A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y'
]
INWARD_CODE_LETTERS = [
    'A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'N', 'P',
    'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z'
]

AREAS_WITH_ONLY_SINGLE_DIGIT_DISTRICTS = [
    'BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM',
    'SR', 'WN', 'ZE'
]
AREAS_WITH_ONLY_DOUBLE_DIGIT_DISTRICTS = ['AB', 'LL', 'SO']
ONLY_AREAS_WITH_ZERO_DISTRICT = [
    'BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS'
]

LETTER_NUMBER = re.compile(r"^%s\d$" % SINGLE_FIRST_POSITION_LETTERS)
LETTER_NUMBER_LETTER = re.compile(r"^%s\d%s$" % (
    VALID_FIRST_POSITION_LETTERS, VALID_THIRD_POSITION_LETTERS
))
LETTER_NUMBER_NUMBER = re.compile(
    r"^%s\d{2}$" % SINGLE_FIRST_POSITION_LETTERS
)
LETTER_LETTER_NUMBER = re.compile(r"^%s%s\d$" % (
    VALID_FIRST_POSITION_LETTERS, VALID_SECOND_POSITION_LETTERS
))
LETTER_LETTER_NUMBER_LETTER = re.compile(r"^%s%s\d%s$" % (
    VALID_FIRST_POSITION_LETTERS,
    VALID_SECOND_POSITION_LETTERS,
    VALID_FOURTH_POSITION_LETTERS
))
LETTER_LETTER_NUMBER_NUMBER = re.compile(r"^%s%s\d{2}$" % (
    VALID_FIRST_POSITION_LETTERS, VALID_SECOND_POSITION_LETTERS
))


class CharacterValidator:
    # To test the postcodes we need to split the post codes into the different
    # sections below. The flow of testing is that the inward code is tested
    # and if it is validated the outward code is then tested we return True if
    # it gets to the end of val, otherwise we return 'Invalid Postcode'
    def __init__(self, postcode):
        self.outward_code = postcode[:len(postcode) - 3]
        self.inward_code = postcode[-3::]
        self.area_code = "".join(self.outward_code[:2])

    def validate_postcode_entries(self):
        if self.check_outward_code() and self.check_inward_code():
            return True

    def check_outward_code(self):
        if len(self.outward_code) == 2:
            return self.check_two_character_outward_code()
        elif len(self.outward_code) == 3:
            return self.check_three_character_outward_code()
        else:
            return self.check_four_character_outward_code()

    # Next we validate Outward Code - First is two character long inward code
    def check_two_character_outward_code(self):
        if LETTER_NUMBER.match(self.outward_code):
            return True
        raise ValueError("Invalid Postcode")

    # Next is three character long validation, we test the format and the
    # letters are acceptable and the district is correct if it is double digit
    def check_three_character_outward_code(self):
        if LETTER_NUMBER_LETTER.match(self.outward_code):
            return True

        elif LETTER_NUMBER_NUMBER.match(self.outward_code):
            return True

        elif LETTER_LETTER_NUMBER.match(self.outward_code) and \
                self.area_code not in AREAS_WITH_ONLY_DOUBLE_DIGIT_DISTRICTS:
            zero_district_code_check = int(self.outward_code[2])
            if zero_district_code_check == 0 and \
                    self.area_code not in ONLY_AREAS_WITH_ZERO_DISTRICT:
                raise ValueError("Invalid Postcode")
            else:
                return True

        raise ValueError("Invalid Postcode")

    # The final validation is against the four character inward codes
    # The two formats are tested and we test the districts are acceptable
    # whether it is double or single digit
    def check_four_character_outward_code(self):
        if LETTER_LETTER_NUMBER_LETTER.match(self.outward_code):
            if self.area_code not in AREAS_WITH_ONLY_DOUBLE_DIGIT_DISTRICTS:
                return True
            raise ValueError("Invalid Postcode")

        elif LETTER_LETTER_NUMBER_NUMBER.match(self.outward_code):
            if self.area_code not in AREAS_WITH_ONLY_SINGLE_DIGIT_DISTRICTS:
                return True

        raise ValueError("Invalid Postcode")

    # The first method inspects the Inward Code - this is the final three
    # entries in a postcode - The format expected is Number Letter Letter
    # along with the correct letters being used
    def check_inward_code(self):
        try:
            int(self.inward_code[0])
        except ValueError:
            raise ValueError("Invalid Postcode")
        else:
            if self.inward_code[1] in INWARD_CODE_LETTERS and \
                     self.inward_code[2] in INWARD_CODE_LETTERS:
                return True
            raise ValueError("Invalid Postcode")
