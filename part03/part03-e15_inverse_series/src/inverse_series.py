#!/usr/bin/env python3

import pandas as pd


def inverse_series(s):
    return pd.Series(index=s.values, data=s.index)


def main():
    d = {2001: "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017: "Trump"}
    print(inverse_series(pd.Series(d)))


if __name__ == "__main__":
    main()
