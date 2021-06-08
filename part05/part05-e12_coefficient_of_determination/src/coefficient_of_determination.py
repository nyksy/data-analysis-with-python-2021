#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression


def coefficient_of_determination():

    # luodaan taulukko vastauksille
    r2_scores = [np.nan] * 6

    df = pd.read_csv("src/mystery_data.tsv", sep="\t")

    X = df.loc[:, "X1":"X5"]
    Y = df['Y']

    model = LinearRegression(fit_intercept=True)
    model.fit(X, Y)

    r2_scores[0] = model.score(X, Y)

    for i, kolumni in enumerate(X):
        # yksittäinen kolumni
        x = df[kolumni].values.reshape(-1, 1)
        model.fit(x, Y)
        r2_scores[i + 1] = model.score(x, Y)

    return r2_scores


def main():
    R2 = coefficient_of_determination()

    for i, coef in enumerate(R2):
        if i == 0:
            print('R2-score with feature(s) X', 'is', coef)
        else:
            print('R2-score with feature(s) X{}'.format(i), 'is', coef)


if __name__ == "__main__":
    main()
