#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week():
    # luetaan data
    df_last_week = pd.read_csv(
        'src/UK-top40-1964-1-2.tsv',
        sep='\t'
    )

    # Re ja New -> NaN
    df_last_week = df_last_week.replace(['New', 'Re'], np.nan)

    # numeeriseksi
    df_last_week['LW'] = pd.to_numeric(df_last_week['LW'])

    # maskataan parhaimmat sijat pois, mikäli niistä ei ole tietoa
    df_last_week['Peak Pos'].mask(
        (df_last_week['Peak Pos'] == df_last_week['Pos']) &
        (df_last_week['Peak Pos'] < df_last_week['LW']),
        np.nan,
        inplace=True
    )

    # siirretään edellinen viikko nykyiseksi, coerce, jotta invalid -> null
    df_last_week['Pos'] = pd.to_numeric(df_last_week['LW'], errors='coerce')

    # koko rivi np.nan, missä positio np.nan
    df_last_week[df_last_week['Pos'].isnull()] = np.nan

    # vähennetään 'Viikkoja listalla' -arvoa yhdellä, sillä tarkastellaan edellistä viikkoa
    df_last_week['WoC'] = df_last_week['WoC'] - 1

    # puuttuvat positiot/indeksit listaan, XOR
    missing = list(set(range(
        1, df_last_week.shape[0] + 1)).symmetric_difference(df_last_week['Pos'].values))

    # nanit pois
    missing = [item for item in missing if str(item) != 'nan']

    # korvataan np.nan -arvot missing_positions-listan arvoilla,
    # ihan sama oikeastaan mikä menee mihin väliin koska arvot kuitenkin nan
    df_last_week.loc[df_last_week['Pos'].isnull(), 'Pos'] = missing

    # koko kolumni -> np.nan
    df_last_week['LW'] = np.nan

    # sortataan
    df_last_week.sort_values(by=['Pos'], inplace=True)

    return df_last_week


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
