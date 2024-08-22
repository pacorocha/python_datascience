from typing import Any


def callLimit(limit: int):
    count = 0
    print("callLimit")
    def callLimiter(function):
        nonlocal count

        print("callLimiter")
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count

            count += 1
            if count > limit:
                print("Function called too many times")
            else:
                return function(*args, **kwds)

        return limit_function

    return callLimiter
