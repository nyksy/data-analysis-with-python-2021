#!/usr/bin/env python3

def main():
    #tulostetaan (i, j) silloin kun i + j == 5
    [print((i, j)) for i in range(1, 7) for j in range(1, 7) if i + j == 5]


if __name__ == "__main__":
    main()
