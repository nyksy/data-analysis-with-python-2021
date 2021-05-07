#!/usr/bin/env python3
def triple(num):
    return num * 3


def square(num):
    return num * num


def main():
    for i in range(1, 11):

        tripled = triple(i)
        squared = square(i)

        if squared > tripled:
            break
        print(f"triple({i})=={tripled} square({i})=={squared}")


if __name__ == "__main__":
    main()
