#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():

    # parit dictionaryt konversioille
    month_dict = {
        'tammi': 1,
        'helmi': 2,
        'maalis': 3,
        'huhti': 4,
        'touko': 5,
        'kesä': 6,
        'heinä': 7,
        'elo': 8,
        'syys': 9,
        'loka': 10,
        'marras': 11,
        'joulu': 12,
    }

    days_dict = {
        'ma': 'Mon',
        'ti': 'Tue',
        'ke': 'Wed',
        'to': 'Thu',
        'pe': 'Fri',
        'la': 'Sat',
        'su': 'Sun',
    }

    # luetaan data
    cyclists_df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')

    # pudotetaan kaikki kolumnit ja rivit, joissa kaikki arvot ovat tyhjiä
    cyclists_df.dropna(how="all", inplace=True, axis=1)
    cyclists_df.dropna(how="all", inplace=True)

    # päivämäärä-kolumnista uusi dataframe
    date_df = cyclists_df['Päivämäärä'].str.split(expand=True)

    # kolmunien nimet
    date_df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']

    # korjataan viikonpäivät
    date_df['Weekday'] = date_df['Weekday'].map(days_dict)

    # korjataan kuukaudet
    date_df['Month'] = date_df['Month'].map(month_dict)

    # tunti
    date_df['Hour'] = pd.to_datetime(date_df['Hour'], format='%H:%M').dt.hour

    # konversiot
    date_df['Day'] = pd.to_numeric(date_df['Day'], errors='coerce')
    date_df['Month'] = pd.to_numeric(date_df['Month'], errors='coerce')
    date_df['Year'] = pd.to_numeric(date_df['Year'], errors='coerce')

    return date_df


def main():
    print(split_date())


if __name__ == "__main__":
    main()
