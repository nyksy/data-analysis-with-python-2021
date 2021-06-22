#!/usr/bin/env python3

import scipy
import scipy.cluster.hierarchy as hc
import scipy.spatial as sp
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

mapping = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}


def toint(x):
    return mapping.get(str.upper(x))


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def get_features_and_labels(filename):

    df = pd.read_csv(filename, sep='\t')

    features = [[toint(char) for char in x] for x in df['X']]
    labels = df['y']

    return (np.array(features), np.array(labels))


def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g = sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage)
    g.fig.suptitle(
        f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()


def cluster_euclidean(filename):

    X, y = get_features_and_labels(filename)

    clustering = AgglomerativeClustering(
        n_clusters=2, affinity='euclidean', linkage='average').fit(X)

    permutation = find_permutation(2, y, clustering.labels_)
    new_labels = [permutation[label] for label in clustering.labels_]

    return accuracy_score(y, new_labels)


def cluster_hamming(filename):

    X, y = get_features_and_labels(filename)

    distances = pairwise_distances(X, metric='hamming')

    clustering = AgglomerativeClustering(
        n_clusters=2, affinity='precomputed', linkage='average').fit(distances)

    permutation = find_permutation(2, y, clustering.labels_)
    new_labels = [permutation[label] for label in clustering.labels_]

    return accuracy_score(y, new_labels)


def main():
    print("Accuracy score with Euclidean affinity is",
          cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is",
          cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
