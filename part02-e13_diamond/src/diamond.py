#!/usr/bin/env python3

import numpy as np


def diamond(n):

    if n == 1:
        return np.array([[1]])

    tr = np.eye(n, dtype=int)
    tl = np.eye(n, dtype=int)[:, ::-1]

    # luodaan vasen ja oikea "puoli" timantista
    right = np.concatenate((tr, tl[1:]))
    left = np.concatenate((tl, tr[1:]))

    # poistetaan vasemmalta puolelta viimeinen kolumni
    left = np.delete(left, n-1, axis=1)

    # yhdistetään ja palautetaan taulukot
    return np.concatenate((left, right), axis=1)


def main():
    print(diamond(3))
    print(diamond(1))


if __name__ == "__main__":
    main()
