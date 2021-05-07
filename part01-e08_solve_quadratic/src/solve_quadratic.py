#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):

    # diskriminantti
    disc = (b*b)-(4*a*c)

    return ((-b-math.sqrt(disc))/(2*a), (-b+math.sqrt(disc))/(2*a))


def main():
    print(solve_quadratic(1,2,1))


if __name__ == "__main__":
    main()
