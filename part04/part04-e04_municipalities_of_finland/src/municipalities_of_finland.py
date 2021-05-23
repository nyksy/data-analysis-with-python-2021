#!/usr/bin/env python3

import pandas as pd


def municipalities_of_finland():
    # luetaan data
    municipal_data = pd.read_csv(
        'src/municipal.tsv',
        sep='\t',
        index_col="Region 2018",
    )

    return municipal_data["Akaa": "Äänekoski"]


def main():
    print(municipalities_of_finland().head())


if __name__ == "__main__":
    main()
