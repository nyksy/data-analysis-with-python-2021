#!/usr/bin/env python3

def find_matching(L, pattern):
    #palautetaan lista indeksejä, joissa indeksin sisältämä sana sisältää patternin sisältämän merkkijonon
    return [index for index, sana in enumerate(L) if pattern in sana]


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))


if __name__ == "__main__":
    main()
