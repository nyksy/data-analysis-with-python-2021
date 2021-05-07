#!/usr/bin/env python3

def transform(s1, s2):
    # splitataan merkkijonot, yhdistetään listat zipillä ja kerrotaan parien sisällöt keskenään
    return [x*y for x,y in zip(list(map(int, s1.split())), list(map(int, s2.split())))]

    
def main():
    transform("1 2 3", "3 4 5")


if __name__ == "__main__":
    main()
