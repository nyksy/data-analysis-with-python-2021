#!/usr/bin/env python3
import pandas as pd
import numpy as np


def create_series(L1, L2):
    return (
        pd.Series(data=L1, index=['a', 'b', 'c']),
        pd.Series(data=L2, index=['a', 'b', 'c'])
    )


def modify_series(s1, s2):

    # lisätään ensimmäiseen
    s1['d'] = s2['b']

    # poistetaan jälkimmäisestä
    s2.drop(labels=['b'], inplace=True)

    return (s1, s2)


def main():
    sarjat = create_series([1, 2, 3], [4, 5, 6])
    print('Sarjat:')
    print(sarjat[0])
    print(sarjat[1])

    muutetut = modify_series(sarjat[0], sarjat[1])
    print('Muutetut:')
    print(muutetut[0])
    print(muutetut[1])
    print(muutetut[0] + muutetut[1])


if __name__ == "__main__":
    main()
