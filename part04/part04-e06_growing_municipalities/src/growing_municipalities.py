#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(df):

    # luodaan maski kasvavista kunnista
    mask = (df['Population change from the previous year, %'] > 0)

    return (len(df[mask]) / len(df.index))


def main():

    # luetaan data
    municipal_data = pd.read_csv(
        'src/municipal.tsv',
        sep='\t',
        index_col="Region 2018"
    )

    print('Proportion of growing municipalities:',
          str("{:.1f}".format(growing_municipalities(
              municipal_data["Kitee": "Kuopio"]))) +
          '%'
          )


if __name__ == "__main__":
    main()
