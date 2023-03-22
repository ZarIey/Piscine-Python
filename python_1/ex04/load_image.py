import sys as check
import imageio
import numpy as py
# import matplotlib.pyplot as plt


def ft_load(path: str) -> py.array:
    '''load an image by giving him the path'''
    try:
        image = imageio.imread(path)
        # print("The shape of image is:", image.shape)
        # plt.imshow(image)
        # plt.show()
        py_image = py.array(image)
        print(py_image)
        return py_image
    except FileNotFoundError:
        print("Error: Something went wrong with the image")
        check.exit()
    except PermissionError:
        print("Permission Error")
        check.exit()
    except ValueError:
        print("Value Error BREEEF 👉😩")
        check.exit()


def zoom(path: str) -> py.array:
    py_image = ft_load(path)
    slice_object = (slice(100, 500), slice(450, 850))
    py_image = py.dot(py_image[..., :3], [0.2989, 0.5870, 0.1140])
    py_image = py_image[slice_object]
    print_image = py.array(py_image)
    print("The shape of image is:", py_image.shape)
    # print("New shape after slicing:", py_image.shape)
    print(print_image)
    # plt.imshow(py_image, cmap='gray')
    # plt.show()
    return (print_image)
