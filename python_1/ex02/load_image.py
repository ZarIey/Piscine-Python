import sys as check
import imageio
import numpy as py


def ft_load(path: str) -> py.array:
    '''load an image by giving him the path'''
    try:
        image = imageio.imread(path)
        print("The shape of image is:", image.shape)
        py_image = py.array(image)
        print(py_image)
        return py_image
    except OSError:
        print("Error: dont play with me...........")
        check.exit()
    except FileNotFoundError:
        print("Error: Something went wrong with the image")
        check.exit()
    except PermissionError:
        print("Permission Error")
        check.exit()
    except ValueError:
        print("Value Error BREEEF 👉😩")
        check.exit()
