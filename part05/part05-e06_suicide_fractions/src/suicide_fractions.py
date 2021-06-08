#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():
    fractions = pd.read_csv('src/who_suicide_statistics.csv', sep=",")

    # dropataan ylimääräiset
    fractions.drop(['year', 'sex', 'age'], axis=1, inplace=True)

    fractions['fraction'] = fractions['suicides_no'] / fractions['population']

    grouped = fractions.groupby('country')

    return pd.Series(index=grouped.mean().index, data=grouped['fraction'].mean())


def main():
    print(suicide_fractions())


if __name__ == "__main__":
    main()
