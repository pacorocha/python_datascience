from array import array
from PIL import Image
import numpy as np


def display_image(array, title):
    img = Image.fromarray(array)
    img.show(title=title)


def ft_invert(array) -> array:
    inverted_array = 255 - array
    title = "inverted"
    display_image(inverted_array, title)

    return array


def ft_red(array) -> array:
    red_array = array.copy()
    red_array[:, :, [1, 2]] = 0
    title = "red"
    display_image(red_array, title)

    return array


def ft_green(array) -> array:
    green_array = array.copy()
    green_array[:, :, [0, 2]] = 0
    title = "green"
    display_image(green_array, title)

    return array


def ft_blue(array) -> array:
    blue_array = array.copy()
    blue_array[:, :, [0, 1]] = 0
    title = "blue"
    display_image(blue_array, title)

    return array


def ft_grey(array) -> array:
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
