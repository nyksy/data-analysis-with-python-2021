#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


days = dict(zip("ma ti ke to pe la su".split(),
                "Mon Tue Wed Thu Fri Sat Sun".split()))

months = dict(zip(
    "tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))


def split_date(df):

    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)

    d["Hour"] = hourmin.iloc[:, 0]
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)

    d = d.astype({"Weekday": object, "Day": int,
                  "Month": int, "Year": int, "Hour": int})

    return d


def split_date_continues():

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")

    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)

    return pd.concat([d, df], axis=1)


def cycling_weather():

    # globaali muuttuja, jos kerta tiedostoja saa lukea vain kahdesti :)
    global wh
    wh = pd.read_csv("src/kumpula-weather-2017.csv")
    bike = split_date_continues()

    result = pd.merge(wh, bike, left_on=["Year", "m", "d"], right_on=[
        "Year", "Month", "Day"])

    return result.drop(['m', 'd', 'Time', 'Time zone'], axis=1)


def cycling_weather_continues(station):

    df = cycling_weather()
    weather_df = wh

    summa = df.groupby(['Month', 'Day'])[station].sum()

    merged = pd.merge(
        weather_df,
        summa,
        left_on=['d', 'm'],
        right_on=['Day', 'Month']
    )

    # ei toimi mikäli axis=1 on ensin, täyttää eri tavalla ja tällöin testit pielessä
    merged = merged.ffill(axis=0).ffill(axis=1)

    # luodaan malli
    model = LinearRegression(fit_intercept=True)

    x = np.vstack([merged['Precipitation amount (mm)'],
                   merged['Snow depth (cm)'],
                   merged['Air temperature (degC)']]
                  ).T
    y = merged[station]

    model.fit(x, y)

    return (model.coef_, model.score(x, y))


def main():

    asema = 'Merikannontie'

    data = cycling_weather_continues(asema)

    print('Measuring station:', asema)
    print("Regression coefficient for variable 'precipitation':",
          format(data[0][0], '.1f'))
    print("Regression coefficient for variable 'snow depth':",
          format(data[0][1], '.1f'))
    print("Regression coefficient for variable 'temperature':",
          format(data[0][2], '.1f'))
    print('Score:', format(data[1], '.2f'))


if __name__ == "__main__":
    main()
