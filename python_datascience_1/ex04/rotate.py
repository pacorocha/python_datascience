import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from load_image import ft_load


def zoom(img) -> Image:
    """
    Crops and converts a specified region of an image to grayscale.

    This function takes an input image, crops a region specified by the
    bounding box (460, 90, 860, 490), and converts this cropped region
    to grayscale. The resulting image is then returned.

    Parameters:
    img (Image): The input image to be processed. This should be an instance
                 of the PIL Image class.

    Returns:
    Image: The processed image, cropped to the specified region and converted
           to grayscale.
    """
    box = (460, 90, 860, 490)
    region = img.crop(box)
    new_img = region.convert("L")

    return new_img


def display_image(img):
    """
    Displays an image using matplotlib.

    This function takes an image as input and displays it using
    matplotlib's imshow function. The image is displayed in grayscale
    with the origin set to the upper left corner.

    Parameters:
    img (ndarray or Image): The input image to be displayed. This can be
                            a NumPy array or a PIL Image object.

    Returns:
    None
    """
    fig, ax = plt.subplots()
    ax.imshow(img, cmap='gray', origin='upper')
    plt.show()


def main():

    original_img = Image.open("animal.jpeg")
    original_img_array = ft_load(original_img)

    print(f"The shape of the image is: {original_img_array.shape}")
    fst_row_els = original_img_array[0, :3]
    last_row_els = original_img_array[-1, -3:]

    print(f"[[{fst_row_els[0]}\n{fst_row_els[1]}\n{fst_row_els[2]}\n     ...")
    print(f"{last_row_els[0]}\n{last_row_els[1]}\n{last_row_els[2]}]]")

    new_img = zoom(original_img)
    new_img_array = ft_load(new_img)
    rotated_img = np.array([
            [new_img_array[j][i]
                for j in range(len(new_img_array))]
            for i in range(len(new_img_array[0]))
        ])

    print(f"The shape after Transpose: {rotated_img.shape}")

    fst_row_els = rotated_img[0]
    last_row_els = rotated_img[-1]

    print(f"[{fst_row_els}\n  ...")
    print(f" [{last_row_els}")

    display_image(rotated_img)


if __name__ == "__main__":
    main()
