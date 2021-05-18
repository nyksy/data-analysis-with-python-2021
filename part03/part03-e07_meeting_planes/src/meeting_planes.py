#!/usr/bin/python3

from numpy import array
from numpy.linalg import solve


def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):

    # z = an y + bn x + cn
    # [ b1 a1 c1 z]
    # [ b2 a2 c2 z]
    # [ b3 a3 c3 z]
    # huomioidaan x:n ja y:n kertoimien järjestys, a, b -> b, a
    return solve(
        array([[b1, a1, -1],
               [b2, a2, -1],
               [b3, a3, -1]]),
        array([-c1, -c2, -c3])
    )


def main():
    a1 = 1
    b1 = 4
    c1 = 5
    a2 = 3
    b2 = 2
    c2 = 1
    a3 = 2
    b3 = 4
    c3 = 1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")


if __name__ == "__main__":
    main()
