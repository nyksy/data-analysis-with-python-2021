#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')

    model = LinearRegression(fit_intercept=False)

    x = np.vstack([df['X1'], df['X2'], df['X3'], df['X4'], df['X5']]).T
    model.fit(x, df['Y'])

    return model.coef_


def main():
    coefficients = mystery_data()

    # print the coefficients here
    for i, coef in enumerate(coefficients):
        print('Coefficient of X{}'.format(i + 1), 'is', coef)


if __name__ == "__main__":
    main()
