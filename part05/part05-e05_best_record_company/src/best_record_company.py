#!/usr/bin/env python3

import pandas as pd


def best_record_company():
    df_top = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')

    # kopioidaan
    df = df_top.copy()

    # groupataan julkaisijan mukaan, summataan WoC
    grouped = df.groupby('Publisher')['WoC'].sum()

    # sortataan
    grouped.sort_values(ascending=False, inplace=True)

    # Palautetaan dataframesta pelkästään "parhaan" julkaisijan kappaleet
    return df.loc[df['Publisher'] == grouped.index[0]]


def main():
    print(best_record_company())


if __name__ == "__main__":
    main()
