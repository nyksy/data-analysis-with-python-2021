#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def explained_variance():

    df = pd.read_csv('src/data.tsv', sep='\t')
    pca = PCA(df.shape[1]).fit(df)

    return df.var(axis=0), pca.explained_variance_


def main():
    v, ev = explained_variance()

    v_floats = [format(num, '.3f') for num in v]
    ev_floats = [format(num, '.3f') for num in ev]

    print('The variances are:',
          ' '.join(map(str, v_floats)))
    print('The explained variances after PCA are:',
          ' '.join(map(str, ev_floats)))

    total = 0
    cumulative_time = [total := total + t for t in ev]

    plt.plot(np.arange(1, len(ev) + 1), cumulative_time)
    plt.show()


if __name__ == "__main__":
    main()
