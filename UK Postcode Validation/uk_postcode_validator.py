from character_validation import CharacterValidator


class UKPostcodeValidation:

    # The first stage of validation is validating the length of the postcode
    # There can only be 5 - 8 characters
    def _validate_postcode_length(self, postcode):
        length = len(postcode)
        if length > 7 or length < 5:
            raise ValueError("Invalid Postcode")
        return True

    # The validate method used by the user - returns True or 'Invalid Postcode'
    def validate(self, postcode):
        postcode = postcode.upper()
        postcode = "".join(postcode.split())
        validate_characters = CharacterValidator(postcode)
        try:
            if self._validate_postcode_length(postcode) and \
                    validate_characters.validate_postcode_entries():
                return True
        except ValueError as err:
            return err

    # The format method returns the postcode in the proper format if valid
    def format(self, postcode):
        postcode = postcode.upper()
        postcode = "".join(postcode.split())
        try:
            if self._validate_postcode_length(postcode) and self.validate(postcode):
                outward_code = postcode[:len(postcode) - 3]
                inward_code = postcode[-3::]
                return outward_code + " " + inward_code
        except ValueError:
            return "Cannot format due to invalid postcode"
