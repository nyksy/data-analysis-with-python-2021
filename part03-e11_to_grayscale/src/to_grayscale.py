#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(kuva):

    # värien painokertoimet
    weights = (0.2126, 0.7152, 0.0722)
    return kuva[:, :, 0] * weights[0] + kuva[:, :, 1] * weights[1] + kuva[:, :, 2] * weights[2]


def to_red(kuva):
    #RGB = (red, green, blue) = (0, 1, 2)
    return kuva * [1, 0, 0]


def to_green(kuva):
    #RGB = (red, green, blue) = (0, 1, 2)
    return kuva * [0, 1, 0]


def to_blue(kuva):
    #RGB = (red, green, blue) = (0, 1, 2)
    return kuva * [0, 0, 1]


def main():
    
    # luetaan kuva
    painting = plt.imread('src/painting.png')
    print(painting.shape)
    
    plt.subplot(3, 1, 1)
    plt.imshow(to_red(painting.copy()))
    plt.subplot(3, 1, 2)
    plt.imshow(to_green(painting.copy()))
    plt.subplot(3, 1, 3)
    plt.imshow(to_blue(painting.copy()))

    # harmaa
    # plt.gray()
    # plt.imshow(to_grayscale(painting))
    plt.show()


if __name__ == "__main__":
    main()
