import sys

try:
    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
except AssertionError as msg:
    print(msg)
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)

if n % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
