#!/usr/bin/env python3

def distinct_characters(L):
    char_dict = {}

    # Käydään sanalista läpi
    for word in L:
        char_dict[word] = len(set(word))

    return char_dict


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
