class calculator:
    """
    A simple calculator class to perform basic arithmetic operations on a list of numeric components.

    Attributes:
    -----------
    components : list
        A list of numeric values on which the arithmetic operations will be performed.

    Methods:
    --------
    __add__(other):
        Adds a numeric value or another list of numeric values to each component in the list.

    __mul__(other):
        Multiplies each component in the list by a numeric value or another list of numeric values.

    __sub__(other):
        Subtracts a numeric value or another list of numeric values from each component in the list.

    __truediv__(other):
        Divides each component in the list by a numeric value or another list of numeric values.
        Division by zero will return infinity for the corresponding component.
    """
    def __init__(self, components) -> None:
        self.components = components

    def __add__(self, other) -> None:
        result = [x + other for x in self.components]
        print(result)

    def __mul__(self, other) -> None:
        result = [x * other for x in self.components]
        print(result)

    def __sub__(self, other) -> None:
        result = [x - other for x in self.components]
        print(result)

    def __truediv__(self, other) -> None:
        result = [x / other if other != 0 else float('inf') for x in self.components]
        print(result)
