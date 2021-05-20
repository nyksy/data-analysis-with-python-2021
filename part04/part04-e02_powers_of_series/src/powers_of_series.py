#!/usr/bin/env python3

import pandas as pd


def powers_of_series(s, k):

    # luodaan dataframe, lisätään sarjan indeksi
    dataframe = pd.DataFrame([], index=s.index)

    # käydään kokonaislukuja yhdestä k:hon asti, lisätään dataframeen
    for i in range(1, k + 1):
        dataframe[i] = s ** i

    return dataframe


def main():
    print(powers_of_series(pd.Series([1, 2, 3, 4], index=list('abcd')), 3))


if __name__ == "__main__":
    main()
