import argparse
from collections import namedtuple
import configparser
import os
import re

"""Endless ATC custom airport file build utility."""


class Fix(namedtuple("Point", ['name', 'lat', 'lon', 'heading', 'pronunciation'])):
    """Simple `namedtuple` to represent a fix."""

    @property
    def short_def(self):
        """Position definition as string."""
        return f"{self.lat}, {self.lon}"

    @property
    def minor_def(self):
        """Definition without holding as string."""
        return f"{self.name}, {self.lat}, {self.lon}, {self.pronunciation}"

    @property
    def full_def(self):
        """Full definition as string."""
        return f"{self.name}, {self.lat}, {self.lon}, {self.heading}, {self.pronunciation}"


Airline = namedtuple("Airline", ['callsign', 'frequency', 'types', 'pronunciation', 'directions'])
"""Simple `namedtuple` to represent an airline declaration."""


def process_fix_list(fix_list, fixes):
    """Expands special commands in a list of fixes in short format
    and produces an iterable of definitions as the result.

    Substitute any "!<name>[, <extra_data>]" in `fix_list` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    Args:
        `fix_list` (list): A list of fix definitions.
        `fixes` (dict): A lookup of `Fix`es."""
    for line in fix_list:
        if line.startswith('!'):
            def_fix, def_sep, def_data = line.lstrip('!').partition(',')
            yield fixes[def_fix.strip()].short_def + def_sep + def_data
        else:
            yield line


def process_approach_fix_list(fix_list, fixes, tagged_routes):
    """Processes special commands in a list of departure fixes
    in short format and produces an iterable of definitions as the result.

    Substitute any "!<name>[, <extra_data>]" in `fix_list` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    If the last item in `fix_list` is "@<name>", substitute in
    the contents of the approach route tagged <name>.

    Args:
        `fix_list` (list): A list of fix definitions.
        `fixes` (dict): A lookup of `Fix`es.
        `tagged_routes` (dict): A lookup of approach routes."""
    if fix_list:
        if fix_list[0].startswith('@'):
            tagged_routes[fix_list[0].lstrip('@')] = fix_list[2:]
            fix_list = fix_list[1:]
        if fix_list[-1].startswith('@'):
            yield from process_fix_list(fix_list[:-1], fixes)
            yield from process_approach_fix_list(tagged_routes[fix_list[-1].lstrip('@')], fixes, tagged_routes)
        else:
            yield from process_fix_list(fix_list, fixes)


def process_departure_fix_list(fix_list, fixes, tagged_routes):
    """Processes special commands in a list of departure fixes
    in short format and produces an iterable of definitions as the result,
    or `None` if there is no result (fix_list was recorded in `tagged_routes`.

    Substitute any "!<name>[, <extra_data>]" in `fix_list` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    If and the first item of fix_list is "@<name>",
    record the rest of the `fix_list` in `tagged_routes` under "name".

    If the second (first if a tagged departure route) item in `fix_list`
    is "@<name>", substitute in the contents of the departure route
    tagged <name>.

    Args:
        `fix_list` (list): A list of fix definitions.
        `fixes` (dict): A lookup of `Fix`es.
        `tagged_routes` (dict): A lookup of departure routes."""
    if fix_list:
        if fix_list[0].startswith('@'):
            tagged_routes[fix_list[0].lstrip('@')] = fix_list[1:]
            return None
        else:
            return _process_departure_fix_list(fix_list, fixes, tagged_routes)


def _process_departure_fix_list(fix_list, fixes, tagged_routes, top_level=True):
    if fix_list:
        if top_level:
            yield fix_list[0]
            fix_list = fix_list[1:]
        if fix_list[0].startswith('@'):
            yield from _process_departure_fix_list(tagged_routes[fix_list[0].lstrip('@')], fixes, tagged_routes, top_level=False)
            yield from process_fix_list(fix_list[1:], fixes)
        else:
            yield from process_fix_list(fix_list, fixes)


def process_sids_fix_list(fix_list, fixes):
    """Processes special commands in a list of fixes in minor format
    and produces an iterable of definitions as the result.

    Substitute any "!<name>[, <extra_data>]" in `fix_list` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    Args:
        `fix_list` (list): A list of fix definitions.
        `fixes` (dict): A lookup of `Fix`es."""
    for line in fix_list:
        if line.startswith('!'):
            def_fix, def_sep, def_data = line.lstrip('!').partition(',')
            yield fixes[def_fix.strip()].minor_def + def_sep + def_data
        else:
            yield line


