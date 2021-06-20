#!/usr/bin/env python3
import gzip
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import numpy as np


def spam_detection(random_state=0, fraction=1.0):

    # luetaan tiedostoista n määrä rivejä
    ham = gzip.open(filename='src/ham.txt.gz').readlines()
    ham_frac = ham[: int(fraction*len(ham))]

    spam = gzip.open(filename='src/spam.txt.gz').readlines()
    spam_frac = spam[: int(fraction*len(spam))]

    both = np.concatenate(
        (
            ham_frac,
            spam_frac
        )
    )

    # CountVectorizer
    vec = CountVectorizer()

    features = vec.fit_transform(both)

    # labelit
    labels = np.concatenate(
        (
            np.zeros(len(ham_frac)),
            np.ones(len(spam_frac))
        )
    )

    X_train, X_test, y_train, y_test = train_test_split(
        features.toarray(), labels, train_size=0.75,  random_state=random_state
    )

    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_fitted = model.predict(X_test)

    acc = accuracy_score(y_test, y_fitted)

    # missed = (1 - acc) * n missä n on testiotoksen pituus
    return acc, len(X_test), int(len(X_test)*(1 - acc))


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")


if __name__ == "__main__":
    main()
