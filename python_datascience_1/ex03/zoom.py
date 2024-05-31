import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from load_image import ft_load


def zoom(img) -> Image:
    box = (460, 90, 860, 490)
    region = img.crop(box)
    new_img = region.convert("L")

    return new_img


def display_image(img):
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

    new_shape = f"{new_img.width}, {new_img.height}, {len(new_img.getbands())}"
    print(f"The shape after slicing: ({new_shape}) or {new_img_array.shape}")

    fst_row_els = new_img_array[0, :3]
    last_row_els = new_img_array[-1, -3:]

    print(f"[[[{fst_row_els[0]}]\n  [{fst_row_els[1]}]\n  [{fst_row_els[2]}]\n  ...")
    print(f"  [{last_row_els[0]}]\n  [{last_row_els[1]}]\n  [{last_row_els[2]}]]]")

    display_image(new_img)


if __name__ == "__main__":
    main()
