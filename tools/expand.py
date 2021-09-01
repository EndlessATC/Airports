import argparse
from collections import deque
import configparser
from copy import deepcopy
from dataclasses import dataclass
from itertools import chain
import glob
import os
import re
from typing import ClassVar, Optional

try:
    import pygeodesy
    from pygeodesy.dms import parseDMS, toDMS, F_SEC
    from pygeodesy.sphericalTrigonometry import LatLon
    from pygeodesy.utily import ft2m, m2NM
except ModuleNotFoundError as e:
    print(f"PyGeodesy could not be imported from name {e.name}. Advanced functions not available.")
    print("Proceeding to attempt build in basic mode.")
    pygeodesy = None

"""Endless ATC custom airport file build utility."""


@dataclass
class Fix:
    """Simple class to represent a fix."""
    name: str
    _lat: str
    _lon: str
    heading: str
    pronunciation: str
    _latlon: LatLon = None
    runway_heading_true: Optional[float] = None

    fixes: ClassVar = None
    _var: ClassVar[float] = 0
    _subclass_registry: ClassVar = {}

    @staticmethod
    def initialize(magvar):
        Fix.fixes = {}
        Fix._var = magvar

    @classmethod
    @property
    def special_prefixes(cls):
        return cls._subclass_registry.keys()

    @classmethod
    def __init_subclass__(cls, /, name_prefix=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if name_prefix is not None:
            for prefix in name_prefix:
                cls._subclass_registry[prefix] = cls

    def __new__(cls, name, *args, **kwargs):
        if name in cls.fixes:
            return cls.fixes[name]
        name_prefix = name[:1]
        if name_prefix in cls._subclass_registry:
            return object.__new__(cls._subclass_registry[name_prefix])
        else:
            return object.__new__(cls)

    def __init__(self, name, lat=None, lon=None, heading="", pronunciation="", *, latlon=None):
        self.name = name.strip()
        self._lat = lat and lat.strip()
        self._lon = lon and lon.strip()
        self.heading = heading.strip()
        self.pronunciation = pronunciation.strip()
        self._latlon = latlon
        Fix.fixes[self.name] = self

    @property
    def lat(self):
        if not self._lat:
            self._lat = toDMS(self._latlon.lat, form=F_SEC, prec=2, sep='.', pos='N', neg='S')
        return self._lat

    @property
    def lon(self):
        if not self._lon:
            self._lon = toDMS(self._latlon.lon, form=F_SEC, prec=2, sep='.', pos='E', neg='W')
        return self._lon

    @property
    def short_def(self):
        """Position definition as string."""
        return f"{self.lat}, {self.lon}"

    @property
    def minor_def(self):
        """Definition without holding as string."""
        if self.pronunciation:
            return f"{self.name}, {self.lat}, {self.lon}, {self.pronunciation}".rstrip(", ")
        return f"{self.name}, {self.lat}, {self.lon}"

    @property
    def full_def(self):
        """Full definition as string."""
        if self.pronunciation:
            return f"{self.name}, {self.lat}, {self.lon}, {self.heading.lstrip('!') or 0}, {self.pronunciation}".rstrip(", ")
        elif self.heading.lstrip('!'):
            return f"{self.name}, {self.lat}, {self.lon}, {self.heading.lstrip('!')}"
        return f"{self.name}, {self.lat}, {self.lon}"

    @property
    def latlon(self):
        if self._latlon:
            return self._latlon
        self._generate_latlon()
        return self._latlon

    def _generate_latlon(self):
        try:
            lat = self._lat
            lon = self._lon
            if lat[:1].isalpha():
                lat = lat[1:] + lat[:1]
            if lon[:1].isalpha():
                lon = lon[1:] + lon[:1]
            if lat.find('.') != lat.rfind('.'):
                lat = parseDMS(lat, sep='.')
            if lon.find('.') != lon.rfind('.'):
                lon = parseDMS(lon, sep='.')
            self._latlon = LatLon(lat, lon)
        except Exception as e:
            raise RuntimeError(f"Unable to generate a LatLon for fix {self.name}: {self}") from e

    def heading_to(self, other, true_heading=False):
        return self.latlon.initialBearingTo(Fix.fixes[other].latlon) + (0 if true_heading else -Fix._var)

    def meters_on_heading(self, meters, heading, true_heading=False):
        if isinstance(heading, str):
            heading = heading.lstrip('!')
            match = re.match(r'RWYHDG(?:(?P<operation>[+-])(?P<offset>\d{2,3}(?:\.\d+)?))?$', heading)
            if match is not None:
                if self.runway_heading_true is None:
                    raise RuntimeError(
                        f'tried creating fix {meters}m on {heading} from {self.name} but {self.name} is not derived from a runway.')
                heading = self.runway_heading_true
                if match['operation']:
                    if match['operation'] == '+':
                        heading += float(match['offset'])
                    elif match['operation'] == '-':
                        heading -= float(match['offset'])
                    heading %= 360
                true_heading = True
            elif heading.endswith('T'):
                true_heading = True
                heading = heading[:-1]
            heading = float(heading)
        if not true_heading:
            heading += Fix._var
        result = self.latlon.destination(meters, heading)
        if self.runway_heading_true:
            result.runway_heading_true = self.runway_heading_true
        return result

    def km_on_heading(self, km, heading, true_heading=False):
        return self.meters_on_heading(km * 1000, heading, true_heading)

    def nmi_on_heading(self, nmi, heading, true_heading=False):
        return self.meters_on_heading(nmi * 1852, heading, true_heading)

    def intersect(self, radial, other_fix, other_radial, radial_true=False, other_radial_true=False):
        """Calculate the intersect of a line 'A' involving this point and another line 'B'.

        If `radial` is not a numeric string (optionally ending in T),
        line 'A' is the line between this point and the point named `radial`.

        Otherwise, lina 'A' is the line extending from this `Fix` on heading `radial`.
        If radial ends in 'T', the heading is a true heading.

        If `other_radial` is not a numeric string (optionally ending in T),
        line 'B' is the line between the `Fix` named `other_fix` and the `Fix` named `other_radial`.

        Otherwise, lina 'B' is the line extending from this `Fix` on heading `other_radial`.
        If radial ends in 'T', the heading is a true heading.

        Args:
            `radial`: A heading as a string, optionally ending in 'T', or the name of a `Fix`.
            `other_fix`: The name of a `Fix` as a string.
            `other_radial`: A heading as a string, optionally ending in 'T', or the name of a `Fix`.
            `radial_true`: Whether `radial` is a true heading. Defaults to `False`.
            `other_radial_true`: Whether `other_radial` is a true heading. Defaults to `False`.
        """
        if radial.endswith('T') and radial[:-1].replace('.', '', 1).isdigit():
            radial_true = True
            radial = radial[:-1]

        if other_radial.endswith('T') and other_radial[:-1].replace('.', '', 1).isdigit():
            other_radial_true = True
            other_radial = other_radial[:-1]

        if radial.replace('.', '', 1).isdigit():
            radial = float(radial)
            if not radial_true:
                radial += Fix._var
        else:
            radial = Fix.fixes[radial].latlon

        if other_radial.replace('.', '', 1).isdigit():
            other_radial = float(other_radial)
            if not other_radial_true:
                other_radial += Fix._var
        else:
            other_radial = Fix.fixes[other_radial].latlon

        result = self.latlon.intersection(radial, other_fix.latlon, other_radial)

        if m2NM(self.latlon.distanceTo(result)) > 300:
            result = result.antipode()

        return result

    def intersects(self, radius, other_fix, other_radius):
        radius = float(radius)
        other_radius = float(other_radius)

        return self.latlon.intersections2(radius, other_fix.latlon, other_radius)

    def intersects_nmi(self, radius, other_fix, other_radius):
        radius = float(radius) * 1852
        other_radius = float(other_radius) * 1852
        return self.intersects(radius, other_fix, other_radius)

    def is_hidden(self):
        return self.heading.startswith("!")


class RunwayFix(Fix, name_prefix="="):

    def __init__(self, runway_id, runway_designator, runway_heading_true, runway_length_meters, *args, **kwargs):
        self.runway_id = runway_id
        self.runway_designator = runway_designator
        self.runway_heading_true = runway_heading_true
        self.runway_length_meters = runway_length_meters
        super().__init__('=' + self.runway_id + self.runway_designator, *args, **kwargs)

    def reciprocal(self):
        if self.runway_designator[-1].isalpha():
            reciprocal_runway_designator = str((int(self.runway_designator[:-1]) + 18) % 36).rjust(2, '0')
            if self.runway_designator[-1] in 'Ll':
                reciprocal_runway_designator += 'R'
            elif self.runway_designator[-1] in 'Rr':
                reciprocal_runway_designator += 'L'
            else:
                reciprocal_runway_designator += self.runway_designator[-1]
        else:
            reciprocal_runway_designator = str((int(self.runway_designator) + 18) % 36).rjust(2, '0')

        reciprocal_runway_id = '=' + self.runway_id + reciprocal_runway_designator

        if reciprocal_runway_id in Fix.fixes:
            return Fix.fixes[reciprocal_runway_id]

        reciprocal_runway_latlon = self.meters_on_heading(self.runway_length_meters, self.runway_heading_true, True)
        reciprocal_runway_heading_true = (self.runway_heading_true + 180) % 360
        return RunwayFix(self.runway_id, reciprocal_runway_designator,
            reciprocal_runway_heading_true, self.runway_length_meters, latlon=reciprocal_runway_latlon)

    @classmethod
    def from_definition(cls, runway_definition):
        runway_data = runway_definition.split(',')
        runway_id = runway_data[0].strip()
        runway_designator = runway_data[1].strip()
        runway_lat = runway_data[2]
        runway_lon = runway_data[3]
        runway_heading_true = float(runway_data[4].strip())
        runway_length_meters = ft2m(float(runway_data[5].strip()))
        return RunwayFix(runway_id, runway_designator, runway_heading_true, runway_length_meters, lat=runway_lat, lon=runway_lon)

    def is_hidden(self):
        return True


class RadialDMEFix(Fix, name_prefix="@"):

    def __init__(self, name, fix=None, distance=None, radial=None, heading="!", pronunciation=""):
        if fix is None:
            try:
                match = re.match(r'@(?P<fix>[a-zA-Z0-9]+)(?P<radial>\d{3}[Tt]?)D(?P<distance>[0-9]+(?:\.[0-9]+)?)', name)
                fix = match['fix']
                distance = float(match['distance'])
                radial = match['radial']
                pronunciation = f"{Fix.fixes[fix].pronunciation} {heading} Radial {distance} D-M-E"
            except Exception as e:
                raise RuntimeError(f"failed to create fix from {name}") from e
        else:
            name = name.strip('@')
            fix = fix.strip()
            distance = float(distance.strip().lstrip('D'))
            radial = radial.strip()
            heading = heading.strip()
        latlon = Fix.fixes[fix].nmi_on_heading(distance, radial)
        self.runway_heading_true = getattr(latlon, 'runway_heading_true', None)
        super().__init__(name, heading=heading, pronunciation=pronunciation, latlon=latlon)


class RadialIntersectFix(Fix, name_prefix='#+'):

    def __init__(self, name, fix1=None, radial1=None, fix2=None, radial2=None, heading="!", pronunciation=""):
        try:
            if fix1 is None:
                match = re.match(r'[#+](?P<fix1>[a-zA-Z0-9]+)(?P<radial1>\d{3})@?(?P<fix2>[a-zA-Z0-9]+)(?P<radial2>\d{3})', name)
                fix1 = match['fix1']
                radial1 = match['radial1']
                fix2 = match['fix2']
                radial2 = match['radial2']
                pronunciation = f'{Fix.fixes[fix1].pronunciation} Radial {"-".join(radial1)} at ' + \
                    f'{Fix.fixes[fix2].pronunciation} Radial {"-".join(radial2)}'

            else:
                name = name.strip('#+')
                fix1 = fix1.strip()
                radial1 = radial1.strip()
                fix2 = fix2.strip()
                radial2 = radial2.strip()

            super().__init__(name, heading=heading, pronunciation=pronunciation,
                latlon=Fix.fixes[fix1].intersect(radial1, Fix.fixes[fix2], radial2))
        except Exception as e:
            raise RuntimeError(f"failed to create fix from {name}") from e


class CircleIntersectFix(Fix, name_prefix='&'):

    def __init__(self, name, fix1=None, radius1=None, fix2=None, radius2=None, direction=None, heading="!", pronunciation=""):
        try:
            if fix1 is None:
                match = re.match(r'&(?P<fix1>[a-zA-Z0-9]+)D(?P<radius1>[0-9]+(?:\.[0-9]+)?)&?(?P<fix2>[a-zA-Z0-9]+)D(?P<radius2>[0-9]+(?:\.[0-9]+)?)\.(?P<direction>[NSWEnswe])', name)
                fix1 = match['fix1']
                radius1 = match['radius1']
                fix2 = match['fix2']
                radius2 = match['radius2']
                direction = match['direction']
            else:
                name = name.strip('%')
                fix1 = fix1.strip()
                radius1 = radius1.strip()
                fix2 = fix2.strip()
                radius2 = radius2.strip()

            latlon_1, latlon_2 = Fix.fixes[fix1].intersects_nmi(radius1, Fix.fixes[fix2], radius2)

            if direction is None:
                if latlon_1 is not latlon_2:
                    raise ValueError(f'''No selector direction specified for intersection of non-abutting circles.
intersect 1: {latlon_1}
intersect 2: {latlon_2}''')
                else:
                    latlon = latlon_1
            else:
                if direction in 'NnSs':
                    if direction in 'Nn':
                        latlon = latlon_1 if latlon_1.lat > latlon_2.lat else latlon_2
                    else:
                        latlon = latlon_1 if latlon_1.lat < latlon_2.lat else latlon_2
                else:
                    if direction in 'Ee':
                        latlon = latlon_1 if latlon_1.lon > latlon_2.lon else latlon_2
                    else:
                        latlon = latlon_1 if latlon_1.lon < latlon_2.lon else latlon_2

            super().__init__(name, heading=heading, pronunciation=pronunciation,
                latlon=latlon)
        except Exception as e:
            raise RuntimeError(f"failed to create fix from {name}") from e


@dataclass
class Airline:
    """Simple class to represent an airline declaration."""
    callsign: str
    frequency: int
    types: str
    pronunciation: str
    directions: str

    callsigns = None
    use_callsigns = True
    test_callsigns = False
    phonetic = None

    @classmethod
    def initialize(cls, callsigns, phonetic):
        cls.callsigns = callsigns
        cls.phonetic = phonetic

    def __init__(self, callsign, frequency, types, *data, gateways=None):
        """Create an airline from an entry in the airlines= list. `data` should be
        `(pronunciation, directions)`.

        If `Airline.callsigns` is defined, `pronunciation` should be omitted from `data`.

        If `gateways` is provided, `directions` becomes `arrival_gateways`, `departure_gateways`."""

        self.frequency = int(frequency.strip())
        self.types = types.strip()
        self.callsign = callsign.strip()
        try:
            if Airline.callsigns is not None and (Airline.use_callsigns or Airline.test_callsigns):
                if '-' not in callsign:
                    self.pronunciation = Airline.callsigns[callsign]
                else:
                    if callsign.endswith('-') and callsign.index('-') != callsign.rindex('-'):
                        unique = True
                        callsign = callsign[:-1]
                    else:
                        unique = False
                    # if length of key is more than 3, assume it is not registration
                    key = callsign[:callsign.index('-')]
                    self.callsign = callsign.strip('_')
                    # if key length is longer than 3 and key doesn't have match,
                    # we strip '_' to allow for mil callsigns with length <= 3
                    self.pronunciation = Airline.callsigns.get(key, key.strip('_')) if len(key) > 3 \
                        else Airline.callsigns.get(key, '0')
                    if unique:
                        midpoint = self.callsign.index('-')
                        if self.pronunciation != '0':
                            number = self.callsign[midpoint + 1:]
                            self.pronunciation += " " + " ".join([self.phonetic[digit] for digit in number])
                        self.callsign = self.callsign[:midpoint] + self.callsign[midpoint + 1:] + '-'

            if Airline.test_callsigns:
                print(f'{self.callsign}: {self.pronunciation}')
            if Airline.callsigns is None or not Airline.use_callsigns:
                self.pronunciation = data[0].strip()
                data = data[1:]
            if gateways is not None:
                arrival_gateways = {gateway.strip() for gateway in data[0].split("/")}
                departure_gateways = {gateway.strip() for gateway in data[1].split("/")}
                self.directions = "".join(sorted(
                    {gateways[gateway] for gateway in arrival_gateways | departure_gateways}))
            else:
                self.directions = data[0].strip()
        except Exception as e:
            raise ValueError(f'''Could not create airline from ({callsign}, {frequency}, {types}, {str(data)})
Callsign pronunciation lookup = {Airline.use_callsigns}''') from e

    def definition(self, frequency):
        return f"{self.callsign}, {frequency}, {self.types}, {self.pronunciation}, {self.directions}"


def process_fix_line(line, fixes):
    """Expands special commands for a fix definition in short format
    and returns the expanded definition as the result.

    Substitute "!<name>[, <extra_data>]" in `line` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    Args:
        `line` (list): A fix definition.
        `fixes` (dict): A lookup of `Fix`es."""
    if line.startswith('!'):
        try:
            def_fix, def_sep, def_data = line.lstrip('!').partition(',')
            def_fix = def_fix.strip()
            if def_fix[0] in Fix.special_prefixes:
                if def_fix not in fixes:
                    Fix(def_fix)
            if def_fix not in fixes:
                raise KeyError(f'Fix lookup failed: No fix defined with name {def_fix}')
            return fixes[def_fix].short_def + def_sep + def_data
        except Exception as e:
            raise RuntimeError(f'Failed to process line {line}') from e
    else:
        return line


def process_fix_list(fix_list, fixes):
    """Expands special commands in a list of fixes in short format
    and produces an iterable of definitions as the result.

    Substitute any "!<name>[, <extra_data>]" in `fix_list` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    Args:
        `fix_list` (list): A list of fix definitions.
        `fixes` (dict): A lookup of `Fix`es."""
    for line in fix_list:
        yield process_fix_line(line, fixes)


def fix_list_with_altitude(fix_list, altitude):
    for line in fix_list:
        if altitude is not None:
            yield line + ", " + altitude
            altitude = None
        else:
            yield line


def _generate_approach(heading, starting_fix):
    return {"heading": heading, "beacon": starting_fix, "route": []}


def _process_simple_approach_fix_list(fix_list, runway, fixes,
        tagged_routes, generated_approaches, current_tag, top_level=True):
    """Inner worker function for `process_approach_fix_list()`.

    Works the same as `process_fix_list`, but in addition, any fix definitions processed
    will be added to any generated approaches in `generated_approaches`. Also, any fixes
    processed will be checked for any approach generator parameters; if found, a new
    generated approach is added to `generated_approaches`. The route of such generated
    approach will also be added to `tagged_routes` if tagged in the fix definition.

    Args:
        `fix_list` (list): A list of fix definitions.
        `runway` (str): The runway this approach is for. If `None`, this is a multi-runway approach.
        `fixes` (dict): A lookup of `Fix`es.
        `tagged_routes` (dict): A lookup of approach routes that were tagged for lookup.
        `generated_approaches`: A dict keyed by runway of dicts of parameters to be used to generate
            derived approaches in post-processing.
        `generate_approaches`: Whether or not to process any approach generator commands.
        `debug` (bool): Whether to print debug information."""

    for line in fix_list:
        def_data, _, approach_generator_params = line.rpartition(',')
        if def_data and ('!' in approach_generator_params or '@' in approach_generator_params):
            fix_name, _, _ = def_data.partition(',')
            fix_name = fix_name.lstrip('!')
            heading, _, tag = approach_generator_params.lstrip(' !').partition('@')
            if top_level:
                generated_approach = _generate_approach(heading, fix_name)
                if tag:
                    generated_approach['tag'] = tag
                    tagged_routes[tag] = []
                generated_approaches[runway or current_tag].append(generated_approach)
        else:
            def_data = line
            if line.startswith("@"):
                print(f'''Warning: An @ reference {line} was found in the wrong place while processing:''',
                    f'''\n{fix_list}\nCheck output for unresolved @.''')
        try:
            result = process_fix_line(def_data, fixes)
            for generated_approach in generated_approaches[runway or current_tag]:
                generated_approach['route'].append(result)
                if top_level and 'tag' in generated_approach:
                    tagged_routes[generated_approach['tag']].append(line)
        except Exception as e:
            raise RuntimeError(f'''failed to process approach route {fix_list} for runway {runway}''') from e


def _process_approach_fix_list(fix_list, runway, fixes, tagged_routes,
        generated_approaches, current_tag=None, top_level=True, terminate=False, debug=False):
    """Inner worker function for `process_approach_fix_list`.

    Args:
        `fix_list` (list): A list of fix definitions.
        `runway` (tuple): The runway this approach is for. If `None`, this is a multi-runway approach.
            Otherwise, this should be a tuple of runway_id, <"," or "">, <" rev" or "">, e.g. the
            result of running partition on runway=.
        `fixes` (dict): A lookup of `Fix`es.
        `tagged_routes` (dict): A dict keyed by runway of dicts of approach routes
            that were tagged for lookup.
        `generated_approaches`: A dict keyed by runway of dicts of parameters
            to be used to generate derived approaches in post-processing.
        `top_level` (bool): Whether or not to process any approach generator commands.
        `terminate` (bool): Whether or not the route has already terminated.
        `debug` (bool): Whether to print debug information."""

    if debug:
        print(f"_process_approach_fix_list: processing route: {fix_list}")
    if fix_list[-1].startswith('@'):
        following_tags = (tag.strip().lstrip('@') for tag in fix_list[-1].split(','))

        if not terminate:
            _process_simple_approach_fix_list(fix_list[:-1], runway, fixes,
                tagged_routes[runway], generated_approaches, current_tag, top_level)

            if len(fix_list) > 1:
                last_fix = fix_list[-2].strip()
                terminate = last_fix.startswith('end') and last_fix.endswith('hold')
                if debug and terminate:
                    print(f"Terminating approach {fix_list}")

        for generated_approach in generated_approaches[runway or current_tag]:
            if 'tag' in generated_approach:
                tagged_routes[runway][generated_approach['tag']].append(fix_list[-1])
                del generated_approach['tag']

        for following_tag in following_tags:
            if following_tag.startswith('!'):
                remove_first_fix = True
                following_tag = following_tag.removeprefix('!')
            else:
                remove_first_fix = False
            if current_tag is not None and current_tag == following_tag:
                raise RuntimeError(f'''Unable to build as approach tagged as @{current_tag} is trying to reference itself.
The following is the route= contents after the @tag:
{fix_list}''')
            following_tag_runways = []
            for route_runway, route_tags in tagged_routes.items():
                if runway is not None and runway != route_runway:
                    continue
                if following_tag in route_tags:
                    following_tag_runways.append(route_runway)
                    if runway is None:
                        try:
                            generated_approaches[route_runway or following_tag] = [
                                deepcopy(generated_approach) for generated_approach in
                                generated_approaches[current_tag]]
                        except Exception as e:
                            raise RuntimeError(f'{generated_approaches}\n{fix_list}\n{runway}') from e
                        for generated_approach in generated_approaches[route_runway or following_tag]:
                            if 'tag' in generated_approach:
                                del generated_approach['tag']
            if not following_tag_runways:
                raise RuntimeError(f'''Unable to build as approach continuation couldn't be found.
There was no approach route tagged {following_tag} for {runway and "runway " + repr(runway) or "any runway"}.
The requesting approach route was {fix_list}''')
            for following_tag_runway in following_tag_runways:
                following_route = tagged_routes[following_tag_runway][following_tag]
                if remove_first_fix:
                    following_route = following_route[1:]

                if debug and terminate:
                    print(f"Connecting terminated approach {fix_list} to {following_route}")
                _process_approach_fix_list(following_route,
                    following_tag_runway, fixes, tagged_routes, generated_approaches, following_tag,
                    False, terminate=terminate, debug=debug)
    else:
        if terminate:
            if debug:
                print(f"Finalizing terminated approach with {fix_list}")
        else:
            _process_simple_approach_fix_list(fix_list, runway, fixes,
                tagged_routes[runway], generated_approaches, current_tag, top_level)

    return generated_approaches


def process_approach_fix_list(fix_list, runway, fixes, tagged_routes,
        starting_fix, debug=False):
    """Processes special commands in a list of approach fixes
    in short format and produces an iterable of definitions as the result.

    Substitute any "!<name>[, <extra_data>]" in `fix_list` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    If the last item in `fix_list` is "@<name>", substitute in
    the contents of the approach route tagged <name>. If `runway` is None,

    Args:
        `fix_list` (list): A list of fix definitions.
        `runway` (tuple): The runway this approach is for. If `None`, this is a multi-runway approach.
            Otherwise, this should be a tuple of runway_id, <"," or "">, <" rev" or "">, e.g. the
            result of running partition on runway=.
        `fixes` (dict): A lookup of `Fix`es.
        `tagged_routes` (dict): A dict keyed by runway of dicts of approach routes
            that were tagged for lookup.
        `starting_fix` (str): The name of the starting fix of this approach.
        `debug` (bool): Whether to print debug information."""

    if fix_list:
        while not fix_list[0]:
            fix_list = fix_list[1:]
        if debug:
            print(f"process_approach_fix_list: processing route: {fix_list}")
        if runway not in tagged_routes:
            tagged_routes[runway] = {}
        tagged_routes_for_runway = tagged_routes[runway]

        if fix_list[0].startswith('@'):
            tagged_route = fix_list[2:]
            if fix_list[0].startswith('@!'):
                tagged_route = tagged_route[1:]
            current_tag = fix_list[0].lstrip('@!')
            tagged_routes_for_runway[current_tag] = tagged_route
            fix_list = fix_list[1:]
        else:
            current_tag = None

        generated_approaches = {runway or current_tag: []}

        if starting_fix:
            generated_approaches[runway or current_tag].append(_generate_approach(fix_list[0], starting_fix))
            fix_list = fix_list[1:]

        return _process_approach_fix_list(fix_list, runway, fixes,
            tagged_routes, generated_approaches, current_tag, debug=debug)

    else:
        raise RuntimeError(f"Tried to process an empty approach route {fix_list} for runway {runway}")


def process_departure_fix_list(fix_list, runway, airport, fixes, tagged_routes, base_runway=None):
    """Processes special commands in a list of departure fixes
    in short format and produces an iterable of definitions as the result,
    or `None` if there is no result (fix_list was recorded in `tagged_routes`.

    Substitute any "!<name>[, <extra_data>]" in `fix_list` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    If the first item of fix_list is "@<name>",
    record the rest of the `fix_list` in `tagged_routes` under `runway` and "name".
    If the first item of fix_list is "@!<name>", this route is a common route.

    If the second (first if a tagged departure route) item in `fix_list`
    is "@<name>", substitute in the contents of the departure route
    tagged <name>.

    Args:
        `fix_list` (list): A list of fix definitions.
        `runway` (str): The runway this departure is for.
        `airport` (str): The airport this departure is for.
        `fixes` (dict): A lookup of `Fix`es.
        `tagged_routes` (dict): A lookup of tagged departure routes.
        `base_runway` (str): The runway to reference when looking up tagged routes."""
    if fix_list:
        if runway not in tagged_routes:
            tagged_routes[runway] = {}
        if airport not in tagged_routes:
            tagged_routes[airport] = {}
        if fix_list[0].startswith('@'):
            tag = fix_list[0].lstrip('@')
            if tag.startswith('!!'):
                tag_namespace = None
            elif tag.startswith('!'):
                tag_namespace = airport
            elif runway:
                tag_namespace = runway
            else:
                raise RuntimeError(f"departure tagged {tag} as a runway-specific route, but no runway was specified")
            tagged_routes[tag_namespace][tag] = fix_list[1:]
            return None
        else:
            if base_runway is not None:
                runway = base_runway
            return _process_departure_fix_list(fix_list, runway, airport, fixes, tagged_routes)


def _process_departure_fix_list(fix_list, runway, airport, fixes, tagged_routes, top_level=True, altitude=None):
    """Inner worker function for `process_departure_fix_list()`.
    This produces the actual generator with the route= lines.

    Args:
        `fix_list` (list): A list of fix definitions.
        `runway` (str): The runway this departure is for.
        `airport` (str): The airport this departure is for.
        `fixes` (dict): A lookup of `Fix`es.
        `tagged_routes` (dict): A lookup of departure routes.
        `altitude` (str): An altitude to append to the first departure fix."""
    if fix_list:
        try:
            if top_level:
                yield fix_list[0]
                fix_list = fix_list[1:]
                # climb altitude
                if fix_list[0].strip().isdigit():
                    if altitude is None:
                        altitude = fix_list[0].strip()
                    fix_list = fix_list[1:]
            if fix_list[0].startswith('@'):
                tag = fix_list[0].lstrip('@')
                if tag.startswith('!') and tag in tagged_routes[None]:
                    tagged_route = tagged_routes[None][tag]
                elif tag in tagged_routes[runway]:
                    tagged_route = tagged_routes[runway][tag]
                elif tag in tagged_routes[airport]:
                    tagged_route = tagged_routes[airport][tag]
                else:
                    raise KeyError(f'''Unable to find route tagged @{tag}.
tags for runway {runway}: {tagged_routes[runway]}
tags for airport {airport}: {tagged_routes[airport]}''')
                yield from _process_departure_fix_list(tagged_route,
                    runway, airport, fixes, tagged_routes, top_level=False, altitude=altitude)
                yield from _process_departure_fix_list(fix_list[1:],
                    runway, airport, fixes, tagged_routes, top_level=False)

            elif fix_list[-1].startswith('@'):
                tag = fix_list[-1].lstrip('@')
                if tag.startswith('!') and tag in tagged_routes[None]:
                    tagged_route = tagged_routes[None][tag]
                elif tag in tagged_routes[runway]:
                    tagged_route = tagged_routes[runway][tag]
                elif tag in tagged_routes[airport]:
                    tagged_route = tagged_routes[airport][tag]
                else:
                    raise KeyError(f'''Unable to find route tagged @{tag}.
tags for runway {runway}: {tagged_routes[runway]}
tags for airport {airport}: {tagged_routes[airport]}''')
                yield from _process_departure_fix_list(fix_list[:-1],
                    runway, airport, fixes, tagged_routes, top_level=False, altitude=altitude)
                yield from _process_departure_fix_list(tagged_route,
                    runway, airport, fixes, tagged_routes, top_level=False)

            else:
                if altitude is not None:
                    fix_list = fix_list_with_altitude(fix_list, altitude)
                yield from process_fix_list(fix_list, fixes)

        except Exception as e:
            raise RuntimeError(
                f"Could not process departure route {fix_list} for runway {runway}"
            ) from e


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


def process_entrypoints_list(entrypoints_list, fixes=None):
    """Processes special commands in a list of fixes in minor format
    and produces an iterable of definitions as the result.

    Substitute any "!<name>[, <extra_data>]" in `fix_list` with
    "lat, lon[, <extra_data>]" based on `fixes`.

    If `fixes` is provided, error checking will be done. Any problems
    will be printed to console.

    Args:
        `entrypoints_list` (list): A list of entrypoints definitions.
        `fixes` (dict): A lookup of `Fix`es."""
    for line in entrypoints_list:
        if not line.strip():
            yield line
            continue
        entrypoint_heading, _, entrypoint_definition = line.partition(',')
        entrypoint_fix, _, entrypoint_definition = entrypoint_definition.partition(',')
        entrypoint_fix = entrypoint_fix.strip()
        if entrypoint_fix not in fixes:
            print(f"Warning: entrypoint fix {entrypoint_fix} is not defined")
        elif fixes[entrypoint_fix].is_hidden():
            print(f"Warning: entrypoint fix {entrypoint_fix} is defined as a hidden fix")
        entrypoint_definition, _, entrypoint_last_parameter = line.rpartition(',')
        entrypoint_last_parameter = entrypoint_last_parameter.strip()
        if entrypoint_last_parameter.startswith('*'):
            for i in range(int(entrypoint_last_parameter.strip('*'))):
                yield entrypoint_definition
        else:
            yield line


def process_repeatable_departure_fix_list(fix_list, runway, airport, fixes, tagged_routes, base_runway=None):
    """`Processes special commands in a list of departure fixes
    in short format and produces an iterable of n iterables of
    definitions as the result.

    If the first item of `fix_list` is *n, n iterables are produced.
    Otherwise, `n = 1`.

    See `process_departure_fix_list` for further special commands.

    Args:
        `fix_list` (list): A list of fix definitions.
        `runway` (str): The runway this departure is for.
        `airport` (str): The airport this departure is for.
        `fixes` (dict): A lookup of `Fix`es.
        `tagged_routes` (dict): A lookup of tagged departure routes.
        `base_runway` (str): The runway to reference when looking up tagged routes."""
    if not fix_list[0]:
        fix_list = fix_list[1:]
    if fix_list[0].startswith('*'):
        result = list(process_departure_fix_list(fix_list[1:], runway, airport,
            fixes, tagged_routes, base_runway))
        for i in range(int(fix_list[0].removeprefix('*'))):
            yield result
    else:
        yield process_departure_fix_list(fix_list, runway, airport,
            fixes, tagged_routes, base_runway)


def process_beacons(fixes):
    """Returns a generator of [airspace] beacons= lines from a list of fixes.

    Fixes marked not to be exported are omitted."""
    for fix in fixes.values():
        if not fix.is_hidden():
            yield fix.full_def


def process_handoffs(handoffs, center):

    """Processes fix references in [airspace] handoff=.

    Returns a generator of processed [airspace] handoff= lines."""
    for handoff in handoffs.strip().splitlines():
        direction, separator, parameters = handoff.partition(',')
        if direction.startswith('!'):
            direction = str(int(center.heading_to(direction[1:])))
        yield ",".join([direction, parameters]).rstrip(", ")


def process_airlines_list(airline_list):
    """Returns generator of airline declaration strings based on the list of `Airline`s `airline_list`.

    If frequency is greater than 10, write floor(frequency / 10) 10 frequency
    declarations and 1x (frequency mod 10) declaration."""
    for airline in airline_list:
        n, r = divmod(airline.frequency, 10)
        for i in range(n):
            yield airline.definition(10)
        if r:
            yield airline.definition(r)


def enumerate_routes(route_list, start=1):
    """built-in `enumerate()` but the enumeration is a string "route#"."""
    for route in route_list:
        yield f"route{start}", route
        start += 1


def process(args, input_file=None, preprocessed_input=None):
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
    source = configparser.ConfigParser()
    if preprocessed_input is None:
        source.read(input_file)
    else:
        source.read_file(preprocessed_input, input_file)

    config = configparser.ConfigParser()
    config.read("common.ini")

    # read optional header to be written in output
    header = ''
    if 'meta' in source:
        if 'header' in source['meta']:
            header = ["# " + line for line in source['meta']['header'].splitlines()]
            header.extend([
                "",
                f"# This file is generated from the source file {os.path.relpath(input_file, os.path.dirname(output_file))} using expand.py.",
                "# All comments have been stripped, and edits are not made directly to this file.",
                "# If you would like to contribute, or see the author's comments, please refer to the source file.",
                "",
                ""])
            header = "\n".join(header)
        if 'callsigns' not in source['meta']:
            Airline.use_callsigns = False
        else:
            Airline.use_callsigns = source['meta'].getboolean('callsigns')
        if args.test_callsigns:
            Airline.test_callsigns = True
        if 'common_data' in source['meta']:
            for common_data_source in source['meta']['common_data'].splitlines():
                found = False
                common_data_filename = f"common_{common_data_source.strip()}.ini"
                for common_data_file in glob.glob(os.path.join(
                        args.input_dir,
                        "**",
                        args.source_dir,
                        common_data_filename), recursive=True):
                    if found:
                        raise RuntimeError(
                            f"Found more than one common data source {common_data_filename}")
                    config.read(common_data_file)
                    found = True
                if not found:
                    raise RuntimeError(f"Could not find common data source {common_data_filename}")
        # remove meta section so it won't be written in output
        del source['meta']
    Airline.initialize(config['expand.callsigns'] if 'expand.callsigns' in config else {},
        config['expand.phonetic'])
    default_gateways = config['expand.gateways'] if 'expand.gateways' in config else {}

    airspace = source['airspace']

    Fix.initialize(airspace.getfloat('magneticvar'))

    # add runways to fix database
    airports = {section: source[section] for section in source if section.startswith('airport')}
    if pygeodesy:
        for airport_data in airports.values():
            runways = airport_data['runways'].strip().splitlines()
            for runway_definition in runways:
                RunwayFix.from_definition(runway_definition).reciprocal()

    Fix('_CTR', *airspace['center'].split(","), heading='!')

    if 'beacons' in airspace:
        # build a fix database from [airspace] beacons=
        for definition in airspace['beacons'].strip().splitlines():
            Fix(*definition.split(","))

        airspace['beacons'] = "\n".join(process_beacons(Fix.fixes))

    if 'handoff' in airspace:
        airspace['handoff'] = "\n".join(process_handoffs(airspace['handoff'], Fix.fixes['_CTR']))

    if 'boundary' in airspace:
        airspace['boundary'] = "\n".join(
            process_fix_list(airspace['boundary'].splitlines(), Fix.fixes))

    areas = {section: source[section] for section in source if section.startswith('area')}

    for area_data in areas.values():
        if 'points' in area_data:
            area_data['points'] = "\n".join(
                process_fix_list(area_data['points'].splitlines(), Fix.fixes))
        if args.draw_all_areas and 'draw' in area_data:
            del area_data['draw']
        if 'position' in area_data:
            area_position = area_data['position'].strip()
            if area_position in Fix.fixes:
                area_data['position'] = Fix.fixes[area_position].short_def
        if 'labelpos' in area_data:
            area_position = area_data['labelpos'].strip()
            if area_position in Fix.fixes:
                area_data['labelpos'] = Fix.fixes[area_position].short_def

    # process airport sections
    runway_to_airport = {}

    for airport_data in airports.values():

        airport_code = airport_data['code']
        airport_code, _, airport_code_full = airport_code.partition(',')
        if airport_code_full:
            airport_data['code'] = airport_code
            airport_code = airport_code_full

        runways = airport_data['runways'].strip().splitlines()
        for runway_definition in runways:
            runway_id, _, _ = runway_definition.partition(',')
            runway_to_airport[runway_id] = airport_code.strip()

        gateways = dict((tuple(map(str.strip, gateway.split(","))) for gateway in airport_data['gateways'].strip().splitlines()),
            **default_gateways) if 'gateways' in airport_data else None

        if 'airlines' in airport_data:
            airlines = [Airline(*airline.split(","), gateways=gateways)
                for airline in airport_data['airlines'].splitlines() if airline]
            airport_data['airlines'] = "\n".join(process_airlines_list(airlines))

        if 'sids' in airport_data:
            airport_data['sids'] = "\n".join(
                process_sids_fix_list(airport_data['sids'].splitlines(), Fix.fixes))

        if 'entrypoints' in airport_data:
            airport_data['entrypoints'] = "\n".join(
                process_entrypoints_list(airport_data['entrypoints'].splitlines(), Fix.fixes))

    # process approach/transition sections
    approaches = {section: source[section] for section in source
        if section.startswith('approach') or section.startswith('transition')}
    tagged_approach_routes = {}
    generated_approaches = {}
    highest_app_index = 0
    discarded_approaches = deque()

    for approach_section, approach_data in approaches.items():
        approach_runway = approach_data.get('runway', fallback=None)
        approach_debug = approach_data.getboolean('debug')
        if approach_runway is not None:
            approach_runway_id, _, approach_runway_direction = approach_runway.partition(',')
            approach_runway = approach_runway_id.strip(), approach_runway_direction.strip()
        else:
            discarded_approaches.append(approach_section)
        if 'beacon' in approach_data and ',' not in approach_data['beacon']:
            approach_beacon = approach_data['beacon'].removeprefix("!")
            if approach_beacon in Fix.fixes and Fix.fixes[approach_beacon].heading.startswith('!'):
                approach_data['beacon'] = Fix.fixes[approach_beacon].full_def
            else:
                approach_data['beacon'] = approach_beacon
        else:
            approach_beacon = approach_data['beacon']
        for option in approach_data:
            if option.startswith('route'):
                new_generated_approaches = process_approach_fix_list(approach_data[option].splitlines(),
                     approach_runway, Fix.fixes, tagged_approach_routes, approach_beacon, approach_debug)
                if approach_runway is not None:
                    generated_approach = new_generated_approaches[approach_runway][0]

                    if generated_approach['beacon'] != approach_beacon:
                        raise RuntimeError(f'''Unexpected behaviour during approach processing.
A single runway approach generated an approach with a mismatched beacon.
Defined beacon was {generated_approach.beacon}, actual beacon was {approach_beacon}.''')

                    approach_data[option] = generated_approach['heading'] + "\n" + "\n".join(
                        generated_approach['route'])
                    new_generated_approaches[approach_runway] = new_generated_approaches[approach_runway][1:]
                for runway, new_generated_approaches_for_runway in new_generated_approaches.items():
                    if runway in generated_approaches:
                        generated_approaches[runway].extend(new_generated_approaches_for_runway)
                    elif isinstance(runway, tuple):
                        generated_approaches[runway] = new_generated_approaches_for_runway

    # find highest approach index as we need to add more approaches
    for section in source:
        if section.startswith('approach'):
            highest_app_index = max(highest_app_index, int(section[8:]))

    for runway, generated_approaches_for_runway in generated_approaches.items():
        for generated_approach in generated_approaches_for_runway:
            if not generated_approach['heading']:
                continue
            if discarded_approaches:
                section = discarded_approaches.popleft()
            else:
                highest_app_index += 1
                section = f'approach{highest_app_index}'
            beacon = generated_approach['beacon']
            if Fix.fixes[beacon].heading.startswith('!'):
                beacon = Fix.fixes[beacon].full_def
            source[section] = {
                "runway": ', '.join(runway),
                "beacon": beacon,
                "route1": generated_approach['heading'] + "\n" + "\n".join(
                    generated_approach['route'])
            }

    # process departure sections
    common_departures = [source[section] for section in sorted(source) if section.startswith('commondeparture')]
    departures = [source[section] for section in sorted(source) if section.startswith('departure')]
    tagged_departures = {None: {}}

    for departure_data in common_departures:
        if 'airport' not in departure_data:
            raise RuntimeError(f'''A [commondeparture] exists with no airport specified.''')

    for departure_data in chain(common_departures, departures):
        if 'airport' in departure_data:
            departure_airport = departure_data['airport']
            departure_runway = None
            departure_base_runway = None
        elif 'runway' not in departure_data:
            raise RuntimeError(f'''A departure exists with no runway. Aborting.
The contents of the departure section are as follows:
{"".join(departure_data.values())}''')
        else:
            departure_runway = departure_data['runway']
            departure_runway = departure_runway.partition(',')
            departure_airport = runway_to_airport[departure_runway[0]]
            departure_base_runway = departure_data.get('baserunway', fallback=None)
            if departure_base_runway is not None:
                departure_base_runway = departure_base_runway.partition(',')
                del departure_data['baserunway']
        routes = {int(option.removeprefix('route')): departure_data[option]
            for option in departure_data if option.startswith('route')}
        processed_routes = []
        for route_index in sorted(routes):
            processed_routes.extend("\n".join(route) for route in
                process_repeatable_departure_fix_list(
                    routes[route_index].splitlines(), departure_runway, departure_airport,
                    Fix.fixes, tagged_departures, departure_base_runway)
                if route)
            del departure_data[f'route{route_index}']
        departure_data.update(enumerate_routes(processed_routes, start=1))

    common_departures = [section for section in source if section.startswith('commondeparture')]
    for section in common_departures:
        del source[section]

    # write output file
    if not args.parse_only:
        with open(output_file, 'w', newline='') as airport_file:
            airport_file.write(header)
            source.write(airport_file)

    return output_file if not args.parse_only else None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''Expands certain commands to allow for concise Endless ATC airport source files.
        \n\n
        Available functions:
        \n\n
        In [airspace] boundary=, [area] points=, or the route= of an [approach/departure/transition], specify "!<name>" instead of lat, lon
        to substitute the lat, lon from the fix with the corresponding name in [airspace] beacons=. In [airport] sids=, "!<name>"
        can also be specified, and will become name, lat, lon instead. In [approach/departure/transition], "!<name>" can also be specified
        in beacon=, where it will become the full fix definition.
        \n\n
        In [airport] airlines=, definitions with frequency >10 with be broken down into multiple definitions of frequency 10 or less.
        \n\n
        In [airport], you can define gateways=, a list of <name>, direction. If gateways= is defined, the ", <directions>"" in
        [airport] airlines= becomes ", <arrival_gateways>, <departure_gateways>", and the directions are used based on the defined
        gateways. Default gateways can be specified in a common.ini in the same directory as the source file, or in the folder where
        this tool is located; gateways= still needs to be defined in an [airport] to activate this feature for the [airport].
        \n\n
        In [airport] airlines=, the airline <pronunciation> can be omitted if [meta] callsigns= is true. A lookup will be loaded from
        [expand.callsigns] defined in a common.ini in the same directory as the source file, or in the folder where this tool is
        located. The former takes precedence. [expand.callsigns] is a list of <code>, <pronunciation>. The first item in each
        line of airlines (stripped of a dash and anything after it, hereafter referred to as the "key") is used to lookup in
        [expand.callsigns] to obtain the pronunciation. If nothing is found, pronunication defaults to the key if it is longer than
        3 characters (assuming it is a military callsign), otherwise it defaults to "0".
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

    process(parser.parse_args())
