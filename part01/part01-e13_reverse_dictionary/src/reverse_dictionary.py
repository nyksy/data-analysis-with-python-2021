#!/usr/bin/env python3

def reverse_dictionary(d):

    rev_dict = {}

    # käydään sanakirja läpi
    for avain, sanalista in d.items():

        # käydään arvon sisältämä lista läpi
        for sana in sanalista:
            # lisätään avain sanakirjaan, mikäli on jo niin lisätään olemassaolevaan
            rev_dict.setdefault(sana, []).append(avain)

    return rev_dict


def main():
    d = {
        'move': ['liikuttaa'],
        'hide': ['piilottaa', 'salata'],
        'six': ['kuusi'],
        'fir': ['kuusi']
    }

    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