def process_repeatable_departure_fix_list(fix_list, fixes, departure_routes):
    """`Processes special commands in a list of departure fixes
    in short format and produces an iterable of n iterables of
    definitions as the result.

    If the first item of `fix_list` is *n, n iterables are produced.
    Otherwise, `n = 1`.

    See `process_departure_fix_list` for further special commands."""
    if fix_list[0].startswith('*'):
        result = list(process_departure_fix_list(fix_list[1:], fixes, departure_routes))
        for i in range(int(fix_list[0].removeprefix('*'))):
            yield result
    else:
        yield process_departure_fix_list(fix_list, fixes, departure_routes)


def process_beacons(fixes):
    """Returns a generator of [airspace] beacons= lines, while removing any
    beacons with ! as the holding heading."""
    for fix in fixes.values():
        if not fix.heading.startswith("!"):
            yield fix.full_def


def process_airlines_list(airline_list):
    """Returns generator of airline declaration strings based on the list of `Airline`s `airline_list`.

    If frequency is greater than 10, write floor(frequency / 10) 10 frequency
    declarations and 1x (frequency mod 10) declaration."""
    for airline in airline_list:
        n, r = divmod(int(airline.frequency), 10)
        for i in range(n):
            yield f"{airline.callsign}, 10, {airline.types}, {airline.pronunciation}, {airline.directions}"
        if r:
            yield f"{airline.callsign}, {r}, {airline.types}, {airline.pronunciation}, {airline.directions}"


def enumerate_routes(route_list, start=1):
    """built-in `enumerate()` but the enumeration is a string "route#"."""
    for route in route_list:
        yield f"route{start}", route
        start += 1


