import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a given list and returns the sliced portion while printing the shape
    of the original and new lists.

    Parameters:
    family (list): The list to be sliced.
    start (int): The starting index for the slice (inclusive).
    end (int): The ending index for the slice (exclusive).

    Returns:
    list: The sliced portion of the list.
    """
    if not isinstance(family, list):
        raise TypeError("family must be a list.")

    if not family:
        raise ValueError("The family list is empty.")

    if not all(isinstance(element, list) for element in family):
        raise TypeError("family must contain only lists.")

    first_len = len(family[0])
    if not all(len(member) == first_len for member in family):
        raise ValueError("Not all lists in family have the same size.")

    shape = [len(family), first_len]
    print("My shape is: ", shape)

    new_family = family[start:end]

    new_shape = [len(new_family), len(np.array(family[0])) if family else 0]
    print("My new shape is: ", new_shape)

    return new_family
