#!/usr/bin/env python3

from scipy.stats import pearsonr
import numpy as np


def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values


def lengths():
    # ladataan datasetti ja verrataan ensimmäistä ja kolmatta saraketta
    dataset = load()
    return pearsonr(dataset[:, 0], dataset[:, 2])[0]


def correlations():
    # ladataan datasetti ja lasketaan correlaatio kaikkien muuttujien välillä
    # rowvar täytyy laittaa falseksi, sillä muuttujia on vain ensimmäisellä rivillä, kolumnien päissä
    dataset = load()
    return np.corrcoef(dataset, rowvar=False)


def main():
    print(lengths())
    print(correlations())


if __name__ == "__main__":
    main()
