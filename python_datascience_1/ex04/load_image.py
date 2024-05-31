import numpy as np

from PIL import Image

np.set_printoptions(threshold=1)


def ft_load(img: Image) -> np.ndarray:
    """
    Load an image from the specified file path and convert it to a NumPy array.

    This function opens an image file, prints its format and shape, and returns
    the image data as a NumPy array. If the image cannot be loaded, an error
    message is printed.

    Args:
        path (str): The file path to the image.

    Returns:
        np.ndarray: The image data as a NumPy array.

    Raises:
        Exception: If there is an error in loading the image, the exception is
        caught and an error message is printed.
    """
    try:
        img_array = np.array(img)
        return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
