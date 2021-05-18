#!/usr/bin/env python3
import pandas as pd
import numpy as np


def read_series():

    sarja = pd.Series(dtype='O')

    while 1:
        # luetaan käyttäjältä
        values = input('index val: ')

        # mikäli tyhjä, lopetataan
        if len(values) == 0:
            break
        # vääränmittainen -> exception
        elif len(values.split()) < 2 or len(values.split()) > 2:
            raise ValueError('Invalid input')

        index, val = values.split()[0], values.split()[1]

        # lisätään sarjaan
        sarja[index] = val

    return sarja


def main():
    print(read_series())


if __name__ == "__main__":
    main()
