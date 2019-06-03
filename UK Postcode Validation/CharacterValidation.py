import re

# This class validates the data in the postcode
# For certain positions, only certain letters are expected - these are added to lists for checking
# There are also certain area codes that can be used with certain districts that are included in a list for validation
# We also include a list of numbers (range used to produce) for testing number positions
# We make these variables in the upper case so that they cannot be edited or changed and the entries are all upper as
# the postcodes are sent in that format
# I did not include any extra validation for the London district as it should just change the format of the postcode

NUMBERS = range(0, 10)
FIRST_POSITION_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S',
                          'T', 'U', 'W', 'Y', 'Z']
SINGLE_FIRST_POSITION_LETTERS = ["B", "E", "G", "L", "M", "N", "S", "W"]

SECOND_POSITION_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L',
                           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
THIRD_POSITION_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'P', 'S', 'T', 'U', 'W']
FOURTH_POSITION_LETTERS = ['A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y']
FINAL_TWO_POSITIONS_LETTERS = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'L',
                               'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']

FIRST_AND_SECOND_POSITION_LETTERS = (FIRST_POSITION_LETTERS, SECOND_POSITION_LETTERS)
FIRST_AND_THIRD_POSITION_LETTERS = (FIRST_POSITION_LETTERS, THIRD_POSITION_LETTERS)
FIRST_SECOND_AND_FOURTH_POSITION_LETTERS = (FIRST_POSITION_LETTERS, SECOND_POSITION_LETTERS, FOURTH_POSITION_LETTERS)

SINGLE_DIGIT_DISTRICTS = ['BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM', 'SR', 'WN', 'ZE']
DOUBLE_DIGIT_DISTRICTS = ['AB', 'LL', 'SO']
ZERO_DISTRICTS = ['BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS']


class CharacterValidator:
    # For analysis, we will require the postcode to be split into different sections
    # These include the single entries for the first four and final two entries in the postcode
    # The full postcode is assigned along with the outward code (area and district)
    # To make the code more readable, I assigned variables to test whether the area code belongs to a double digit
    # district, a single digit district and single digit area with their corresponding districts
    # This will be more clear by the code below
    # These are all the type list to make analysing the individual entries easier

    # The flow of testing is that the inward code is tested and if it is validated the outward code is then tested
    def __init__(self, area_and_district_list, full_postcode_list):
        self.area_and_district_list = area_and_district_list
        self.full_postcode_list = full_postcode_list
        self.single_digit_area_letter = "".join(area_and_district_list[:1])
        self.single_digit_district_test = "".join(area_and_district_list[:2])
        self.double_digit_district_test = "".join(area_and_district_list[:2])

        self.postcode = "".join(area_and_district_list)
        self.postcode_first_position = "".join(area_and_district_list[:1])
        self.postcode_second_position = "".join(area_and_district_list[1:2])
        self.postcode_third_position = "".join(area_and_district_list[2:])
        self.postcode_fourth_position = "".join(area_and_district_list[3:])

    # The first method inspects the Inward Code - this is the final three entries in a postcode
    # The format expected is Number Letter Letter
    # We have a couple of cases that inspect the individual entries to ensure they are valid
    def test_postcode_sector_and_unit_entries(self):
        last_three_entries = self.full_postcode_list[len(self.full_postcode_list):len(self.full_postcode_list) - 4:-1]
        last_three_entries = last_three_entries[::-1]

        # We first ensure the first entry in the Inward code is an integer
        # If it is not we will return an error detailing this
        try:
            first_node = int(last_three_entries[0])
        except ValueError:
            raise ValueError("Invalid Postcode")

        # The next piece of validation is around ensuring the first node is a valid number and
        # the final two letters are in the list of acceptable letters
        # If an entry is not in the list of acceptable letters or the
        else:
            if first_node in NUMBERS \
                    and last_three_entries[1] in FINAL_TWO_POSITIONS_LETTERS \
                    and last_three_entries[2] in FINAL_TWO_POSITIONS_LETTERS:
                return True
            else:
                raise ValueError("Invalid Postcode")

    # Next we look into validating the Inward Code - consisting of the are and district code
    # The first one we look it is when this is two characters long
    # The only format that is expected here are is a letter and then a number
    # We use regex to ensure that the format is LetterNumber and that the letter is in the accepted list of letters
    def two_character_postcode_area_and_district_validation(self):
        if re.match(r"^%s\d$" % SINGLE_FIRST_POSITION_LETTERS, self.postcode):
            return self.test_postcode_sector_and_unit_entries()

        # Otherwise, we return an error that this in valid format and give the correct one
        else:
            raise ValueError("Invalid Postcode")

    # Next Inward Code for inspection are those of length three
    # These have the most types of formats accepting 3 types - LetterNumberLetter, LetterLetterNumber
    # or LetterNumberNumber
    # We use Regex again for this, giving the three entries and matching against their respecting acceptable entries
    def three_character_postcode_area_and_district_validation(self):
        if re.match(r"^%s\d%s$" % FIRST_AND_THIRD_POSITION_LETTERS, self.postcode):
            return self.test_postcode_sector_and_unit_entries()

        elif re.match(r"^%s\d{2}$" % SINGLE_FIRST_POSITION_LETTERS, self.postcode):
            return self.test_postcode_sector_and_unit_entries()

        # The format LetterLetterNumber requires additional formatting
        # There are only a few areas that are 2 letters long and have a single digit district
        # This is one of the special validation cases mentioned above - we use the double digit district test
        # variable (which is just the postcode area and compare it against the list of areas that have single digit
        # districts. If it matches, we test the outward code, otherwise we return a detailed error
        elif re.match(r"^%s%s\d$" % FIRST_AND_SECOND_POSITION_LETTERS, self.postcode) \
                and self.double_digit_district_test not in DOUBLE_DIGIT_DISTRICTS:
            zero_district_test = list(self.postcode)
            zero_district_test = int(zero_district_test[2])
            if zero_district_test == 0 and self.double_digit_district_test not in ZERO_DISTRICTS:
                raise ValueError("Invalid Postcode")
            else:
                return self.test_postcode_sector_and_unit_entries()

        # Finally we return any other errors, including an invalid format of the postcode sent which is the only
        # possible case here
        else:
            raise ValueError("Invalid Postcode")

    # The final validation is against the four character inward codes
    # There are two formats accepted - LetterLetterNumberLetter and LetterLetterNumberNumber
    # We validate again with regex against the expected values in each of the entries with further validation
    # detailed below
    def four_character_postcode_area_and_district_validation(self):
        if re.match(r"^%s%s\d%s$" % FIRST_SECOND_AND_FOURTH_POSITION_LETTERS, self.postcode):
                # As this is a double digit area with a single digit district, we need to ensure that the area is not
                # specified to only have a double digit district before validating - we again return a detailed error
                # if conditions are not met
                if self.double_digit_district_test not in DOUBLE_DIGIT_DISTRICTS:
                    return self.test_postcode_sector_and_unit_entries()
                else:
                    raise ValueError("Invalid Postcode")

        # The extra validation here is making sure the area code is not in the only single digit district code list
        # If it is, we throw an error detailing this
        elif re.match(r"^%s%s\d{2}$" % FIRST_AND_SECOND_POSITION_LETTERS, self.postcode):
                if self.single_digit_district_test not in SINGLE_DIGIT_DISTRICTS:
                    return self.test_postcode_sector_and_unit_entries()
                else:
                    raise ValueError("Invalid Postcode")

        # As before, the only remaining error here is that the inward code has an invalid format,
        # we return a detail of this in the error again
        else:
            raise ValueError("Invalid Postcode")
