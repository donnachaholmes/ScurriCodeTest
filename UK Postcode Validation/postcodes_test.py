from uk_postcode_validator import UKPostcodeValidation


def test_valid_two_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert check_postcode.validate("M1 1AE") is True


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


def test_invalid_three_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("AB2 6XH")) == "Invalid Postcode"
    assert str(check_postcode.validate("BT0 1AA")) == "Invalid Postcode"


def test_valid_four_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert check_postcode.validate("BB18 5QQ") is True
    assert check_postcode.validate("SW1A 1AA") is True


def test_invalid_four_character_outward_code():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("BR11 1AA")) == "Invalid Postcode"
    assert str(check_postcode.validate("LL1B 1AA")) == "Invalid Postcode"


def test_invalid_inward_code():
    check_postcode = UKPostcodeValidation()
    assert str(check_postcode.validate("W1A AAX")) == "Invalid Postcode"
    assert str(check_postcode.validate("W1A 01X")) == "Invalid Postcode"
    assert str(check_postcode.validate("M1 1AC")) == "Invalid Postcode"
    assert str(check_postcode.validate("M1 1IA")) == "Invalid Postcode"


def test_invalid_inward_letter_entries():
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
