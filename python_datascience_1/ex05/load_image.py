from PIL import Image
import numpy as np

np.set_printoptions(threshold=1)


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified file path and convert it to a NumPy array.

    This function opens an image file, prints its format and shape, and returns
    the image data as a NumPy array. If the image cannot be loaded, an error
    message is printed.

    Args:
        path (str): The file path to the image.

    Returns:
        np.ndarray: The image data as a NumPy array formatted for the required
        output.

    Raises:
        Exception: If there is an error in loading the image, the exception is
        caught and an error message is printed.
    """
    try:
        with Image.open(path) as img:
            print(f"The format of the image is: {img.format}")

            img_array = np.array(img)

            print(f"The shape of the image is: {img_array.shape}")

            first_row_elements = img_array[0, :3]
            last_row_elements = img_array[-1, -3:]

            print(f"[{first_row_elements}\n    ...\n{last_row_elements}]")

            return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
