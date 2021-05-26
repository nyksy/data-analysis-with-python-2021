#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    # luetaan data
    df = pd.read_csv('src/presidents.tsv', sep='\t')

    # mikäli sisältää pilkun, splitataan ja vaihdetaan etunimen ja sukunimen paikka
    df['President'] = (df['President'].str.split()
                       .apply(lambda x: ' '.join(x[::-1]).rstrip(','))
                       .where(df['President'].str.contains(','), df['President'])
                       .str.title()
                       )

    df['Vice-president'] = (df['Vice-president'].str.split()
                            .apply(lambda x: ' '.join(x[::-1]).rstrip(','))
                            .where(df['Vice-president'].str.contains(','), df['Vice-president'])
                            .str.title()
                            )

    # splitataan ja otetaan ensimmäinen
    df['Start'] = df['Start'].str.split().str[0]

    # numeeriseksi
    df['Last'] = pd.to_numeric(df['Last'], errors='coerce')

    # korvataan "two" -> 2
    df['Seasons'] = df['Seasons'].replace(to_replace="two", value=2)

    # konversiot
    df['President'] = df['President'].astype('object')
    df['Start'] = df['Start'].astype(int)
    df['Last'] = df['Last'].astype(float)
    df['Seasons'] = df['Seasons'].astype(int)
    df['Vice-president'] = df['Vice-president'].astype('object')

    return df


def main():
    df = cleaning_data()
    print(df.dtypes)
    print(df.shape)
    print(df)


if __name__ == "__main__":
    main()
