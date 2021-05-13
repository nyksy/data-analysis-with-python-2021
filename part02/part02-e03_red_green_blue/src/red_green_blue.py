#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):

    result_list = []

    # avataan tiedosto
    with open(filename, "r") as tiedosto:
        next(tiedosto)

        for rivi in tiedosto:

            # haetaan regexillä rgb-arvo sekä mahdollisesti moniosainen nimi
            result = re.match(
                r'([\s]*[\d]+)\s+([\d]+)\s+([\d]+)\s+([\w]+(\s+\w+)?)', rivi)

            if result:

                # matchi listaksi ja tuloslistaan
                rgb_list = result.groups()
                result_list.append(
                    str(rgb_list[0]) + '\t' + str(rgb_list[1]) + '\t' + str(rgb_list[2]) + '\t' + rgb_list[3])

    return result_list


def main():
    test_list = red_green_blue()

    for item in test_list:
        print(item)


if __name__ == "__main__":
    main()
