#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)


def load_finnish():
    # Returns a list of Finnish words
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode('utf-8'))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines


def get_features(a):

    features = np.zeros((len(a), len(alphabet_set)))

    # käydään sanalista läpi
    for i, sana in enumerate(a):

        # kirjaimet sanassa
        letter_counts = Counter(list(sana))

        feature = []

        for kirjain in list(alphabet):

            if letter_counts[kirjain] != 0:
                feature.append(letter_counts[kirjain])
            else:
                feature.append(0)

        # lisätään koko rivi kerralla
        features[i, :] = feature

    return features


def contains_valid_chars(s):
    # jos sana s on subset, kaikki kirjaimet löytyvät aakkos-setistä
    return set(s).issubset(alphabet_set)


def get_features_and_labels():

    # haetaan suomenkieliset sanat, muunnetaan samalla lowercase
    list_fi = [str(sana).lower() for sana in load_finnish()]

    # englanninkieliset vain mikäli ensimmäinen kirjain on pieni
    list_en = [str(sana).lower()
               for sana in load_english() if sana[0].islower()]

    # filtterit
    filtered_fi = [sana for sana in list_fi if contains_valid_chars(sana)]
    filtered_en = [sana for sana in list_en if contains_valid_chars(sana)]

    # featuret
    features_fi = get_features(filtered_fi)
    features_en = get_features(filtered_en)

    features = np.concatenate((features_fi, features_en))

    # suomenkieliset 0, englanninkieliset 1
    labels = np.concatenate(
        (
            np.zeros(features_fi.shape[0]),
            np.ones(features_en.shape[0])
        )
    )

    return features, labels


def word_classification():
    X, y = get_features_and_labels()

    model = MultinomialNB()
    cvs = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)

    return cross_val_score(model, X, y, cv=cvs)


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
