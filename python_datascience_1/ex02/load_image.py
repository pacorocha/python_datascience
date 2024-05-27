from PIL import Image
import numpy as np

np.set_printoptions(threshold=1)


def ft_load(path: str) -> np.ndarray:
    try:
        with Image.open(path) as img:
            print(f"The format of the image is: {img.format}")

            img = img.convert("RGB")

            img_array = np.array(img)

            print(f"The shape of the image is: {img_array.shape}")

            return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
