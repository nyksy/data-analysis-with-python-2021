#!/usr/bin/env python3

import numpy as np


def first_half_second_half(a):
    # pilkotaan jokainen rivi puoliksi ja vertaillaan summia
    return a[np.sum(a[:, :a.shape[1]//2], axis=1) > np.sum(a[:, a.shape[1]//2:], axis=1)]


def main():
    np.random.seed(0)
    a = np.random.randn(10, 2*10)
    print("result:\n", first_half_second_half(a))


if __name__ == "__main__":
    main()
