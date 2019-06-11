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
VALID_INWARD_CODE_LETTERS = [
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

# These are the patterns we will use to validate the outward code
LETTER_NUMBER_PATTERN = re.compile(r"^%s\d$" % SINGLE_FIRST_POSITION_LETTERS)
LETTER_NUMBER_LETTER_PATTERN = re.compile(r"^%s\d%s$" % (
    VALID_FIRST_POSITION_LETTERS, VALID_THIRD_POSITION_LETTERS
))
LETTER_NUMBER_NUMBER_PATTERN = re.compile(
    r"^%s\d{2}$" % SINGLE_FIRST_POSITION_LETTERS
)
LETTER_LETTER_NUMBER_PATTERN = re.compile(r"^%s%s\d$" % (
    VALID_FIRST_POSITION_LETTERS, VALID_SECOND_POSITION_LETTERS
))
LETTER_LETTER_NUMBER_LETTER_PATTERN = re.compile(r"^%s%s\d%s$" % (
    VALID_FIRST_POSITION_LETTERS,
    VALID_SECOND_POSITION_LETTERS,
    VALID_FOURTH_POSITION_LETTERS
))
LETTER_LETTER_NUMBER_NUMBER_PATTERN = re.compile(r"^%s%s\d{2}$" % (
    VALID_FIRST_POSITION_LETTERS, VALID_SECOND_POSITION_LETTERS
))


class CharacterValidator:
    def __init__(self, postcode):
        self.outward_code = postcode[:len(postcode) - 3]
        self.inward_code = postcode[-3::]
        self.area_code = "".join(self.outward_code[:2])

    # The flow of testing is that the outward code and inward code is tested
    # If both return True we return True otherwise we raise a value error
    def validate_postcode_entries(self):
        if self.check_outward_code() and self.check_inward_code():
            return True

    # To test the outward code we check length and then run the regex
    def check_outward_code(self):
        if len(self.outward_code) == 2:
            return self.check_two_character_outward_code()
        elif len(self.outward_code) == 3:
            return self.check_three_character_outward_code()
        else:
            return self.check_four_character_outward_code()

    def check_two_character_outward_code(self):
        if LETTER_NUMBER_PATTERN.match(self.outward_code):
            return True
        raise ValueError("Invalid Postcode")

    def check_three_character_outward_code(self):
        if LETTER_NUMBER_LETTER_PATTERN.match(self.outward_code):
            return True

        elif LETTER_NUMBER_NUMBER_PATTERN.match(self.outward_code):
            return True

        elif LETTER_LETTER_NUMBER_PATTERN.match(self.outward_code) and \
                self.area_code not in AREAS_WITH_ONLY_DOUBLE_DIGIT_DISTRICTS:
            zero_district_code_check = int(self.outward_code[2])
            if zero_district_code_check == 0 and \
                    self.area_code not in ONLY_AREAS_WITH_ZERO_DISTRICT:
                raise ValueError("Invalid Postcode")
            else:
                return True

        raise ValueError("Invalid Postcode")

    def check_four_character_outward_code(self):
        if LETTER_LETTER_NUMBER_LETTER_PATTERN.match(self.outward_code):
            if self.area_code not in AREAS_WITH_ONLY_DOUBLE_DIGIT_DISTRICTS:
                return True
            raise ValueError("Invalid Postcode")

        elif LETTER_LETTER_NUMBER_NUMBER_PATTERN.match(self.outward_code):
            if self.area_code not in AREAS_WITH_ONLY_SINGLE_DIGIT_DISTRICTS:
                return True

        raise ValueError("Invalid Postcode")

    # This method inspects the Inward Code - we make sure it starts with
    # an integer and then 2 valid letters
    def check_inward_code(self):
        try:
            int(self.inward_code[0])
        except ValueError:
            raise ValueError("Invalid Postcode")
        else:
            if self.inward_code[1] in VALID_INWARD_CODE_LETTERS and \
                     self.inward_code[2] in VALID_INWARD_CODE_LETTERS:
                return True
            raise ValueError("Invalid Postcode")
