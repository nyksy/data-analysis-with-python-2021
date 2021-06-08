#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date(df):

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
    cyclists_df = df.copy()

    # pudotetaan kaikki kolumnit ja rivit, joissa kaikki arvot ovat tyhjiä
    cyclists_df.dropna(how="all", inplace=True, axis=1)
    cyclists_df.dropna(how="all", inplace=True)

    # päivämäärä-kolumnista uusi dataframe
    date_df = cyclists_df['Päivämäärä'].str.split(expand=True)

    # kolmunien nimet
    date_df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']

    # korjataan viikonpäivät
    date_df['Weekday'] = date_df['Weekday'].map(days_dict)

    date_df['Weekday'] = date_df['Weekday'].astype('object')

    # korjataan kuukaudet
    date_df['Month'] = date_df['Month'].map(month_dict)

    # tunti
    date_df['Hour'] = pd.to_datetime(date_df['Hour'], format='%H:%M').dt.hour

    # konversiot
    date_df['Day'] = pd.to_numeric(date_df['Day'], errors='coerce')
    date_df['Month'] = pd.to_numeric(date_df['Month'], errors='coerce')
    date_df['Year'] = pd.to_numeric(date_df['Year'], errors='coerce')

    date_df['Hour'] = date_df['Hour'].astype(int)
    date_df['Day'] = date_df['Day'].astype(int)
    date_df['Month'] = date_df['Month'].astype(int)
    date_df['Year'] = date_df['Year'].astype(int)

    return date_df


def get_cyclists_df():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    date_df = split_date(df)

    df = df.dropna(how="all", axis=1).dropna(how="all")
    del df['Päivämäärä']

    return pd.concat([date_df, df], axis=1)


def cyclists_per_day():
    df = get_cyclists_df()

    # kopioidaan
    cyclists_df = df.copy()
    cyclists_df.drop(['Hour', 'Weekday'], axis=1, inplace=True)

    groups = cyclists_df.groupby(['Year', 'Month', 'Day']).sum()

    return groups


def main():
    df = cyclists_per_day()
    print(df.head())

    # elokuu 2017 plotattavaksi
    data_august_2017 = df.loc[2017, 8, :]

    data_august_2017.plot()
    plt.show()


if __name__ == "__main__":
    main()
