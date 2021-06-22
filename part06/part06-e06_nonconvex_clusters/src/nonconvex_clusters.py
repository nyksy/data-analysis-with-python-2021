#!/usr/bin/env python3

import scipy
from numpy.lib.arraysetops import unique
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():

    df = pd.read_csv('src/data.tsv', sep='\t')

    eps = []
    scores = []
    clusters = []
    outliers = []

    X = df[['X1', 'X2']]
    y = df['y']

    unique_count = len(unique(y))

    for dist in np.arange(0.05, 0.2, 0.05):

        clustered = DBSCAN(eps=dist).fit(X)

        # lasketaan uniikkien määrä, ei huomioida -1
        unique_labels = len(
            unique(
                [label for label in clustered.labels_ if label != -1]
            )
        )
        
        # -1 -arvojen määrä
        outlier_count = list(clustered.labels_).count(-1)

        score = np.nan
        # scoret
        if unique_count == unique_labels:
            permutation = find_permutation(unique_labels, y, clustered.labels_)
            new_labels = [permutation[label] for label in clustered.labels_]

            # TODO score ei ole oikea
            score = accuracy_score(y, new_labels)

        eps.append(float(dist))
        scores.append(float(score))
        clusters.append(float(unique_labels))
        outliers.append(float(outlier_count))

    # muodostetaan dataframe
    result = pd.DataFrame(
        data={
            'eps': eps,
            'Score': scores,
            'Clusters': clusters,
            'Outliers': outliers
        }
    )
    return result


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
