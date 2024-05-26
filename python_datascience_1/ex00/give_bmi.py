import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate Body Mass Index (BMI) for a list of heights and weights.

    Args:
    - height (list[int | float]): A list containing heights in meters.
    - weight (list[int | float]): A list containing weights in kilograms.

    Returns:
    - list[int | float]: A list of corresponding BMIs calculated for each pair
    of height and weight.

    Raises:
    - TypeError: If height or weight lists contain non-integer or non-float
    values.
    - ValueError: If height or weight lists are empty or have different
    lengths.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be provided as lists.")
    if not all(isinstance(h, (int, float)) for h in height) or \
       not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("Height and weight must contain only integers or \
floats.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    if len(height) == 0:
        raise ValueError("Height list cannot be empty.")
    if len(weight) == 0:
        raise ValueError("Weight list cannot be empty.")

    np_height = np.array(height)
    np_weight = np.array(weight)
    bmi = np_weight / np_height ** 2
    return list(bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of Body Mass Index (BMI) values.

    Args:
    - bmi (list[int | float]): A list containing BMI values.
    - limit (int): The threshold limit to be applied to the BMI values.

    Returns:
    - list[bool]: A list of boolean values indicating whether each BMI value \
exceeds the limit.

    Raises:
    - TypeError: If bmi is not a list or contains non-integer or non-float \
values.
    - ValueError: If bmi is empty.
    """
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")
    if not all(isinstance(item, (int, float)) for item in bmi):
        raise TypeError("BMI list must contain only integers or floats.")
    if len(bmi) == 0:
        raise ValueError("BMI list cannot be empty.")
    limits = []
    for item in bmi:
        if item > limit:
            limits.append(True)
        else:
            limits.append(False)
    return limits
