#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def main():

    # 1
    plt.plot(
        # x-akseli
        np.array([2, 4, 6, 7]),
        # y-akseli
        np.array([4, 3, 5, 1])
    )

    # 2
    plt.plot(
        # x-akseli
        np.array([1, 2, 3, 4]),
        # y-akseli
        np.array([4, 2, 3, 1])
    )

    # labelit ja title
    plt.title('title')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    plt.show()


if __name__ == "__main__":
    main()
