from UKPostcodeValidator import UKPostcodeValidation
# For the valid codes, I used the examples from the wikipedia page:
# https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom
# and used this generator:https://www.doogal.co.uk/PostcodeGenerator.php
# I also used different cases and spacing to show this is not an issue
valid_postcodes = [
    "B338TH", "W1A 0AX", "M1 1AE", "B33 8TH", "CR2 6XH", "DN55 1PT",
    "W1J7NT", "DE12 8HJ", "SW1A 1AA", "HD7 5UZ", "CH5 3QW", "W2 1JB", "PL7 1RF",
    "JE31EP", "JE23XP", "IM94EB", "im94AJ", "GY79YH", "PR0 9yh", "FK13 6DN", "PE5 7AB",
    "WD17 3EZ", "BB18 5QQ", "nR16 1EE", "CV1 2QZ", "NP4 6GS", "LU1 5LF", "HR3 6LQ", "MK42 9UA",
    "SK1 3PG", "PO13 0HG", "b13 8nl", "EC1Y8JR", "AB42 4XH", "WD99 1AX", "CV11 6PR", "G44 3DA", "EX39 4FW",
    "BS10 6AF", "M15 4BR", "PA46 7RR", "l23 8tq", "SO24 9HG", "AL3 6AY", "OL3 6ED", "CF36 5HY", "HU13 0GN",
    "PA30 8HA", "PO18 0LE", "PE20 3HF", "EH9 1BR", "BS36 2UL", "PL35 0AJ", "BN17 7FX", "HU12 8NT",
    "BB9 6NX", "LA9 6NN", "ME7 1UL", "WD7 8PR", "YO26 8LE", "CF47 9UN", "M8 4GP", "L4 1YE", "L 4 1 Y E  "
]

# Invalid postcodes are based off the validation notes, getting intentionally every one
# wrong to show it does not validate
# I have tried to include cases where all of the notes in the wikipedia page will cause a failure
invalid_postcodes = [
    # Length Val Failures
    "EC1As11s", "Ec1a",
    # Incorrect entries for last three characters
    "W1A AAX", "W1A 01X", "W1A 0A2", "W1A 045", "M1 1AC", "M1 AAE",
    # Incorrect entries  for first two characters
    "A1 1AE", "MA 1A1", "21 AAE",
    # Failures for first, second, third and fourth characters
    "QE12 8HJ", "AI12 8HJ", "W1I 0AX", "SW1C 1AA",
    # Double character areas only valid for single or double digit districts
    "BR11 1AA", "LL1B 1AA", "LL2 1AA",
    # Invalid areas with district 0
    "BT0 1AA", "L4 oneYE"
    # Number errors
    "1a4B1ye", '123456',
    # Letter errors
    "asdfg", "aa",
]

# Now we just loop through everything and give the responses
for postcode in valid_postcodes:
    check_postcode = UKPostcodeValidation(postcode)
    if check_postcode.validate():
        print str(check_postcode.format()) + " - " + str(check_postcode.validate()) + "\n"
    else:
        print postcode + " - " + check_postcode.validate() + "\n"

for postcode in invalid_postcodes:
    check_postcode = UKPostcodeValidation(postcode)
    if check_postcode.validate() == True:
        print str(check_postcode.format()) + " - " + str(check_postcode.validate()) + "\n"
    else:
        print postcode + " - " + str(check_postcode.validate()) + "\n"

messy_postcodes = ["A l 36 A y", "L 4 1 Y E  ", "po 1 8 0 Le", "146 oneYE"]

for mess in messy_postcodes:
    format_postcode = UKPostcodeValidation(mess)
    print format_postcode.format()
