
"""
kolmion funktioita

"""

__author__ = "Juho Nykänen, UEF"
__version__ = "0.0.1"


from math import sqrt


def hypothenuse(s1, s2):
    """palauttaa hypotenuusan pituuden

    Args:
        s1 (float): kolmion kanta
        s2 (float): kolmion korkeus

    Returns:
        float: hypotenuusan pituus laskettuna kannasta ja korkeudesta
    """
    return sqrt(float(s1**2) + float(s2**2))


def area(s1, s2):
    """palautetaan kolmion pinta-ala

    Args:
        s1 (float): kolmion kanta
        s2 (float): kolmion korkeus

    Returns:
        Float: pinta-ala (kanta*korkeus)/2
    """
    return (s1 * s2) / 2
