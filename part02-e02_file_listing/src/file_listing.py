#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):

    tuple_list = []

    # avataan tiedosto
    with open(filename, "r") as tiedosto:
        for rivi in tiedosto:

            size = re.findall(r'\d{2,}', rivi)
            month = re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s-]', rivi)
            #day  = re.findall()
            #hour = re.findall()
            #minute = re.findall()
            name = re.findall(r'\w+\.?_?[a-z]{2,}$', rivi)

            print(name)

            # lisätään "tmp"-listojen ensimmäisistä alkioista koostuva tuple listaan
            tuple_list.append((int(size[0]), month[0], name[0]))

    return tuple_list


def main():
    print(file_listing())


if __name__ == "__main__":
    main()
