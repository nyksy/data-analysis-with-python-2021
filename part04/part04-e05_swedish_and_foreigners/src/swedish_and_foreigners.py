#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners():
    # luetaan data
    original_data = pd.read_csv(
        'src/municipal.tsv',
        sep='\t',
        index_col="Region 2018",
    )

    # otetaan vain kaupungit alkuperäisestä datasta
    municipal_data = original_data["Akaa": "Äänekoski"]

    # ruotsinkielisiä yli 5%
    swedish_data = municipal_data[municipal_data["Share of Swedish-speakers of the population, %"] > 5]

    # ruotsinkielisistä ulkomaalaisia yli 5%
    swedish_and_foreigers_data = swedish_data[swedish_data["Share of foreign citizens of the population, %"] > 5]

    # Palautetaan vain kolme kolumnia
    return swedish_and_foreigers_data[
        ['Population',
         'Share of Swedish-speakers of the population, %',
         'Share of foreign citizens of the population, %']
    ]


def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
