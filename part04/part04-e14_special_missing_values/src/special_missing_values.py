#!/usr/bin/env python3

import pandas as pd
import numpy as np


def special_missing_values():
    # luetaan data
    df = pd.read_csv(
        'src/UK-top40-1964-1-2.tsv',
        sep='\t'
    )

    # korvataan new ja re Nonella, pudotetaan nonet
    df.replace({'New': None, 'Re': None}, inplace=True)
    df.dropna(inplace=True)

    # palautetaan ne kappaleet, joiden sijoitus on huonontunut viimeviikosta
    return df[df['Pos'].astype(int) > df['LW'].astype(float)]


def main():
    print(special_missing_values())


if __name__ == "__main__":
    main()
