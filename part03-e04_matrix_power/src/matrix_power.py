#!/usr/bin/env python3
from numpy import eye, matmul, linalg, random
from functools import reduce


def matrix_power(a, n):

    if n == 0:
        return eye(a.shape[0])
    # Mikäli n negatiivinen, käytetään inverse matriisia
    elif n < 0:
        return reduce(matmul, (linalg.inv(a) for x in range(abs(n))), eye(linalg.inv(a).shape[0]))
    else:
        return reduce(matmul, (a for x in range(abs(n))), eye(a.shape[0]))


def main():
    random.seed(42)
    a = random.randn(10, 10)
    n = 2
    print("result:\n", matrix_power(a, n))


if __name__ == "__main__":
    main()
