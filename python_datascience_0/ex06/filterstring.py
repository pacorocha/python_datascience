import sys


def main(argv):
    try:
        assert len(argv) == 3, "AssertionError: the arguments are bad"
    except AssertionError as msg:
        sys.exit(msg)
    filtered_words = filter_by_word_length(argv[1], int(argv[2]))
    print(filtered_words)


def filter_by_word_length(s, n):
    words = s.split()
    return [word for word in words if (lambda x: len(x) > n)(word)]


if __name__ == "__main__":
    main(sys.argv)
