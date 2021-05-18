#!/usr/bin/python3

from numpy.linalg import solve
from numpy import array


def meeting_lines(a1, b1, a2, b2):

    # a1x + b1 = y ja a2x + b2 = y
    # luvut a1 ja a2 tulee vaihtaa negatiiviseksi, vastaavasti voitaisiin laittaa -1 ja -b (?)
    return solve(
        array([[-a1, 1], [-a2, 1]]),
        array([b1, b2])
    )


def main():
    a1 = 1
    b1 = 4
    a2 = 3
    b2 = 2

    x, y = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")


if __name__ == "__main__":
    main()
