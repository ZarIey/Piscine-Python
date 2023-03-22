from load_image import zoom
import numpy as np
import sys as check
import matplotlib.pyplot as plt
from scipy import ndimage


def rotate():
    '''rotate the image and flip it'''
    img = np.flipud(zoom("~/Downloads/animal.jpeg"))
    rotated_img = ndimage.rotate(img, -90)
    print("New shape after Transpose:", rotated_img.shape)
    print(rotated_img)
    plt.imshow(rotated_img, cmap=plt.cm.gray)
    plt.show()


def main():
    rotate()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program stop")
        check.exit()
    except ValueError:
        print("Error: Value error")
