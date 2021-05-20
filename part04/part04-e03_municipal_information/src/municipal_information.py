#!/usr/bin/env python3

import pandas as pd


def main():

    # luetaan data
    municipal_data = pd.read_csv(
        'src/municipal.tsv',
        sep='\t',
        lineterminator='\r'
    )

    print('Shape:', str(
        municipal_data.shape[0] - 1) + ',' + str(municipal_data.shape[1]))

    print('Columns:')
    [print(kolumni) for kolumni in municipal_data.columns]
    

if __name__ == "__main__":
    main()
