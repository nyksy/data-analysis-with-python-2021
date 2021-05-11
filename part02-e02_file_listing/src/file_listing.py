#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):

    tuple_list = []

    # avataan tiedosto
    with open(filename, "r") as tiedosto:
        for rivi in tiedosto:
        
            #tehdään erillisillä regex-hauilla, jotta saattaa tulla selkeämmän näköistä
            size = re.findall(r'\d{2,}', rivi)
            month = re.findall(
                r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', rivi)
            datetime = re.findall(r'\d{1,2}\s{1}\d{2}:\d{2}', rivi)
            name = re.findall(r'[a-z._]{2,}$', rivi)

            #päivä, tunti ja minuutti samaan listaan
            date_list = datetime[0].replace(':', ' ').split()

            # lisätään "tmp"-listojen ensimmäisistä alkioista koostuva tuple listaan
            tuple_list.append((int(size[0]), month[0], int(
                date_list[0]), int(date_list[1]), int(date_list[2]), name[0]))

    return tuple_list


def main():
    test_list = file_listing()
    [print(item) for item in test_list]


if __name__ == "__main__":
    main()
