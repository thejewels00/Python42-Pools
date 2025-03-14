from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def ft_load_and_zoom(path: str) -> np.array:
    '''This function loads a picture, prints some information about it, and displays a zoomed version.'''
    try:
        img_array = ft_load(path)
        if img_array is None:
            return
        height, width, _ = img_array.shape
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)
        zoomed_img_array = img_array[height//4:3*height//4, width//4:3*width//4]
        # Convert to grayscale by averaging the RGB channels
        zoomed_img_array_gray = np.mean(zoomed_img_array, axis=2, keepdims=True).astype(np.uint8)
        print(f"New shape after slicing: {zoomed_img_array_gray.shape}")
        print(zoomed_img_array_gray)
        plt.imshow(zoomed_img_array_gray.squeeze(), cmap='gray')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()
        zoomed_img = Image.fromarray(zoomed_img_array_gray.squeeze())
        zoomed_img.save("zoomed_animal.jpeg")
        return zoomed_img_array_gray
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    ft_load_and_zoom("../animal.jpeg")