from array import array
from PIL import Image
import numpy as np


def display_image(array, title):
    """
    Display an image from a numpy array.

    Parameters:
    array (numpy.ndarray): The array representing the image to be displayed.
    title (str): The title of the image window.
    """
    img = Image.fromarray(array)
    img.show(title=title)


def ft_invert(array) -> array:
    """
    Invert the colors of an image represented by a numpy array and display it.

    Parameters:
    array (numpy.ndarray): The array representing the image to be inverted.

    Returns:
    array: The original array.
    """
    inverted_array = 255 - array
    title = "inverted"
    display_image(inverted_array, title)

    return array


def ft_red(array) -> array:
    """
    Display the image with only the red channel.

    Parameters:
    array (numpy.ndarray): The array representing the image.

    Returns:
    array: The original array.
    """
    red_array = array.copy()
    red_array[:, :, [1, 2]] = 0
    title = "red"
    display_image(red_array, title)

    return array


def ft_green(array) -> array:
    """
    Display the image with only the green channel.

    Parameters:
    array (numpy.ndarray): The array representing the image.

    Returns:
    array: The original array.
    """
    green_array = array.copy()
    green_array[:, :, [0, 2]] = 0
    title = "green"
    display_image(green_array, title)

    return array


def ft_blue(array) -> array:
    """
    Display the image with only the blue channel.

    Parameters:
    array (numpy.ndarray): The array representing the image.

    Returns:
    array: The original array.
    """
    blue_array = array.copy()
    blue_array[:, :, [0, 1]] = 0
    title = "blue"
    display_image(blue_array, title)

    return array


def ft_grey(array) -> array:
    """
    Convert the image to grayscale and display it.

    Parameters:
    array (numpy.ndarray): The array representing the image.

    Returns:
    array: The original array.
    """
    grey_array = array.copy()
    grey_value1 = grey_array[:, :, 0] / 3
    grey_value2 = grey_array[:, :, 1] / 3
    grey_value3 = grey_array[:, :, 2] / 3
    grey = (grey_value1 + grey_value2 + grey_value3).astype(np.uint8)
    grey_array[:, :, 0] = grey
    grey_array[:, :, 1] = grey
    grey_array[:, :, 2] = grey

    title = "grey"
    display_image(grey_array, title)

    return array
