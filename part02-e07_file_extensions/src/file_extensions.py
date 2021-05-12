#!/usr/bin/env python3

def file_extensions(filename):

    no_extensions = []
    extension_dict = {}

    with open(filename, 'r') as tiedosto:
        for rivi in tiedosto:
            
            #suodatetaan rivinvaihto pois
            rivi = rivi.replace('\n', '')
            formaatti = rivi.split('.')[-1]

            #mikäli formaatti löytyy
            if len(rivi.split('.')) > 1:
                extension_dict.setdefault(formaatti, []).append(rivi)
            else:
                no_extensions.append(rivi)

    return (no_extensions, extension_dict)


def main():
    extensions = file_extensions('src/filenames.txt')

    print(len(extensions[0]), 'files with no extension')
    for key, val in extensions[1].items():
        print(key, len(val))


if __name__ == "__main__":
    main()
