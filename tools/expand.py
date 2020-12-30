import argparse
import collections
import configparser
import os
import re

Fix = collections.namedtuple("Point", ['name', 'lat', 'lon', 'heading', 'pronunciation'])
Airline = collections.namedtuple("Airline", ['callsign', 'frequency', 'types', 'pronunciation', 'directions'])


def process_fix_list(fix_list, fixes):
    for line in fix_list:
        if line.startswith('!'):
            def_fix, def_sep, def_data = line.lstrip('!').partition(',')
            yield f"{fixes[def_fix.strip()].lat}, {fixes[def_fix.strip()].lon}" + def_sep + def_data
        else:
            yield line


def process_repeatable_fix_list(fix_list, fixes):
    if fix_list[0].startswith('*'):
        result = list(process_fix_list(fix_list[1:], fixes))
        for i in range(int(fix_list[0].removeprefix('*'))):
            yield result
    else:
        yield process_fix_list(fix_list, fixes)


def process_airlines_list(airline_list):
    for airline in airline_list:
        n, r = divmod(int(airline.frequency), 10)
        for i in range(n):
            yield f"{airline.callsign}, 10, {airline.types}, {airline.pronunciation}, {airline.directions}"
        if r:
            yield f"{airline.callsign}, {r}, {airline.types}, {airline.pronunciation}, {airline.directions}"


def enumerate_routes(route_list, start=1):
    for route in route_list:
        yield f"route{start}", route
        start += 1


def main(args, input_file=None):

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

        config['airspace']['boundary'] = "\n".join(
            process_fix_list(config['airspace']['boundary'].splitlines(), fixes))

        # process airport sections
        airports = {section: config[section] for section in config if section.startswith('airport')}

        for airport_data in airports.values():
            if 'airlines' in airport_data:
                airlines = [Airline(*(value.strip() for value in airline.split(",")))
                    for airline in airport_data['airlines'].splitlines() if airline]
                airport_data['airlines'] = "\n".join(process_airlines_list(airlines))

        # process approach/transition sections
        approaches = {section: config[section] for section in config
            if section.startswith('approach') or section.startswith('transition')}

        for approach in approaches.values():
            for option in approach:
                if option.startswith('route'):
                    approach[option] = "\n".join(process_fix_list(approach[option].splitlines(), fixes))

        # process departure sections
        departures = {section: config[section] for section in config if section.startswith('departure')}

        for departure_data in departures.values():
            routes = {option.removeprefix('route'): departure_data[option] for option in departure_data if option.startswith('route')}
            processed_routes = []
            for route_index in sorted(routes):
                processed_routes.extend("\n".join(route) for route in process_repeatable_fix_list(routes[route_index].splitlines(), fixes))
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
        in [airspace] boundary=, or the route= of an [approach/departure/transition], specify !<name> instead of lat, lon 
        to substitute the lat, lon from the fix with the corresponding name in [airspace] beacons=.
        \n\n
        in [airport] airlines=, definitions with frequency >10 with be broken down into multiple definitions of frequency 10 or less.
        \n\n
        *n as the first line of a [departure] route= value will repeat that route n times.''')
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

    main(parser.parse_args())