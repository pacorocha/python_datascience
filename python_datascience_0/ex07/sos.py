import sys


def main(argv):
    try:
        assert len(argv) == 2, "AssertionError: the arguments are bad"
    except AssertionError as msg:
        sys.exit(msg)
    try:
        assert check_string(argv[1]), "AssertionError: the arguments are bad"
    except AssertionError as msg:
        sys.exit(msg)
    encoded_string = encode_morse(argv[1])
    print(encoded_string)


def check_string(string):
    return all(c.isalnum() for c in string)


NESTED_MORSE = {
    " ": "/ ",
    "a": ".- ",
    "b": "-... ",
    "c": "-.-. ",
    "d": "-.. ",
    "e": ". ",
    "f": "..-. ",
    "g": "--. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..- ",
    "y": "-.--",
    "z": "--.. ",
    "1": ".--- ",
    "2": "..--- ",
    "3": "...--- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "10": "----- "
}


def encode_morse(string):
    '''Returns a string converted into morse code.'''
    encoded_string = ""
    for c in string.lower():
        encoded_string += NESTED_MORSE[c]
    return encoded_string[:-1]


if __name__ == "__main__":
    main(sys.argv)
