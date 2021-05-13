#!/usr/bin/env python3

import sys
from math import sqrt


def summary(filename):

    summa = 0
    avg = 0
    stddev = 0

    # luetaan tiedosto listaksi
    with open(filename, 'r') as tiedosto:
        rivit = tiedosto.readlines()

    float_rivit = []

    # testataan muuntaa rivit floateiksi
    for luku in rivit:
        try:
            float_rivit.append(float(luku))
        except ValueError:
            continue

    summa = sum([float(luku) for luku in float_rivit])

    avg = summa/len(float_rivit)

    stddev = sqrt(sum([((float(luku) - avg) ** 2)
                       for luku in float_rivit]) / (len(float_rivit) - 1))

    return (summa, avg, stddev)


def main():
    for item in sys.argv[1:]:
        smr = summary(item)
        print('File:', item, 'Sum:', format(smr[0], '.6f'),
              'Average:', format(smr[1], '.6f'), 'Stddev:', format(smr[2], '.6f'))

    if len(sys.argv) <= 1:
        print(summary('src/example.txt'))


if __name__ == "__main__":
    main()
