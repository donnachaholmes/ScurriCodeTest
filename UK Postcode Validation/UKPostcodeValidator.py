from CharacterValidation import CharacterValidator


class UKPostcodeValidation:
    # We normalise the data by putting it in the upper case
    # format and remove any whitespace for data processing
    def __init__(self, postcode):
        self.postcode = postcode.upper()
        self.postcode = "".join(self.postcode.split())

    # The first stage of validation is validating the length of the postcode
    # There can only be 5 - 8 characters
    def _validate_postcode_length(self):
        length = len(self.postcode)
        if length > 7 or length < 5:
            raise ValueError("Invalid Postcode")
        return True

    # The validate method used by the user - returns True or 'Invalid Postcode'
    def validate(self):
        validate_characters = CharacterValidator(self.postcode)
        try:
            if self._validate_postcode_length() \
                    and validate_characters.validate_postcode_entries():
                return True
        except ValueError as err:
            return err

    # The format method returns the postcode in the proper format if valid
    def format(self):
        try:
            if self._validate_postcode_length() \
                    and self.validate():
                postcode_list = list(self.postcode)
                postcode_area_and_district_list = postcode_list[:len(postcode_list) - 3]
                postcode_sector_and_unit_list = postcode_list[len(postcode_list):len(postcode_list) - 4:-1]
                postcode_sector_and_unit_list = postcode_sector_and_unit_list[::-1]
                postcode_area_and_district = "".join(postcode_area_and_district_list)
                postcode_sector_and_unit = "".join(postcode_sector_and_unit_list)
                return postcode_area_and_district + " " + postcode_sector_and_unit
        except ValueError:
            return "Cannot format due to invalid postcode"
