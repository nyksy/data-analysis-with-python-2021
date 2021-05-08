#!/usr/bin/env python3

def sum_equation(L):

    #testataan, onko listassa alkioita
    if len(L) > 0:
        return " + ".join([str(num) for num in L]) + " = " + str(sum(L))
    else:
        return "0 = 0"


def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
