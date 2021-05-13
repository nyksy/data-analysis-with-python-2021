#!/usr/bin/env python3
import re


def integers_in_brackets(s):
    #palautetaan lista regexin löytämiä numeroja, ei oteta mukaan kirjaimia sisältäviä lukuja
    return [int(num) for num in re.findall(r'\[\s*(?:\+(?=\d))?(-?\d+)\s*]', s)] 


def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))


if __name__ == "__main__":
    main()
