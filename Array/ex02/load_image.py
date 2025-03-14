from PIL import Image
import numpy as np
import matplotlib as plt

def ft_load(path: str) -> np.array:
    '''this function jsut load a picture and print some information about it'''
    try:
        with Image.open(path) as img:
            if img.format not in ['JPEG', 'JPG']:
                raise ValueError("Unsupported image format. Only JPG and JPEG are supported.")
            print(f"Image format: {img.format}")
            img = img.convert('RGB')
            img_array = np.array(img)
            print(f"The shape of image is: {img_array.shape}")
            print(img_array)
            return img_array
    except Exception as e:
        print(f"Error: {e}")
        return None


# if __name__ == "__main__":
#     print(ft_load("landscape.jpg"))
