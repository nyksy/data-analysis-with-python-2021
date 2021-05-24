#!/usr/bin/env python3

import pandas as pd


def average_temperature():
    # luetaan data
    weather_df = pd.read_csv(
        'src/kumpula-weather-2017.csv',
        sep=','
    )

    # heinäkuulle maski
    mask = (weather_df['m'] == 7)
    masked_data = weather_df[mask]

    # mean-funktio lämpötilalle heinäkuussa
    return masked_data['Air temperature (degC)'].mean()


def main():
    print('Average temperature in July:', str(
        format(average_temperature(), '.1f')))


if __name__ == "__main__":
    main()
