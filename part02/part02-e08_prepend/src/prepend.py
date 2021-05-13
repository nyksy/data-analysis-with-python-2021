#!/usr/bin/env python3

class Prepend(object):

    def __init__(self, s):
        self.start = s

    def write(self, s):
        print(self.start + s)


def main():
    p = Prepend("+++ ")
    p.write("Hello")


if __name__ == "__main__":
    main()
