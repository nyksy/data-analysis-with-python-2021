#!/usr/bin/env python3

import pandas as pd


def top_bands():
    df_top = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df_bands = pd.read_csv('src/bands.tsv', sep='\t')

    # muutetaan kieliasu yhdenmukaiseksi
    df_top['Artist'] = df_top['Artist'].str.lower()
    df_bands['Band'] = df_bands['Band'].str.lower()

    return pd.merge(
        df_top, df_bands,
        how='inner',
        left_on=['Artist'],
        right_on=['Band']
    )


def main():
    print(top_bands().head())


if __name__ == "__main__":
    main()
