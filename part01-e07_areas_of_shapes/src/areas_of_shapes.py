#!/usr/bin/env python3

import math


def tria():
    base = input('Give base of the triangle: ')
    height = input('Give height of the triangle: ')
    print('The area is', (float(base)*float(height))/2)


def rect():
    width = input('Give width of the rectangle: ')
    height = input('Give height of the rectangle: ')
    print('The area is', float(width)*float(height))


def circ():
    radius = input('Give radius of the circle: ')
    print('The area is', float(radius)*float(radius)*math.pi)


def main():
    shape = input("Choose a shape (triangle, rectangle, circle): ")

    while len(shape) > 0:
        if shape == 'triangle':
            tria()
        elif shape == 'rectangle':
            rect()
        elif shape == 'circle':
            circ()
        else:
            print("Unknown shape!")
        shape = input("Choose a shape (triangle, rectangle, circle): ")


if __name__ == "__main__":
    main()
