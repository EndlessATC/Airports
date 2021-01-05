import argparse
import re

"""Endless ATC custom airport file section renumbering utility."""


def process(args, file=None):
    """Rewrites an Endless ATC airport file with renumbered sections.

    Sections are renumbered from 1. Sections do not need to be numbered
    in the input. Routes, however, need to be numbered in the input.

    Args:
        `args`: An `argparse.Namespace`. The command line args from the invoking module.
        `file`: The file to process. Defaults to `input_file` in `args`."""

    header_re = re.compile(r"^(?:\[(?P<header>(?:approach)|(?:transition)|(?:departure)|(?:area))\d*\])|^(?:route\d+ *= *)")

    def number_approach(match, indexes={'approach': 0, 'transition': 0, 'departure': 0, 'area': 0, 'route': 0}):
        header = match.group("header")
        if header:
            indexes['route'] = 0
        else:
            header = 'route'
        indexes[header] += 1
        return header == 'route' and f"{header}{indexes[header]} = " or f"[{header}{indexes[header]}]"

    if file is None:
        file = args.input_file

    result = []

    with open(file, 'r', newline='') as input_file:
        for line in input_file:
            result.append(header_re.sub(number_approach, line))

    with open(file, 'w', newline='') as output_file:
        output_file.writelines(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Re-number [approach] sections for Endless ATC airport files.')
    parser.add_argument('input_file')

    process(parser.parse_args())
