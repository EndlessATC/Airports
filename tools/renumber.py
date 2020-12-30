import argparse
import re

header_re = re.compile(r"^(?:\[(?P<header>(?:approach)|(?:transition)|(?:departure)|(?:area))\d*\])|^(?:route\d+ *= *)")


def main(args, file=None):

    def number_approach(match, indexes={'approach': 0, 'transition': 0, 'departure': 0, 'area': 0, 'route': 0}):
        header = match.group("header")
        if header:
            indexes['route'] = 0
        else:
            header = 'route'
        indexes[header] += 1
        return header == 'route' and f"{header}{indexes[header]} = " or f"[{header}{indexes[header]}]"

    if file is None:
        file = args.airport_file

    result = []

    with open(file, 'r', newline='') as airport_file:
        for line in airport_file:
            result.append(header_re.sub(number_approach, line))

    with open(file, 'w', newline='') as airport_file:
        airport_file.writelines(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Re-number [approach] sections for Endless ATC airport files.')
    parser.add_argument('airport_file')

    main(parser.parse_args())
