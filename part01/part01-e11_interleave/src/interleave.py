#!/usr/bin/env python3

def interleave(*lists):
    #summataan yhdeksi listaksi zip-funktion palauttamat objektit
    return [*sum(zip(*lists),())]

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
