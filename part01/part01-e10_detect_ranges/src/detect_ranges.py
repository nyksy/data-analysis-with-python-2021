#!/usr/bin/env python3

def detect_ranges(L):
    # Järjestetään
    sorted_list = sorted(L)
    result = []
    i = 0

    # käydään järjestetty lista läpi
    while i < len(sorted_list):

        # Otetaan ensimmäinen talteen
        first = sorted_list[i]

        if i + 1 < len(sorted_list):
            # Mikäli luvut peräkkäisiä
            while sorted_list[i] == sorted_list[i + 1] - 1:

                # kasvatetaan indeksiä kunnes luvut eivät enää ole peräkkäisiä
                i += 1

                # tarkistetaan ettei mennä listan pituudesta yli
                if i + 1 == len(sorted_list):
                    break

        # Otetaan viimeinen peräkkäinen
        last = sorted_list[i]

        # mikäli olivat sama luku == mikäli sisemmässä whilessa ei edetty
        # muutoin lisätään väli
        if first == last:
            result.append(first)
        else:
            # kasvatetaan viimeistä yhdellä koska python on ihanaa <3
            result.append((first, last + 1))

        i += 1

    return result


def main():
    L = [1, 2, 4]
    print(L)
    result = detect_ranges(L)
    print(result)


if __name__ == "__main__":
    main()
