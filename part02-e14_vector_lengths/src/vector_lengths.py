#!/usr/bin/env python3

import numpy as np
#import scipy.linalg


def vector_lengths(a):
    a = a**2
    return np.sqrt(a.sum(axis=1))


def main():
    np.random.seed(0)
    a = np.random.randint(-100, 100, (4, 5))
    print(vector_lengths(a))


if __name__ == "__main__":
    main()
