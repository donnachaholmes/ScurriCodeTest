from uk_postcode_validator import UKPostcodeValidation


# We first test valid and invalid outward codes
def test_valid_two_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert check_postcode.validate("M1 1AE") is True


# The invalid data contain invalid data in postions and invalid patterns
def test_invalid_two_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("A1 1AE")) == "Invalid Postcode"
    assert str(check_postcode.validate("MA 1A1")) == "Invalid Postcode"
    assert str(check_postcode.validate("21 AAE")) == "Invalid Postcode"


def test_valid_three_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert check_postcode.validate("W1A 0AX") is True
    assert check_postcode.validate("B33 8TH") is True
    assert check_postcode.validate("CR2 6XH") is True
    assert check_postcode.validate("BL0 1AA") is True


# The first 2 test below fail because only certain areas BT can have a 0
# district and certain areas can only have a double digit district - these
# areas do not qualify.
def test_invalid_three_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("AB2 6XH")) == "Invalid Postcode"
    assert str(check_postcode.validate("BT0 1AA")) == "Invalid Postcode"
    assert str(check_postcode.validate("AAA 8TH")) == "Invalid Postcode"
    assert str(check_postcode.validate("123 8TH")) == "Invalid Postcode"
    assert str(check_postcode.validate("2AA 8TH")) == "Invalid Postcode"


def test_valid_four_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert check_postcode.validate("BB18 5QQ") is True
    assert check_postcode.validate("SW1A 1AA") is True


# The first 2 test below fail because some areas can only have a double
# digit district and some areas can only have single digit districts
def test_invalid_four_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("BR11 1AA")) == "Invalid Postcode"
    assert str(check_postcode.validate("LL1B 1AA")) == "Invalid Postcode"
    assert str(check_postcode.validate("LLAB 1AA")) == "Invalid Postcode"
    assert str(check_postcode.validate("1234 1AA")) == "Invalid Postcode"
    assert str(check_postcode.validate("L2F3 1AA")) == "Invalid Postcode"


def test_invalid_inward_code():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("W1A AAX")) == "Invalid Postcode"
    assert str(check_postcode.validate("W1A 01X")) == "Invalid Postcode"
    assert str(check_postcode.validate("M1 1AC")) == "Invalid Postcode"
    assert str(check_postcode.validate("M1 1IA")) == "Invalid Postcode"


# Tests for invald letters in the first four postcode positions
def test_invalid_outward_letter_entries():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("QE12 8HJ")) == "Invalid Postcode"
    assert str(check_postcode.validate("AI12 8HJ")) == "Invalid Postcode"
    assert str(check_postcode.validate("W1I 0AX")) == "Invalid Postcode"
    assert str(check_postcode.validate("SW1C 1AA")) == "Invalid Postcode"


def test_invalid_postcode_length():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("EC1As11s")) == "Invalid Postcode"
    assert str(check_postcode.validate("Ec1a")) == "Invalid Postcode"


def test_white_space_in_postcode():
    check_postcode = UKPostcodeValidation()
    assert check_postcode.validate("M8      4GP") is True
    assert check_postcode.validate("L4 1YE") is True
    assert check_postcode.validate("L 4 1 Y E  ") is True


def test_valid_postcode_format_function():
    format_postcode = UKPostcodeValidation()
    assert format_postcode.format("A l 36 A y") == "AL3 6AY"
    assert format_postcode.format("po 1 8 0 Le") == "PO18 0LE"


def test_invalid_postcode_format_function():
    format_postcode = UKPostcodeValidation()
    assert format_postcode.format("146 oneYE") \
        == "Cannot format due to invalid postcode"
