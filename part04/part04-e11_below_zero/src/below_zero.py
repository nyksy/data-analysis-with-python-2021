#!/usr/bin/env python3

import pandas as pd


def below_zero():

    # luetaan data
    weather_df = pd.read_csv('src/kumpula-weather-2017.csv')

    # palautetaan lämpötilalla maskatun dataframen index-kolumnin pituus
    return len(weather_df[weather_df['Air temperature (degC)'] < 0].index)


def main():
    print('Number of days below zero:', below_zero())


if __name__ == "__main__":
    main()