def process(args, input_file=None):
    """Parses an Endless ATC custom airport "source" file and expands certain special commands,
    then rewrites as a minimized output suitable for use by the game.

    Refer to argparse help for detailed syntax of special commands.

    Args:
        `args`: An `argparse.Namespace`. The command line args from the invoking module.
        `file`: The file to process. Defaults to `input_file` in `args`."""

    # if input_file is None, we were invoked standalone and not from deploy.py
    if input_file is None:
        input_file = args.input_file
        output_file = input_file if args.output_file is None else args.output_file
    else:
        output_file = os.path.join(os.path.dirname(input_file), args.output_path, os.path.basename(input_file))
    print(f"Building {input_file} to {output_file}")

    if 'legacy' not in args or not args.legacy:
        config = configparser.ConfigParser()
        config.read(input_file)

        # read optional header to be written in output
        header = None
        if 'meta' in config and 'header' in config['meta']:
            header = ["# " + line for line in config['meta']['header'].splitlines()]
            header.extend([
                "",
                f"# This file is generated from the source file {os.path.relpath(input_file, os.path.dirname(output_file))} using expand.py.",
                "# All comments have been stripped, and edits are not made directly to this file.",
                "# If you would like to contribute, or see the author's comments, please refer to the source file.",
                "",
                ""])
            header = "\n".join(header)
            # remove meta section so it won't be written in output
            del config['meta']

        # build a fix database from [airspace] beacons=
        fixes = {fix.name: fix for fix in (
            Fix(*map(str.strip, definition.split(","))) for definition in
            config['airspace']['beacons'].strip().splitlines()
        )}

        config['airspace']['beacons'] = "\n".join(process_beacons(fixes))

        config['airspace']['boundary'] = "\n".join(
            process_fix_list(config['airspace']['boundary'].splitlines(), fixes))

        # process airport sections
        airports = {section: config[section] for section in config if section.startswith('airport')}

        for airport_data in airports.values():

            if 'airlines' in airport_data:
                airlines = [Airline(*(value.strip() for value in airline.split(",")))
                    for airline in airport_data['airlines'].splitlines() if airline]
                airport_data['airlines'] = "\n".join(process_airlines_list(airlines))

            if 'sids' in airport_data:
                airport_data['sids'] = "\n".join(
                    process_sids_fix_list(airport_data['sids'].splitlines(), fixes))

        # process approach/transition sections
        approaches = [config[section] for section in config
            if section.startswith('approach') or section.startswith('transition')]
        tagged_approaches = {}

        for approach_data in approaches:
            if 'beacon' in approach_data and approach_data['beacon'].startswith("!"):
                approach_data['beacon'] = fixes[approach_data['beacon'].removeprefix("!")].full_def
            for option in approach_data:
                if option.startswith('route'):
                    approach_data[option] = "\n".join(process_approach_fix_list(approach_data[option].splitlines(),
                        fixes, tagged_approaches))

        # process departure sections
        departures = [config[section] for section in config if section.startswith('departure')]
        tagged_departures = {}

        for departure_data in departures:
            routes = {int(option.removeprefix('route')): departure_data[option]
                for option in departure_data if option.startswith('route')}
            processed_routes = []
            for route_index in sorted(routes):
                processed_routes.extend("\n".join(route) for route in
                    process_repeatable_departure_fix_list(
                        routes[route_index].splitlines(), fixes, tagged_departures)
                    if route)
                del departure_data[f'route{route_index}']
            departure_data.update(enumerate_routes(processed_routes, start=1))

        # write output file
        with open(output_file, 'w', newline='') as airport_file:
            airport_file.write(header)
            config.write(airport_file)

    # legacy processor in regex. Don't use for new projects.
    else:
        pattern = re.compile(r"^(?P<airport_section>\[airport(?P<airport_id>\d*)\])|(?P<airline_entry>#!\t(?P<airline_code>[-\w]*), (?P<airline_frequency>\d*), (?P<airline_parameters>[\w/d]*, [-\w ]*, [nswe]*))|(?P<result_marker>#!expansionoutput(?P<result_id>\d+))|(?P<result_end_marker>#!expansionoutputend)|(?P<sid_marker>#!sid(?P<sid_frequency>[\d]+)x)")

        result = {'output': []}
        airport = 0
        ignore_lines = False
        ignore_one_line = False
        sid_frequency = 0
        sid_lines = []

        with open(input_file, 'r', newline='') as airport_file:
            for line in airport_file:
                match = pattern.match(line)
                if match:
                    if match['airport_section']:
                        airport = match['airport_id']
                        if airport not in result:
                            result[airport] = []

                    elif match['airline_entry']:
                        total_frequency = int(match['airline_frequency'])
                        frequencies = []
                        while total_frequency > 10:
                            frequencies.append(10)
                            total_frequency -= 10
                        frequencies.append(total_frequency)
                        for frequency in frequencies:
                            result[airport].append(
                                f"\t{match['airline_code']}, {frequency}, {match['airline_parameters']}\n"
                            )

                    elif match['result_marker']:
                        result['output'].append(line)
                        for result_line in result[match['result_id']]:
                            result['output'].append(result_line)
                        ignore_lines = True

                    elif match['result_end_marker']:
                        ignore_lines = False

                    elif match['sid_marker']:
                        sid_frequency = int(match['sid_frequency']) - 1
                        ignore_one_line = True

                if sid_frequency:
                    if line.isspace():
                        for _ in range(sid_frequency):
                            result['output'].extend(sid_lines)
                        sid_frequency = 0
                        sid_lines = []
                    elif not len(sid_lines):
                        sid_lines.append("\n")
                    else:
                        sid_lines.append(line)

                if not ignore_lines and not ignore_one_line:
                    result['output'].append(line)

                if ignore_one_line:
                    ignore_one_line = False

        with open(output_file, 'w', newline='') as airport_file:
            airport_file.writelines(result['output'])
    return output_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''Expands certain commands to allow for concise Endless ATC airport source files.
        \n\n
        Available functions:
        \n\n
        In [airspace] boundary= or the route= of an [approach/departure/transition], specify "!<name>" instead of lat, lon
        to substitute the lat, lon from the fix with the corresponding name in [airspace] beacons=. In [airport] sids=, "!<name>"
        can also be specified, and will become name, lat, lon instead.
        \n\n
        In [airport] airlines=, definitions with frequency >10 with be broken down into multiple definitions of frequency 10 or less.
        \n\n
        In a [approach/transition] route=, specify "@<name>" to "tag" the approach route. Any subsequent [approach] route= can then
        specify "@<name>" as the last point to chain the approach route tagged as "name" to the end.
        \n\n
        In a [departure] route=, specify "@<name>" to "tag" the route. This will remove the departure route from the resulting file
        (as it is an incomplete departure route). Any subsequent [departure] route= can then specify "@<name>" as the *first* point
        (second line, after the route name) to chain the departure route tagged as "name" to the beginning.
        \n\n
        *n as the first line of a [departure] route= value will repeat that route n times. Obviously, a repeated route= cannot be
        tagged as it wouldn't make any sense.''')
    parser.add_argument('input_file')
    parser.add_argument('output_file', nargs='?')
    parser.add_argument('-l', '--legacy', action="store_true",
        help='''Use legacy processing method. Don't use for new projects.
        \n\n
        #!expansionoutput<airport_id> can be inserted on its own line in a source file terminated by
        #!expansionoutputend on a following line. This block, which should remain empty, will be used
        to write the result of expanding any airline definitions in a #! comment. Any #! definitions
        with frequency greater are split into entries with max 10 frequency each.
        \n\n
        #!sid<n>x can be inserted before any "routex =" declaration in a [departure] section to repeat the
        route <n> times. This can be used to adjust the distribution of traffic on each SID. Note the
        numbering of each "route" will not be adjusted. See renumber.py for such operation.''')

    process(parser.parse_args())
