def square(x: int | float) -> int | float:
    """
    Calculate the square of a given number.

    Args:
        x (int | float): The number to be squared.

    Returns:
        int | float: The square of the input number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Calculate the exponentiation of a given number by itself.

    Args:
        x (int | float): The base number.

    Returns:
        int | float: The result of raising the base number to the power of
        itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a callable object that applies a given function to an initial
    number.
    The function is applied iteratively, updating the initial number with each
    call.

    Args:
        x (int | float): The initial number.
        function (callable): The function to apply to the number. It must
        accept a single argument of type int or float and return a result of
        the same type.

    Returns:
        object: A callable object that applies the given function to the number
        and returns the updated result on each call.
    """
    count = 0

    def inner() -> float:
        """
        Applies the function to the current value of x, updates x with the
        result, and increments the call counter.

        Returns:
            float: The result of applying the function to the current value of
            x.
        """
        nonlocal count, x
        count += 1
        x = function(x)
        return x
    return inner
