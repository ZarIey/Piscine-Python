import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.array) -> np.array:
    '''Inverts the color of the image received.'''
    image = np.invert(array)
    plt.imshow(image)
    plt.show()
    return image


def ft_red(array: np.array) -> np.array:
    ''' Make the image red only'''
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    plt.imshow(red)
    plt.show()


def ft_green(array: np.array) -> np.array:
    ''' Make the image green only'''
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    plt.imshow(green)
    plt.show()


def ft_blue(array: np.array) -> np.array:
    ''' Make the image blue only'''
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(blue)
    plt.show()


def ft_grey(array: np.array) -> np.array:
    ''' Make the image grey and white only'''
    new_image = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    plt.imshow(new_image, cmap='gray')
    plt.show()
