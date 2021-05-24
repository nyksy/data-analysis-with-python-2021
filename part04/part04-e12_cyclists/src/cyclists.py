#!/usr/bin/env python3

import pandas as pd


def cyclists():
    
    # luetaan data
    cyclists_df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')

    print(cyclists_df.shape)

    # pudotetaan kaikki kolumnit ja rivit, joissa kaikki arvot ovat tyhjiä
    cyclists_df.dropna(how="all", inplace=True, axis=1)
    cyclists_df.dropna(how="all", inplace=True)

    return cyclists_df


def main():
    print(cyclists().shape)


if __name__ == "__main__":
    main()
