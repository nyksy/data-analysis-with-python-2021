#!/usr/bin/env python3

import sys


def file_count(filename):

    with open(filename, 'r') as tiedosto:
        rivit = tiedosto.readlines()

        tiedosto.seek(0)
        sisalto = tiedosto.read()

    sanat = 0
    for rivi in rivit:
        if rivi != '\n':
            sanat += len(rivi.split(" "))

    return (
        len(rivit),
        sanat,
        len(sisalto)
    )


def main():
    for item in sys.argv[1:]:
        count = file_count(item)
        print(str(count[0]) + '\t' + str(count[1]) + '\t' + str(count[2]) + '\t' + item)

    if len(sys.argv) <= 1:
        print(file_count('src/test.txt'))


if __name__ == "__main__":
    main()
