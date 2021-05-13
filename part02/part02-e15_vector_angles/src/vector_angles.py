#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X, Y):

    # lasketaan inner product, sekä vektorien pituudet ko kö (?)
    inner_product = np.sum(X*Y, axis=1)

    length_x = np.sum(np.square(X), axis=1)
    length_y = np.sum(np.square(Y), axis=1)

    return np.degrees(
        np.arccos(
            np.clip(inner_product / (np.sqrt(length_x)*np.sqrt(length_y)), -1, 1)))


def main():
    print(vector_angles(
        np.array([[1, 4, 3, 7], [0, 2, 2, 1]]),
        np.array([[1, 4, 3, 7], [0, 2, 2, 1]]))
    )


if __name__ == "__main__":
    main()
