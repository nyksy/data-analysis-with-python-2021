#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def subfigures(a):
    fig, ax = plt.subplots(1, 2)

    # vasemmanpuoleinen plotti
    ax[0].plot(a[:, 0], a[:, 1])

    # oikeanpuoleinen plotti
    ax[1].scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])

    plt.show()


def main():
    subfigures(
        np.array([[1, 1, 0, 100], [2, 4, 20, 150], [3, 1, 40, 230], [4, 2, 80, 50]]))


if __name__ == "__main__":
    main()
