#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    return (((a.shape[0] - 1) / 2), (a.shape[1] - 1) / 2)


def radial_distance(a):

    # kuvaa vastaava taulu, mutta täynnä nollia (float)
    dist_table = np.full((a.shape[0], a.shape[1]), 0.0)
    print(dist_table.shape)

    # keskipisteen sijainti muuttujiin
    x_loc, y_loc = center(a)

    # käydään dist_table läpi niin, jotta otetaan numpyllä jokaisen arvon indeksi
    for i, val in np.ndenumerate(dist_table):
        dist_table[i] = np.linalg.norm(np.array(i) - np.array([x_loc, y_loc]))

    return dist_table


def scale(a, tmin=0.0, tmax=1.0):
    """
    Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax].
    """
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))


def radial_mask(a):
    # 1 - funktio(), jotta saadaan mahdollisimman suuret tulokset keskelle
    return scale(1 - radial_distance(a))


def radial_fade(a):
    # kerrotaan alkuperäinen kuva maskilla (broadcast)
    # maskia täytyy muokata, sillä shape erimuotoinen
    return a * radial_mask(a).reshape(a.shape[0], a.shape[1], 1)


def main():

    # luetaan kuva
    painting = plt.imread('src/painting.png')
    print(painting.shape)

    # alkuperäinen
    plt.subplot(3, 1, 1)
    plt.imshow(painting.copy())

    # maski
    plt.subplot(3, 1, 2)
    plt.imshow(radial_mask(painting.copy()))

    # maski * alkuperäinen
    plt.subplot(3, 1, 3)
    plt.imshow(radial_fade(painting.copy()))

    plt.show()


if __name__ == "__main__":
    main()
