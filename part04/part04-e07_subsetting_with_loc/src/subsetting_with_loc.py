#!/usr/bin/env python3

import pandas as pd


def subsetting_with_loc():

    # luetaan data
    df = pd.read_csv(
        'src/municipal.tsv',
        sep='\t',
        index_col="Region 2018"
    )

    return df.loc[
        "Akaa":"Äänekoski",
        [
            "Population",
            "Share of Swedish-speakers of the population, %",
            "Share of foreign citizens of the population, %"
        ]
    ]


def main():
    print(subsetting_with_loc().head())


if __name__ == "__main__":
    main()
