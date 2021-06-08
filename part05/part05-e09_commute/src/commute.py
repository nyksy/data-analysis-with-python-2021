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


def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    date_df = split_date(df)

    df = df.dropna(how="all", axis=1).dropna(how="all")
    del df['Päivämäärä']

    return pd.concat([date_df, df], axis=1)


def bicycle_timeseries():
    #df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')

    df = split_date_continues()

    # luodaan date-kolumni
    df['date'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour']])

    # dropataan ylimääräiset
    df = df.drop(columns=['Year', 'Month', 'Day', 'Hour'])

    # muutetaan indeksi
    df = df.set_index('date')

    return df


def commute():

    weekday_dict = {
        'Mon': 1,
        'Tue': 2,
        'Wed': 3,
        'Thu': 4,
        'Fri': 5,
        'Sat': 6,
        'Sun': 7
    }

    df = bicycle_timeseries()

    # elokuu 2017 plotattavaksi
    df = df['2017-08-01':'2017-08-31']

    df['Weekday'] = df['Weekday'].map(weekday_dict)

    df = df.set_index('Weekday')

    grouped = df.groupby('Weekday').sum()

    return grouped


def main():
    df = commute()

    df.plot()

    weekdays = "x mon tue wed thu fri sat sun".title().split()

    plt.gca().set_xticklabels(weekdays)
    plt.show()


if __name__ == "__main__":
    main()
