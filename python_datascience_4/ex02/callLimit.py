from typing import Any


def callLimit(limit: int):
    """
    A decorator generator that limits the number of times a function can be
    called.

    Args:
        limit (int): The maximum number of times the decorated function can be
        called.

    Returns:
        Callable: A decorator that, when applied to a function, restricts its
        usage to the specified number of calls. If the function is called more
        than the allowed limit, an error message is printed, and the function
        is not executed for the excess calls.
    """
    count = 0

    def callLimiter(function):
        nonlocal count

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count

            count += 1
            if count > limit:
                print(f"Error: {function} Function called too many times")
            else:
                return function(*args, **kwds)

        return limit_function

    return callLimiter
