#!/usr/bin/env python3

def extract_numbers(s):

    result = []

    for item in s.split(' '):
        try:
            # yritetään muuntaa kokonaisluvuksi
            integer = int(item)
            result.append(integer)

        except ValueError:
            try:
                # yritetään muuntaa floatiksi
                decimal = float(item)
                result.append(decimal)

            except ValueError:
                continue

    return result


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
