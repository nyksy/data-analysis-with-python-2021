#!/usr/bin/env python3

import pandas as pd


def snow_depth():

    # luetaan data
    weather_df = pd.read_csv(
        'src/kumpula-weather-2017.csv',
        sep=','
    )

    # käytetään lumen syvyys -kolumnille max-funktiota
    return weather_df['Snow depth (cm)'].max()


def main():
    print('Max snow depth:', format(snow_depth(), '.1f'))


if __name__ == "__main__":
    main()
