#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():

    df = pd.read_csv("src/who_suicide_statistics.csv")

    df["Suicide fraction"] = df["suicides_no"] / df["population"]

    result = df.groupby("country").mean()

    return result["Suicide fraction"]


def suicide_weather():
    # haetaan data
    suicide_series = suicide_fractions()
    temperatures = pd.read_html(
        'src/List_of_countries_by_average_yearly_temperature.html',
        index_col=0,
        header=0
    )[0]

    # muunnetaan html:stä luettu dataframen kolumnin nimi kivempaan muotoon
    temperatures.rename(
        columns={
            'Average yearly temperature (1961–1990, degrees Celsius)': 't'},
        inplace=True
    )

    temperatures['t'] = temperatures['t'].apply(
        lambda val: float(val.replace("\u2212", "-")))

    temperatures['t'] = temperatures['t'].astype(float)

    # yhdistetään
    merged = pd.concat(
        [suicide_series.to_frame(), temperatures],
        join='inner',
        axis=1
    )

    # korrelaatio
    corr = suicide_series.corr(
        temperatures['t'],
        method="spearman"
    )

    return (len(suicide_series), len(temperatures), len(merged), corr)


def main():
    tpl = suicide_weather()
    print('Suicide DataFrame has', tpl[0], 'rows')
    print('Temperature DataFrame has', tpl[1], 'rows')
    print('Common DataFrame has', tpl[2], 'rows')
    print('Spearman correlation:', format(tpl[3], '.1f'))


if __name__ == "__main__":
    main()
