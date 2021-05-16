#!/usr/bin/python3

from numpy import array
from numpy.linalg import lstsq, solve, LinAlgError


def almost_meeting_lines(a1, b1, a2, b2):
    # luvut a1 ja a2 tulee vaihtaa negatiiviseksi, vastaavasti voitaisiin laittaa -1 ja -b (?)

    try:
        # Solve heittää linalgerrorin, mikäli ei löydä vastausta, true perään mikäli onnistui
        return solve(
            array([[-a1, 1], [-a2, 1]]),
            array([b1, b2])
        ), True

    except LinAlgError:
        # Lstsq palauttaa useamman ratkaisun, otetaan taulukosta ensimmäinen tuple
        return lstsq(
            array([[-a1, 1], [-a2, 1]]),
            array([b1, b2]),
            rcond=None
        )[0], False


def main():
    a1 = 1
    b1 = 2
    a2 = -1
    b2 = 0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1 = a2 = 1
    b1 = 2
    b2 = -2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1 = 1
    b1 = 2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1 = 1
    b1 = 2
    a2 = 1
    b2 = 1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")


if __name__ == "__main__":
    main()
