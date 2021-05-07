#!/usr/bin/env python3

def merge(L1, L2):

    i = 0
    j = 0

    s1 = len(L1)
    s2 = len(L2)

    sol = []

    #Käydään listoja läpi siihen saakka kunnes toinen loppuu
    while i < s1 and j < s2:
        if L1[i] <= L2[j]:
            sol.append(L1[i])
            i += 1
        else:
            sol.append(L2[j])
            j += 1

    #palautetaan tulos + toisen listan jäänteet
    return sol + L1[i:] + L2[j:]


def main():
    print(merge([1, 5, 9, 12], [2, 6, 10]))


if __name__ == "__main__":
    main()
