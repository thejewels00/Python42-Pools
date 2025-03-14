from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def cut_and_transpose_image(path: str):
    '''This function cuts a square part from the image, transposes it,
    and displays the result'''
    try:
        img_array = ft_load(path)
        if img_array is None:
            return
        height, width, _ = img_array.shape
        square_img_array = img_array[height//4:3*height//4, width//4:3*width//4]
        # Convert to grayscale by averaging the RGB channels
        square_img_array_gray = np.mean(square_img_array, axis=2,
                                        keepdims=True).astype(np.uint8)
        print(f"The shape of the square image is: {square_img_array_gray.shape}")
        print(square_img_array_gray)
        transposed_img_array = np.zeros((square_img_array_gray.shape[1],
                                         square_img_array_gray.shape[0]),
                                        dtype=square_img_array_gray.dtype)
        for i in range(square_img_array_gray.shape[0]):
            for j in range(square_img_array_gray.shape[1]):
                transposed_img_array[j, i] = square_img_array_gray[i, j].item()
        print(f"New shape after Transpose: {transposed_img_array.shape}")
        print(transposed_img_array)  
        # Display the transposed image
        plt.imshow(transposed_img_array, cmap='gray')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.show()    
        # Save the transposed image to a file
        transposed_img = Image.fromarray(transposed_img_array)
        transposed_img.save("transposed_animal.jpeg")   
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    cut_and_transpose_image("../animal.jpeg")