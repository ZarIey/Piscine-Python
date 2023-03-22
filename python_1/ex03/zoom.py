import sys as check
import numpy as py
import matplotlib.pyplot as plt

from load_image import ft_load


def zoom():
    '''zoom in the image and convert it to black and white'''
    py_image = ft_load("~/Downloads/animal.jpeg")
    slice_object = (slice(100, 500), slice(450, 850))
    py_image = py.dot(py_image[..., :3], [0.2989, 0.5870, 0.1140])
    py_image = py_image[slice_object]
    print_image = py.array(py_image)
    print("New shape after slicing:", py_image.shape)
    print(print_image)
    plt.imshow(py_image, cmap='gray')
    plt.show()


def main():
    zoom()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program stop")
        check.exit()
    except ValueError:
        print("Error: Value error")
