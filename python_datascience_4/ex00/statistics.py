from typing import Any, List


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Computes and prints statistical values such as mean, median, or quartile
    based on the provided arguments and keyword arguments.

    Args:
        *args (Any): A series of numeric values to be analyzed.
        **kwargs (Any): Keyword arguments indicating the statistic to
            calculate. Supported values: "mean", "median", "quartile".

    Raises:
        TypeError: If the inputs are not numeric.
        Exception: For any other unexpected errors.
    """
    try:
        args_list = sorted(args)
        args_sum = sum(args_list)
        args_len = len(args_list)

        functions = {
            "mean": lambda: mean(args_sum, args_len),
            "median": lambda: median(args_list),
            "quartile": lambda: quartile(args_list),
            "var": lambda: variance(args_list, args_sum, args_len),
            "std": lambda: standard_deviation(args_list, args_sum, args_len)
        }
        for key, value in kwargs.items():
            if value in functions:
                result = functions[value]()
                if result is not None:
                    print(f'{value}: {result}')

    except TypeError as e:
        print("ERROR: Invalid input, expected numeric values. ", e)

    except Exception as e:
        print("ERROR: ", e)


def mean(args_sum: float, args_len: int) -> float:
    """
    Calculates and returns the mean (average) of the provided values.

    Args:
        args_sum (float): The sum of all the numeric values.
        args_len (int): The number of numeric values.

    Returns:
        float: The mean value.

    Raises:
        ZeroDivisionError: If the number of elements is zero.
    """
    try:
        return args_sum / args_len
    except ZeroDivisionError as e:
        print("ERROR Cannot calculate mean of zero elements. ", e)
        return None


def median(args_list: List[float]) -> int | float:
    """
    Calculates and returns the median of the provided values.

    Args:
        args_list (List[float]): A sorted list of numeric values.

    Returns:
        int or float: The median value.

    Raises:
        IndexError: If the list is empty.
    """
    try:
        median_value = len(args_list) // 2
        return args_list[median_value]
    except IndexError as e:
        print("ERROR Cannot calculate median of an empty list.", e)
        return None


def quartile(args_list: List[float]) -> List[float]:
    """
    Calculates and returns the first and third quartiles of the provided
    values.

    Args:
        args_list (List[float]): A sorted list of numeric values.

    Returns:
        List[float]: A list containing the first and third quartile values.

    Raises:
        IndexError: If the list is empty.
    """
    try:
        first_quartile = len(args_list) // 4
        second_quartile = len(args_list) * 3 // 4
        first_value = float(args_list[first_quartile])
        second_value = float(args_list[second_quartile])
        return [first_value, second_value]
    except IndexError as e:
        print("ERROR  Cannot calculate quartiles of an empty list.", e)
        return None


def variance(args_list: List[float], args_sum: float, args_len: int) -> float:
    """
    Calculates and returns the variance of the provided values.

    Args:
        args_list (List[float]): A sorted list of numeric values.
        args_sum (float): The sum of all the numeric values.
        args_len (int): The number of numeric values.

    Returns:
        float: The variance value.

    Raises:
        IndexError: If the list is empty.
    """
    try:
        mean_value = mean(args_sum, args_len)
        return sum((x - mean_value) ** 2 for x in args_list) / args_len
    except ZeroDivisionError:
        print("ERROR: Cannot calculate variance of zero elements.")
        return None


def standard_deviation(
        args_list: List[float],
        args_sum: float,
        args_len: int) -> float:
    """
    Calculates and returns the standard deviation of the provided numeric
    values.

    Args:
        args_list (List[float]): A sorted list of numeric values.
        args_sum (float): The sum of all the numeric values.
        args_len (int): The number of numeric values.

    Returns:
        float: The standard deviation of the numeric values.

    Raises:
        Exception: For any unexpected errors that occur during calculation.

    Notes:
        - The standard deviation is calculated as the square root of the
        variance.
        - This function relies on the `variance` function to compute the
        variance of the provided values.
        - If the variance calculation fails, an exception will be raised.
    """
    try:
        var_value = variance(args_list, args_sum, args_len)
        if var_value is not None:
            return var_value ** 0.5
        else:
            raise ValueError("Variance calculation failed, cannot compute \
standard deviation.")
    except Exception as e:
        print("ERROR: ", e)
        return None
