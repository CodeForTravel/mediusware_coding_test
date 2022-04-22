import re


def password_complexity_validator(password_value):
    # validate password complexities
    complexities = {
        "UPPER": 1,  # Uppercase
        "LOWER": 1,  # Lowercase
        "LETTERS": 1,  # Either uppercase or lowercase letters
        "DIGITS": 1,  # Digits
        "SPECIAL": 1,  # Not alphanumeric, space or punctuation character
        # Words (alphanumeric sequences separated by a whitespace or punctuation character)
        "WORDS": 1,
    }
    special_characters = ["@", "#", "$", "_", "-", "!"]

    uppercase, lowercase, letters = set(), set(), set()
    digits, special = set(), set()
    contain_space = False

    for character in password_value:
        if character.isupper():
            uppercase.add(character)
            letters.add(character)
        elif character.islower():
            lowercase.add(character)
            letters.add(character)
        elif character.isdigit():
            digits.add(character)
        elif character in special_characters:
            special.add(character)
        elif character.isspace():
            contain_space = True

    words = set(re.findall(r"\b\w+", password_value, re.UNICODE))

    errors = []
    if len(uppercase) < complexities.get("UPPER", 0):
        errors.append(f"{complexities['UPPER']} or more uppercase characters")
    if len(lowercase) < complexities.get("LOWER", 0):
        errors.append(f"{complexities['LOWER']} or more lowercase characters")
    if len(letters) < complexities.get("LETTERS", 0):
        errors.append(f"{complexities['LETTERS']} or more letters")
    if len(digits) < complexities.get("DIGITS", 0):
        errors.append(f"{complexities['DIGITS']} or more digits")
    if len(special) < complexities.get("SPECIAL", 0):
        errors.append(
            f"{complexities['SPECIAL']} or more special characters (@ # $ _ - !)"
        )
    if len(words) < complexities.get("WORDS", 0):
        errors.append(f"{complexities['WORDS']} or more unique words")

    return (errors, contain_space)
