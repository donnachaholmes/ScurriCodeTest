from CharacterValidation import CharacterValidator


class UKPostcodeValidation:
    # When creating an instance of the class, a single postcode of the string type is expected
    # We normalise the data by putting it in the upper case format and remove any whitespace for data processing

    def __init__(self, postcode):
        self.postcode = postcode.upper()
        self.postcode = "".join(self.postcode.split())

    # The first stage of validation is validating the length of the postcode
    # When there is no whitespace, the postcode can only be between 5 and 8 characters
    # If it is not this length, we return an applicable error message
    # this is a private method

    def _validate_postcode_length(self):
        length = len(self.postcode)
        if length > 7 or length < 5:
            raise ValueError("Invalid Postcode")
        return True

    # The second stage of validation is checking the data within the postcode to be valid
    # There are 2 main parts of the postcode - Outward and inward code
    # For analysis, we create an instance of the character validator with both the full postcode and
    # the inward code (area and district) in list form
    # The inward code (part before the space) can have a length of 3, 4 or 5,
    # We use different methods to validate the inward code based on the length of the inward code

    def _validate_postcode_entries(self):
        postcode_list = list(self.postcode)
        area_and_district = postcode_list[:len(postcode_list) - 3]
        validate_characters = CharacterValidator(area_and_district, postcode_list)

        if len(area_and_district) == 2:
            return validate_characters.two_character_postcode_area_and_district_validation()
        elif len(area_and_district) == 3:
            return validate_characters.three_character_postcode_area_and_district_validation()
        else:
            return validate_characters.four_character_postcode_area_and_district_validation()

    # Code validation returns either True or an error code detailing the error
    # If the length and character both validate (from above) we return True, otherwise we return the error message

    def validate(self):
        try:
            if self._validate_postcode_length() and self._validate_postcode_entries():
                return True
        except ValueError as err:
            return err

    # We also have a format method, where we return the expected format of a postcode as a string if it is a valid code
    # We return in the format of Outward Code (space) Inward Code all uppercase
    # The idea is that we check if it is valid, then manipulate the data to be in the correct format
    # An invalid postcode will not be formatted and we return the reason for this as an error message

    def format(self):
        try:
            if self._validate_postcode_length() and self._validate_postcode_entries():
                postcode_list = list(self.postcode)
                postcode_area_and_district_list = postcode_list[:len(postcode_list) - 3]
                postcode_sector_and_unit_list = postcode_list[len(postcode_list):len(postcode_list) - 4:-1]
                postcode_sector_and_unit_list = postcode_sector_and_unit_list[::-1]
                postcode_area_and_district = "".join(postcode_area_and_district_list)
                postcode_sector_and_unit = "".join(postcode_sector_and_unit_list)
                return postcode_area_and_district + " " + postcode_sector_and_unit
        except ValueError as err:
            return "Cannot format due to {}".format(err)
