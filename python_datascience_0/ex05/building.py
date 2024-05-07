import sys


def main(input):

    try:
        string = input[1]
    except IndexError:
        try:
            string = prompt_input()
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            sys.exit(1)
    else:
        try:
            assert len(input) == 2, "more than one argument is provided"
        except AssertionError as msg:
            sys.exit(msg)

    print("The text contains", total_chars(string), "characters:")
    print(sum_uppercase(string), "upper letters")
    print(sum_lowercase(string), "punctuation marks")
    print(sum_spaces(string), "spaces")
    print(sum_digits(string), "digits")


def prompt_input():
    return input("""What is the text to count?
""")


def total_chars(input):
    """Sums all charatcers in a string

    Parameters:
    input (str): String entered by user

    Returns:
    int:Total characters

    """
    total_chars = [char for char in input]
    return len(total_chars)


def sum_uppercase(input):
    """Sums uppercase characters in a string

    Parameters:
    input (str): String entered by user

    Returns:
    int:Total uppercase characters

   """
    total_uppercase = [char for char in input if char.isupper()]
    return len(total_uppercase)


def sum_lowercase(input):
    """Sums lowercase characters in a string

    Parameters:
    input (str): String entered by user

    Returns:
    int:Total lowercase characters

   """
    total_lowercase = [char for char in input if char.islower()]
    return len(total_lowercase)


def sum_punctuation_marks(input):
    """Sums punctuation mark characters in a string

    Parameters:
    input (str): String entered by user

    Returns:
    int:Total punctuation mark characters

   """
    count = 0
    chars = ('!', ",", "\'", ";", "\"", ".", "-", "?")
    for c in range(0, len(input)):
        if input[c] in chars:
            count = count + 1

    return count


def sum_digits(input):
    """Sums digit characters in a string

    Parameters:
    input (str): String entered by user

    Returns:
    int:Total digit characters

   """
    total_digits = [char for char in input if char.isdigit()]
    return len(total_digits)


def sum_spaces(input):
    """Sums space characters in a string

    Parameters:
    input (str): String entered by user

    Returns:
    int:Total space characters

   """
    total_spaces = [char for char in input if char.isspace()]

    return len(total_spaces)


if __name__ == "__main__":
    main(sys.argv)
