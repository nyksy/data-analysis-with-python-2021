#!/usr/bin/env python3

class Rational(object):

    def __init__(self, osittaja, nimittaja = 1):
        self.osittaja = osittaja
        self.nimittaja = nimittaja

    def __add__(self, other):
        return Rational(self.osittaja*other.nimittaja + self.nimittaja*other.osittaja, self.nimittaja*other.nimittaja)

    def __sub__(self, other):
        return Rational(self.osittaja*other.nimittaja - self.nimittaja*other.osittaja, self.nimittaja*other.nimittaja)

    def __mul__(self, other):
        return Rational(self.osittaja * other.osittaja, self.nimittaja*other.nimittaja)

    def __truediv__(self, other):
        return Rational(self.osittaja*other.nimittaja, self.nimittaja*other.osittaja)

    def __gt__(self, other):
        return self.osittaja*other.nimittaja > self.nimittaja*other.osittaja

    def __lt__(self, other):
        return self.osittaja*other.nimittaja < self.nimittaja*other.osittaja

    def __eq__(self, other):
        return self.osittaja == other.osittaja and self.nimittaja == other.nimittaja

    def __str__(self):
        if self.nimittaja == 1:
            return str(self.osittaja)
        else:
            return str(self.osittaja) + '/' + str(self.nimittaja)


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1+r2)
    print(r1*r2)
    print(r1/r2)
    print(r1-r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
