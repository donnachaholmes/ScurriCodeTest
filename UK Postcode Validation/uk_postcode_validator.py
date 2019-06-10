from character_validation import CharacterValidator


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
            if self._validate_postcode_length() and \
                    validate_characters.validate_postcode_entries():
                return True
        except ValueError as err:
            return err

    # The format method returns the postcode in the proper format if valid
    def format(self):
        try:
            if self._validate_postcode_length() and self.validate():
                outward_code = self.postcode[:len(self.postcode) - 3]
                inward_code = self.postcode[-3::]
                return outward_code + " " + inward_code
        except ValueError:
            return "Cannot format due to invalid postcode"
