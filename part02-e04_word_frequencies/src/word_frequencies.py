#!/usr/bin/env python3

def word_frequencies(filename):

    sana_list = []

    sana_dict = {}

    # avataan tiedosto
    with open(filename, 'r') as tiedosto:

        # käydään rivit läpi
        for rivi in tiedosto:
            # lisätään kaikki sanat yhteen listaan, joka lopuksi iteroidaan dictionaryyn
            sana_list.extend([sana.strip("""!"#$%&'()*,-./:;?@[]_""")
                              for sana in rivi.split()])

    # käydään sanalista läpi ja kasvatetaan sanakirjan arvoa aina esiintymän yhteydessä
    for sana in sana_list:
        sana_dict[sana] = sana_dict.get(sana, 0) + 1

    return sana_dict


def main():
    test_dict = word_frequencies('src/alice.txt')

    for key, val in test_dict.items():
        print(key, val)


if __name__ == "__main__":
    main()
