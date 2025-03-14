import numpy as np
from load_image import ft_load
from PIL import Image


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    return 255 - array


def ft_red(array) -> np.array:
    """
    Applies a red filter to the image received.
    """
    red_array = array.copy()
    red_array[:, :, 1] = 0  # Set green channel to 0
    red_array[:, :, 2] = 0  # Set blue channel to 0
    return red_array


def ft_green(array) -> np.array:
    """
    Applies a green filter to the image received.
    """
    green_array = array.copy()
    green_array[:, :, 0] = 0  # Set red channel to 0
    green_array[:, :, 2] = 0  # Set blue channel to 0
    return green_array


def ft_blue(array) -> np.array:
    """
    Applies a blue filter to the image received.
    """
    blue_array = array.copy()
    blue_array[:, :, 0] = 0  # Set red channel to 0
    blue_array[:, :, 1] = 0  # Set green channel to 0
    return blue_array


def ft_grey(array) -> np.array:
    """
    Converts the image to grayscale.
    """
    grey_array = np.mean(array, axis=2, keepdims=True).astype(np.uint8)
    return np.repeat(grey_array, 3, axis=2)


def save_image(title, image):
    img = Image.fromarray(image)
    img.save(f"{title}.jpeg") 


if __name__ == "__main__":
    array = ft_load("../landscape.jpg")

    # Apply filters
    inverted_array = ft_invert(array)
    red_array = ft_red(array)
    green_array = ft_green(array)
    blue_array = ft_blue(array)
    grey_array = ft_grey(array)

    # Save the results
    save_image("Original", array)
    save_image("Inverted", inverted_array)
    save_image("Red_Filter", red_array)
    save_image("Green_Filter", green_array)
    save_image("Blue_Filter", blue_array)
    save_image("Grey_Filter", grey_array)
