# Endless ATC Custom Airport Tools 0.13.0

In this directory are a few tools useful for writing Endless ATC airport files. You can see examples of its usage in `RJTT` and `RJBB`.

The tools are Python 3 scripts. They have not been tested in Python 2 and likely will not work. The tools have only been tested with Python 3.9. Python 3.5.3 or newer is likely required, but versions older than 3.9 have not been tested.

You will need PyGeodesy for full functionality. However, if the file being built does not use advanced functionality, you should be able to build without PyGeodesy installed (this is untested). To install PyGeodesy, (activate your `venv` if you don't want it installed to your system Python), then run `pip install PyGeodesy`.

Depending on your platform, you will need to run `python3 deploy.py`, `python deploy.py`, or possibly even `deploy.py` will work.

For further help, view the help available by running `python deploy.py -h`

If you find any bugs, you can report on the community Discord in the `#tools-python` channel. You can also ask for assistance there with using the tool.

## Features

This is an incomplete list; there are features that are not yet documented here.

### Build from source

Work from a source file that will be built into a product file readable by the game. The source file uses extensions on the game's existing syntax; any file readable by the game is also readable as a source file by the tools.

This allows writing custom airports in a much more human-readable form.

### Auto-numbering of sections and routes

Sections that are numbered will be renumbered. Such sections can also have numbering omitted. Routes will also be renumbered (and can have numbering omitted).

Applicable sections:

*	`[airport]`
*	`[area]`
*	`[approach]`
*	`[departure]`
*	`[transition]` (deprecated)
*	`route=`

### Header

The build process results in a fairly minimal file with no comments. To add a header, define it in `[meta]` of the source file:

```INI
[meta]
header = RJTT ACA 3.3.0
	See RJTT_readme.md
```

A message indicating this file was built using these tools and the location of the source file will be appended after the `header=` message:

```INI
# RJTT ACA 3.3.0
# See RJTT_readme.md

# This file is generated from the source file source\RJTT.txt using expand.py.
# All comments have been stripped, and edits are not made directly to this file.
# If you would like to contribute, or see the author's comments, please refer to the source file.
```

### Fix definitions and references

Fixes defined in `[airspace]` `beacons=` are stored in a database for reference elsewhere in the file.
If you specify `!` as the heading, the fix will be "hidden" and not be drawn on the map unless called for elsewhere in the file. A hold heading can be specified after the `!` if necessary.

Any fixes can be referenced by name later in the following areas using `!<fix_name>` instead of `<position>` unless indicated otherwise:

*	`[airspace]`
	-	`boundary=`
	-	`handoff=`
		- The heading from `[airspace] center=` to the specified fix will be substituted in
*	`[airport]`
	-	`sids=`
		- This is intended to be used for drawing "hidden" fixes on the map that aren't meant to be used by arrival aircraft, as you cannot issue DCT to these fixes
		- However, if you are not using `[departure]`s, then these will function as usual
*	`[area]`
	-	`position=`
	-	`points=`
	-	`labelpos=`
*	`[approach]`
	-	`route=`
		- Restrictions can be specified as normal
	-	`beacon=`
		- `!` is optional
		- If the referenced fix is "hidden", the fix definition will be substituted in, so that the fix is drawn on the map while the approach is available
*	`[departure]`
	-	`route=`

The `center=` of the TMA will be made available under the name `_CTR` as a hidden fix.

Example for `handoff=`:
```INI
handoff = 
#T13 (Musashi Sector)
	!KAGNA, Tokyo Control, Tokyo Control, 132.1
	!SEDRI, Tokyo Control, Tokyo Control, 132.1
	!MITOP, Tokyo Control, Tokyo Control, 132.1
	!DALMA, Tokyo Control, Tokyo Control, 292.4
#T03 (Kanto North Sector)
	!KIMIN, Tokyo Control, Tokyo Control, 124.1
	!AGRIS, Tokyo Control, Tokyo Control, 124.1
	!CLARK, Tokyo Control, Tokyo Control, 124.1
	!JD, Tokyo Control, Tokyo Control, 276.1
```

becomes:
```INI
handoff = 259, Tokyo Control, Tokyo Control, 132.1
	267, Tokyo Control, Tokyo Control, 132.1
	275, Tokyo Control, Tokyo Control, 132.1
	261, Tokyo Control, Tokyo Control, 292.4
	359, Tokyo Control, Tokyo Control, 124.1
	350, Tokyo Control, Tokyo Control, 124.1
	336, Tokyo Control, Tokyo Control, 124.1
	348, Tokyo Control, Tokyo Control, 276.1
```

### Multiplying entry points

```INI
entrypoints = 
#Following line will be repeated 10 times (without the ", *10" at the end)
	242, SPENS, 22000, *10
#Following line will be repeated 6 times (without the ", *6" at the end)
	223, SELNO, 23000, *6
	123, DOLBA, 22000
	193, TOPIT, 22000
#Following line will be repeated 7 times (without the ", *7" at the end)
	359, TEDIX, 16000, *7
	64, LALID, 16000
```

### Airlines

Airlines definitions with a frequency greater than 10 will be split into multiple definitions with frequency 10 or less.

```INI
#The below will result in 30 lines of "ana, 10, b763, ..." and 10 lines of "ana, 10, b77l, w"
#The a124 lines will remain the same as they are less than 10 frequency
airlines = 
	ana, 300, b763, all nippon, w
	ana, 100, b77l, all nippon, w
	vda, 5, a124, volga, nswe
	adb, 1, a124, antonov, nswe
```

### Auto airlines callsigns

If callsigns is enabled in meta, callsigns can be omitted in `airlines=`. They will be resolved using the list in the base data source, the `common.ini` in the directory where these tools are located. 
You can override these callsign definitions (or add local callsigns) in a common data source, which can be called upon by a source file by specifying a list of names in `[meta] common_data=`. A file `common_<name>.ini` will be searched for in a source directory under the input directory and loaded to overwrite any declarations in the base data source.

```INI
[meta]
header = RJTT ACA 3.3.0
	See RJTT_readme.md
callsigns = True
```
common.ini:
```INI
[expand.callsigns]
cygns = cygnus
#if the callsign code portion is less than 2 characters, add an underscore prefix to make it 3 characters
_jf = japan force
```

Then in your source file:
```INI
airlines = 
	cygns-1, 10, b77w, nswe
#if the callsign code portion is less than 2 characters, add an underscore prefix to make it 3 characters
	_jf-1, 10, b77w, nswe
```
Which becomes:
```INI
airlines = 
	cygns-1, 10, b77w, cygnus, nswe
	jf-1, 10, b77w, japan force, nswe
```


### Unique aircraft callsign resolution (requires `callsigns = True`)

You can define callsigns with two dashes, one at the end. This will result in a "unique" aircraft of which only one can appear at a time:
```INI
airlines = 
	gaf-1-, 1, a343, nw
	_jf-1-, 10, b77w, nswe
```
becomes:
```INI
airlines = 
	gaf1-, 1, a343, german air force one, nw
	jf1-, 10, b77w, japan air force one, nswe
```

Note that the only possible aircraft that can spawn with the above definitions are `GAF1` and `JF1`. The game will be unable to spawn any more than two aircraft as only two unique callsigns can be generated.

### Advanced fix definitions (requires PyGeodesy)

If PyGeodesy is available, the below functions are also available. The tool will error if a file being built tries to use advanced fix definitions when PyGeodesy is not available.

Advanced fix definitions can be used in `[airspace]` `beacons=`, or special name prefixes can be used to define fixes "inline" using references.

#### Runway fixes

All runway ends will be available for reference under the name `=<runway_id><runway_designator>`.

#### Defining fixes by radial and distance

You can define a fix as a radial and distance from another fix in `[airspace]` `beacons=` using the following syntax:

```
@<name>, <fix>, <distance>, <radial>[, <hold_heading>, <pronunciation>]
```

*	`<fix>` is the name of another fix from which the radial and distance is calculated.
*	`<distance>` is a distance from `<fix>` in the following format: `D<distance in nmi>`, e.g. `D4`, `D21.9`
*	`<radial>` is the radial from `<fix>`, e.g. `325`, `4`, `91`. 
	-	Magnetic variation is considered as defined in `[airspace]` `magneticvar=`. You can add `T` as a suffix to indicate a true heading, e.g. `270T`
	-	If `<fix>` is a runway fix, the generated fix is also a runway fix. In such case, `<radial>` can also be specified as `RWYHDG[<+ or -><offset>]`. E.g. `RWYHDG+180`, `RWYHDG-90`.

You can also reference a fix using the below name format, and if a fix with the same name doesn't exist already, it will generate it on the fly:

```@<fix><radial><distance>```

For example:

```INI
# PANAS ONE departure from RJOO 32L
route = @PANAS1
	!O2L50
	!O2L51
# 8 DME (nmi) outbound from ITE Itami VORDME on radial 101 (magnetic)
	!@ITE101D8
	!PANAS
```

#### Defining fixes as intersection of two radials

You can define a fix as the intersection of two radials using the following syntax:

```
+<name>, <fix1>, <radial1>, <fix2>, <radial2>[, <hold_heading>, <pronunciation>]
```

*	`<fixn>` is the fix from which the respective radial is based on.
*	`<radialn>` is the heading of the respective radial.
	-	Magnetic variation is considered as defined in `[airspace]` `magneticvar=`. You can add `T` as a suffix to indicate a true heading.
	-	`<radialn>` can also be the name of a fix. In this case, the radial is the heading from `<fixn>` to the fix `<radialn>`.

You can also reference a fix using the below name format, and if a fix with the same name doesn't exist already, it will generate it on the fly:

```+<fix1><radial1><fix2><radial2>```

For example:

```INI
# KOBE FOUR departure from RJBE 09
route = @KCE4
	!@YOE274D20
#Intersection of YOE Yao VORDME radial 274 and KNE Kansai VORDME radial 323
	!+YOE274KNE323
#KNE R323 at KCE R272
	!+KNE323KCE272
	!MAIKO
```

#### Defining fixes as an intersection of two circles

You can define a fix as an intersection of two circles using the following syntax:

```
&<name>, <fix1>, <radius1>, <fix2>, <radius2>, <direction>[, <hold_heading>, <pronunciation>]
```

*	`<fixn>` is the fix from which the respective circle is based on.
*	`<radiusn>` is the radius in nmi of the respective circle in the following format: `D<distance in nmi>`
*	`<direction>` is the a cardinal direction N, S, W, or E. As two intersecting circles usually intersect at two points, the fix position will be the intersection that is <direction> relative to the other intersection.

You can also reference a fix using the below name format, and if a fix with the same name doesn't exist already, it will generate it on the fly:

```&<fix1><radius1><fix2><radius2>.<direction>```

For example:

```INI
# excerpt from definition of Yao Control Zone
[area]
shape = polygon
altitude = 2001
name = OY
draw = 50
labelpos = N34.35.00, E135.36.00
points = 
# The eastmost intersection of two circles defined as follows:
# 1: center = fix OOPR1, radius = 4.5nmi
# 2: center = fix RJOY, radius = 5nmi
	!&OOPR1D4.5&RJOYD5.E
	N34.40.05.00, E135.38.22.00
	!@OOPR1110TD4.5
	!@OOPR1115TD4.5
	...
```

### Joining approach routes

An approach route can start with `@[!]<name>` to tag the route with a name. Any approach lower in the file with the same `runway=` or no `runway=` can specify `@<name>` as the last item in their `route=` to continue on to the specified route. `!` can be included after the `@` optionally to skip the first fix in the continuing route.

For example:

```INI
[approach]
runway = RJBBRWYA, rev
beacon = AMBER
# the below route is tagged with the name ILSZ24L
route = @ILSZ24L
	58
	!MAYAH, 4000
	!BB450, 2600, 185
	!BB451
	!BB452
	!BEIGE
	5.5, 1200, 185


# defining an approach with the same route, but activated off a different beacon
[approach]
runway = RJBBRWYA, rev
beacon = MAYAH
route = 
	58
# this route is just a carbon copy of the above
	@ILSZ24L


# defining a SID to connect to the above approach
[approach]
runway = RJBBRWYA, rev
beacon = ALISA

route = @ALISAC24L
	180
	!ALISA
	!TANTA, !140
	!AWAJI, !58@AWAJI24L
	!LILAC, !58
# continue the route as per ILSZ24L.
# So after LILAC, proceed to MAYAH max 4000ft, BB450 max 2600ft 185kt, etc.
	@ILSZ24L
```

If an approach route starts with `@!<name>`, then the first point in the route is omitted when the route is referenced later. This is useful when defining approach routes that start already on the localizer.

For example:

```INI
# RJOO ILS 32L
[approach]
runway = RJOORWYB
beacon = IKOMA

# IKOMA is actually a point on the localizer 14.2 nmi from the runway.
route = @!ILS32L
	322
	!IKOMA
	14.2, 3500, 200

# HABIK ARRIVAL STAR into RJOO
[approach]
beacon = IZUMI
route = @HABIK
	41
	!IZUMI
	!HABIK, !296
# after HABIK, the route continues with 14.2, 3500, 200. 
# !IKOMA is omitted.
	@ILS32L
```

In an approach route, if the last item in a line with a fix reference is `[!<heading>][@<name>]`, it will be treated as special parameters. If the `!<heading` is defined, an approach will be generated for the same runway activating from that fix. There will only be one route, the route inbound heading will be `<heading>`, and the route consists of the rest of the declaring route starting at the current line. If the `@<name>` is defined; this will tag the rest of the route starting at the current line with the specified name.

For example:

```INI
[approach]
runway = RJBBRWYA, rev
beacon = ALISA

route = @ALISAC24L
	180
	!ALISA
# an approach for runway (RJBBRWYA, rev) activating from TANTA will be generated with the following route:
# [140, !TANTA, !AWAJI, !LILAC, @ILSZ24L]
	!TANTA, !140
# an approach activating from TANTA will be generated with the following route:
# [58, !AWAJI, !LILAC, @ILSZ24L]
# this route can be referenced by the name AWAJI24L
	!AWAJI, !58@AWAJI24L
# you can specify altitude (and speed restrictions) still, as long as the ! is last
	!LILAC, 4000, !58
	@ILSZ24L

# defining an approach that references a generated approach
[approach]
runway = RJBBRWYA, rev
beacon = BERTH

route = @BERTHC24L
	90
	!BERTH
# continue to AWAJI, LILAC, then further via ILSZ24L
	@AWAJI24L
```

An approach `route=` under an `[approach]` that doesn't specify a `runway=` can specify a comma-separated list of `@<name>` as the last item in their route. Each `<@name>` should be for a different runway. This will create an approach for each runway.

```INI
# HABIK ARRIVAL STAR into RJOO
[approach]
# note that no runway was defined
beacon = IZUMI
# yes, you can join a route to this route by having @HABIK at the end of a route. 4 approaches will be generated for that route.
route = @HABIK
	41
	!IZUMI
	!HABIK, !296
# continue on via the ILS 32L, the RNAV 32R, 
# the ILS 32L circle to land 14R, or the ILS 32L circle to land 14L.
	@ILS32L, @RNAV32RIKOMA, @ILS32LC14R, @ILS32LC14L
# In total, 4 approaches will result from this one route definition.
```

### Joining departure routes

A departure route can start with `@<name>` which makes the route a "segment". A segment will not be output in the product. This segment will be available for reference in the current `[departure]`. This is useful for defining initial departure segments unique to specific runways.

Alternatively, a departure route can start with `@!<name>` which also makes the route a "segment", but available to all subsequent `[departure]`s for the same airport including the current one. This is useful for defining transition segments common to all runways.

To use these segments, a departure route can include after the route name line an unlimited number of `@<name>` lines , which will be substituted with the respective segment.

For example:

```INI
# excerpt from Takamatsu departures
[departure]
runway = RJOTRWY

# All these routes with tags will not be in the product.
	
# TAROH THREE departure available only in this [departure]
route = @TAROH3
	!OT26D
	!TAROH

# MIHO TRANSITION available in all [departure]s for the airport this runway belongs to
route = @!MIHO
	!MIHOU

route = @OLIVE2
	!OT26D
	!OLIVE

route = @!SHTLE
	!HYOGO
	!SANDA
	!SHTLE

# the two routes below will be in the final product
# the resulting route is OT26D TAROH MIHOU
route = 
	TAROH THREE MIHO TRANSITION
	@TAROH3
	@!MIHO

# the resulting route is OT26D OLIVE HYOGO SANDA SHTLE
route =
	OLIVE TWO SHTLE TRANSITION, Olive Two Shuttle Transition
	@OLIVE2
	@!SHTLE


[departure]
runway = RJOTRWY, rev
	
# we redefine the TAROH THREE departure as it is different depending on the runway
route = @TAROH3
	!OT08D
	!TAROH

# same here
route = @OLIVE2
	!OT08D
	!OLIVE

# note that we can reference !MIHO that was defined in the above [departure]
route = 
	TAROH THREE MIHO TRANSITION
	@TAROH3
	@!MIHO

route = *4
	OLIVE TWO SHTLE TRANSITION, Olive Two Shuttle Transition
	@OLIVE2
	@!SHTLE
```

For organizational purposes, you can define shared segments in a `[commondeparture]` section:

```INI
#this section will not be in the outputted product
[commondeparture]
airport = OS

#you still need to define with @! to make them shared by airport
route = @!KILAP
	!KMANO
	!KILAP

route = @!WASYU
	!KULUL
	!KTE
	!UTAZU
	!WASYU
```

## Changelog
*	0.8.0 - 2021/02/20
	- Added generated approaches feature
	- Tagged approach routes are now runway-specific
	- Added argument to test loading from common callsigns
	- Added argument to parse source and build, not do not write product
*	0.9.0 - 2021/05/24
	- `[section]s` and `route=`s in source are no longer renumbered on disk
		- This means the build process no longer changes the source file
		- You can omit numbering for all sections and `route=`s now
	- Approach routes can now join to multiple tagged approach routes
		- Such approaches should omit `runway=`
			- The build process will infer the `runway=` from the final `route=`
	- Added argument to ignore `draw=` in `[area]`s for debug purposes
	- Added support for fix references ikn `[area]` `position=`
	- Added generated fixes feature (requires PyGeodesy)
		- Runway ends are available as fixes with name `=<runway_id><runway_designator>`
		- Defining fixes by distance on a radial
		- Defining fixes as the intersect of two radials
		- Defining fixes as the intersect of two circles
	- Added support for creating fixes on the fly from references in `route=`s
		- Only works for generated fixes, you cannot define a fix by position in a `route=`
	- It should now be easier to tell where a build failed (at the cost of long error messages)
*	0.9.1 - 2021/05/31
	- Runway coordinates are no longer assumed to be `[D]DDMMSS[.SS]`
*	0.10.0 - 2021/07/01
	- Radial intersection fix prefix character changed from `#` to `+`
		- `#` still works but is deprecated and will be disabled in the future
	- Radial intersection fixes defined in `beacons=` can use the name of a fix instead of a radial
		- The initial heading to the fix will be used as the radial
	- Approaches can be referenced with `!` to skip the first fix
		- Previously this was only possible upon definition, not upon reference
	- `_CTR` fix will be generated as a hidden fix from `[airspace] center=`.
	- Added feature to calculate headings from fixes for `[airspace] handoff=`.
*	0.10.1 - 2021/07/01
	- Bugfix: consider magnetic variation when computing `[airspace] handoff=`.
*	0.11.0 - 2021/07/18
	- Entrypoints now support multipliers
	- Approaches that end with a hold can link to other approaches
		- In preparation for 4.5.1
		- To be used to connect to multiple runways
		- The approach route is not extended with the linked approach
	- Airlines can be defined with two dashes to define unique traffic
		- Pronunciation generation added to support this
*	0.12.0 - 2021/08/30
	- Add simple error checking for entrypoints
	- Bug fix for approaches terminating in holds that connect to another approach
	- `[commondeparture]` feature for defining departures per airport
	- Allow second argument in `[airport] code=` to define full ICAO code for secondary airports
*	0.13.0 - 2021/08/31
	- Remove legacy processor, it probably was broken long time ago anyway
	- Handle the case when `[airspace] boundary=` does not exist
	- Handle the case when `[airspace] handoff=` does not exist
	- Decouple common data sources from the directory tree
		- Now common data sources can be specified in `[meta] common_data=`
		- Values can be multi-line; each line will load another common data source
		- Common data sources will be searched for similar to normal source files