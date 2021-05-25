# Endless ATC Custom Airport Tools 0.9.0

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
*	`[transition]`
*	`route=`

### Fix definitions and references

Fixes defined in `[airspace]` `beacons=` are stored in a database for reference elsewhere in the file.
If you specify `!` as the heading, the fix will be "hidden" and not be drawn on the map unless called for elsewhere in the file. A hold heading can be specified after the `!` if necessary.

Any fixes can be referenced by name later in the following areas using `!<fix_name>` instead of `<position>` unless indicated otherwise:

*	`[airspace]` `boundary=`
*	`[airport]`
	-	`sids=`
		- This is intended to be used for drawing "hidden" fixes on the map that aren't meant to be used by arrival aircraft, as you cannot issue DCT to these fixes
		- However, if you are not using `[departure]`s, then these will function as usual
*	`[area]`
	-	`position=`
	-	`points=`
*	`[approach]`
	-	`route=`
		- Restrictions can be specified as normal
	-	`beacon=`
		- `!` is optional
		- If the referenced fix is "hidden", the fix definition will be substituted in, so that the fix is drawn on the map while the approach is available
*	`[departure]`
	-	`route=`

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
#<name>, <fix1>, <radial1>, <fix2>, <radial2>[, <hold_heading>, <pronunciation>]
```

*	`<fixn>` is the fix from which the respective radial is based on.
*	`<radialn>` is the heading of the respective radial.
	-	Magnetic variation is considered as defined in `[airspace]` `magneticvar=`. You can add `T` as a suffix to indicate a true heading.

You can also reference a fix using the below name format, and if a fix with the same name doesn't exist already, it will generate it on the fly:

```#<fix1><radial1><fix2><radial2>```

For example:

```INI
# KOBE FOUR departure from RJBE 09
route = @KCE4
	!@YOE274D20
#Intersection of YOE Yao VORDME radial 274 and KNE Kansai VORDME radial 323
	!#YOE274KNE323
#KNE R323 at KCE R272
	!#KNE323KCE272
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

An approach route can start with `@<name>` to tag the route with a name. Any approach lower in the file with the same `runway=` or no `runway=` can specify `@<name>` as the last item in their `route=` to continue on to specified route.

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

```
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

In an approach route, if the last item in a line with a fix reference is `!<heading>[@<name>]`, an approach will be generated for the same runway activating from that fix. There will only be one route, the route inbound heading will be `<heading>`, and the route consists of the rest of the declaring route. `@<name>` is optional; this will tag the route of the generated approach for reference by other approaches.

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

```
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

Alternatively, a departure route can start with `@!<name>` which also makes the route a "segment", but available to all subsequent `[departure]`s including the current one. This is useful for defining transition segments common to all runways.

To use these segments, a departure route can include after the route name line an unlimited number of `@<name>` lines , which will be substituted with the respective segment.

For example:

```
# excerpt from Takamatsu departures
[departure]
runway = RJOTRWY

# All these routes with tags will not be in the product.
	
# TAROH THREE departure available only in this [departure]
route = @TAROH3
	!OT26D
	!TAROH

# MIHO TRANSITION available in all [departure]s
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
