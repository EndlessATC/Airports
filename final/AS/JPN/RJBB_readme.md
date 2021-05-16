# RJBB ACA 2.0.0

This is an implementation of the Kansai ACA (Approach Control Area) for [Endless ATC](https://steamcommunity.com/app/666610) featuring RJBB Kansai International Airport, RJOO Osaka International Airport (often referred to as Itami), RJBE Kobe Airport, RJOS Tokushima Airport, RJOT Takamatsu Airport, and RJOB Okayama Airport. The airspace ceiling is FL180.

The Kansai ACA is a very complex airspace, with many airports in close vicinity in Osaka Bay and the surroundings. There are many flight paths that cross over each other, and altitude will need to used to separate aircraft very often, especially within Osaka Bay. The controller will need to carefully monitor both departures and arrivals and issue altitude, speed, and vectors to ensure proper separation.

Based upon AIP Japan 2020/12/31. The choice of SIDs and STARs may not be 100% accurate to real life but should be reasonably accurate reflecting daytime IMC conditions. All aircraft are assumed to be RNAV capable; no conventional NAVAID-based SIDs or STARs were implemented unless there is no RNAV procedure published. Coastline data from naturalearthdata.com.

STARs are implemented as approach transitions. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. Multiple approaches may be available from a fix (even approaches to airports other than the aircraft's intended destination). **\*Use care to ensure you have selected the approach to the correct airport!!!\*** Pressing the APP button again (do not long press) to select the next approach available from that fix. If the aircraft is already on an approach from that fix, you will need to cancel the approach clearance first before issuing another approach clearance.

The published STARs for the aerodromes in the Kansai ACA typically do not have "at or below" crossing restrictions. Given this type of restriction is the only one that can be implemented in Endless ATC, this would have resulted in appraoches providing only lateral guidance. Therefore, restrictions have been implemented to provide a "latest possible descent" to the initial approach fix. You can descend aircraft below the implemented restrictions for separation purposes in most cases; any "at or above" crossing restrictions are noted below per airport.

**\*Departures may need to handed off before they reach the boundary of the ACA\***, *as there are cases where the SID exts the ACA before cruise altitude can be reached.*

`RJOY` Yao Airport is currently not implemented in this version.

The Tokushima ACA which exists almost entirely under the Kansai ACA, is treated as part of Kansai ACA for gameplay purposes. Note that only aircraft arriving or departing RJOS Tokushima are allowed into the Tokushima ACA airspace (areas labeled with `OS`).

The Kansai ACA is extended over the Chubu ACA to the east around `SINGU` and `KODAI` as well as to the north around `ROKKO` and `WAKIT` for gameplay reasons. However, the southwestern part of Kansai ACA around `RJOK` Kochi is omitted for gameplay reasons. Flight routes between `RJOO`/`RJBB` and `RJOK` are also not represented.

## Airports

### `RJBB` Kansai International Airport

The main airport of this airspace, Kansai handles both domestic and international traffic to the Kansai region (Osaka, Kobe, Kyoto, Nara, etc). Arrivals/departures will fly over RJBE Kobe to the north, and care should taken here to maintain separation of aircraft.

There is custom traffic for `RJBB`. The proportions are very much estimates but shouldn't be too far off from reality.

Many fixes visible on the map have a defined hold including some key fixes along the STARs.

Aircraft arrive at:

- (`SAEKI`) -> `ALISA` (northwest from Korea/northern China and northeast from NE Japan, Europe)
- (`RANDY`) -> `BERTH` (west from Fukuoka, western Japan, China)
- (`KARIN`) -> `BECKY` (southwest from southwestern Japan, Taiwan, HK, Singapore, Malaysia, etc.)
- (`EVERT`) -> `CANDY` (southwest from Philippines, south from Indonesia/Oceania, east from Nagoya/PACOTS)
- (`KOHWA`) -> `SINGU` -> `DANDE` (east from RJTT Tokyo, RJAA Narita, RJSS Sendai, RJSF Fukushima)

Aircraft depart via:

- `KEC` (east for `RJAA` Narita, PACOTS)
- `SHTLE` (east for `RJTT` Tokyo)
- `UENOH` (northeast to Tohoku, southeast Hokkaido)
- `SIGAK` (northeast to northwest Hokkaido, east NA, Europe)
- `YME` (northeast to northeastern China)
- `SOUJA` (northwest to Korea, northern China, Europe)
- `WASYU` (west to western Japan/Jeju)
- `HABAR` (west to China)
- `POPPY` (southwest to Taiwan, HK, Singapore, Malaysia, etc.)

There are two runways:

- 06R/24L (RWY A)
- 06L/24R (RWY B)

Note that simultaneous parallel independent approaches do not appear to be in use at RJBB. It is possible in the game, but the approaches are not built with this in mind. Of course, you can still do simultaneous parallel dependent approaches with staggered sequencing, which can help with dealing with wake turbulence separation.

The preferred runway is generally RWY A as the main terminal 1 is much closer to RWY A. LCC carriers operating from terminal 2 would have a shorter taxi from RWY B.

STARs are available from `ALISA`, `BERTH`, `BECKY`, `CANDY`, `DANDE`, and approach modes can be activated from those fixes as well as intermediate fixes on the STARs, as well as fixes on airways joining to the STARs.

There are two landing configurations:

-	Landing/departing RWY 06L/06R

This is the preferred configuration for RJBB. 

Vectors can be used for sequencing, or direct to fix shortcuts can also be issued (or both). Approaches are available from `ALLAN` and `BERRY`, and approaches from GATES are available from `JANET` and `JENNY`.

Use care not to descend arrivals into Tokushima ACA. Cross TANTA (from ALISA), NALTO (from BERTH), EVIAN, DATIS, JOLLY +6000 (at or above 6000).

Departures will be climbing over `RJBE` departures from 09, use care to maintain separation. Departures may also join paths after diverging initially especially after `MAIKO`, and may conflict with departures from `RJOO` and `RJBE` northwest of MAIKO. 

The published hold for missed approaches is `LILAC` +3000 for 06L, `AKASI` +4000 (via MAIKO) for 06R.

-	Landing/departing RWY 24L/24R

This is the south wind configuration for RJBB. 

Vectors onto the localizer should NOT be used. Approaches are available from `MAYAH` (24L), or `AMBER` (24L) and `BEIGE` (24R). Arrivals can be vectored over the sea west of Awaji Island if needed on top of `RJBE` arrivals.

Use care not to descend arrivals into the `RJBE` PCA. Cross JOLLY (from DANDE) +8000, AWAJI +7000, MAYAH 4000 (**at** 4000). Aircraft should descend as per the approach after MAYAH in order to main separation from `RJBE` traffic. Note that due to the lack of circle to land approaches in Endless ATC, `RJBE` 27 arrivals will fly a long downwind at ~1300 and may conflict with `RJBB` 24 arrivals leaving 2600. Having the `RJBE` arrival fly slightly ahead of an overhead `RJBB` arrival should allow for separation to be maintained.

Departures to the west will be climbing through arrivals descending to 4000 from `AWAJI` to `LILAC` to `MAYAH` and over `RJBE departures`. Departures over `DAISY` should cross `DAISY` +6000 and JULIA +8000. Departures over HELEN should cross `HELEN` +8000. Due care will need to be taken to maintain separation. Recommend descending to arrivals to 4000 after `AWAJI`, and expediting climb of departures from 24R. Departures to the west may also conflict with `RJBE` departures and `RJOO` departures to the west.

Departures to the south may conflict with arrivals from DANDE and the south/southwest. Use caution.

### `RJOO` Osaka International Airport

An airport near the heart of Osaka, only domestic traffic is handled aside from the odd state aircraft. Mountains surround the airport to the north, west, and east.

There is custom traffic for `RJOO`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `ROKKO` (northwest from northwestern Japan, northeast from northeastern Japan)
- `KODAI` (east from eastern Japan)
- `KAZRA` -> `MIRIO` -> `KAINA` -> `IZUMI` (west from western Japan)
- `JANGO` -> `MIRIO` -> `KAINA` -> `IZUMI` (west from western Japan)
- `MUGIE` -> `HONMA` -> `KAINA` -> `IZUMI` (southwest from southwestern Japan)

Aircraft depart via:

- `SHTLE` (east for Tokyo)
- `MINAC` (northeast to Tohoku, Hokkaido)
- `TOZAN` (northwest to Taiwan, HK, Singapore, Malaysia, etc.)
- `SOUJA` (west to north Kyushu)
- `WASYU` (west to western Japan, central Kyushu)
- `KRE` (southwest to southwestern Japan, south Kyushu)

There are two runways:

- 14R/32L
- 14L/32R

Larger aircraft land 14R/32L, as 14L/32R is generally only suitable for aircraft A320/B738 or smaller. It is not possible to model this in the game however.

Note that simultaneous parallel independent approaches are not used at `RJOO`. It is possible in the game, but the approaches are not built with this in mind. Of course, you can still do simultaneous parallel dependent approaches with staggered sequencing, which can help with dealing with wake turbulence separation, however, this would not be used in reality as the runways are too close to each other.

Airspace to vector arrivals for sequencing is avaiable south of IKOMA/southeast of IZUMI/west of KODAI. Arrivals will fly over `RJOY` Yao, use care not to descend into YAO airspace. Use care to keep separation at `KAINA`, `ROKKO` and near `IKOMA`.

West departures may conflict with other aircraft on west departures. Use caution.

The missed approach hold is IZUMI +3000.

There are two simple runway configurations:

-	Landing and departing 32L/32R

The preferred runway configuration.

Due to the mountains surrounding the airport, departures make a climbing left turn towards the south.

-	Landing and departing 14L/14R

This runway configuration is only used when winds do not allow for use of the 32s. Arrivals circle west of the airport to land the 14s within the mountainous surroundings.

Due to the lack of circle to land approaches in Endless ATC, aircraft make long downwind to 14. Note that in real life these aircraft would have long flown into terrain, but this is the best we can do here.

Departures may conflict with arrivals circling to 14. Use caution.

West departures may conflict with other aircraft on west departures or arrivals to `RJBE`/`RJOT`/`RJOB`. Use caution.

### `RJBE` Kobe Airport

A smaller airport in Osaka Bay minutes from central Kobe. Located under to approach to the 24s at `RJBB`, typically in-out operations landing 09 and departing 27 are ideal. Unfortunately, this is not possible in Endless ATC.

There is custom traffic for `RJBE`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `GINJI` (east from eastern Japan)
- `WAKIT` (northeast from northeastern Japan)
- `RANDY` -> `BERTH` (west from western Japan)
- `KARIN` -> `BECKY` (southwest from southwestern Japan)

Aircraft depart via:

- `SHTLE` (east for Tokyo)
- `CUE` (east to eastern Japan)
- `YME` (northeast to Tohoku/Hokkaido)
- `SOUJA` (west to north Kyushu)
- `WASYU` (west to western Japan, central Kyushu)
- `POPPY` (southwest to southwestern Japan, south Kyushu)

Aircraft arriving/departing `RJBE` in general will be operating under `RJBB` traffic. Ensure that arrivals are low enough before entering the bay, and that departures are clear of traffic above before issuing further climb.

Arrivals can be vectored over the sea west of Awaji Island.

Departures may conflict with other aircraft on west departures or arrivals to `RJOT`/`RJOB`. Use caution.

The missed approach hold is SIOJI +3000.

There are two simple runway configurations:

-	Landing and departing 09

The preferred runway configuration. Departures make a climbing right turn to depart to the west remaining under `RJBB` departures and over `RJBE` arrivals.

-	Landing and departing 27

This runway configuration is used when `RJBB` is landing 24, as Endless ATC requires departures to climb to a minimum of 3000 which would conflict with the `RJBB` 24 approach path. Arrivals circle to land 27, however as Endless ATC does not have circle to land approaches, arrivals make a long downwind to 27, and may conflict with RJBB arrivals leaving 2600. Having the `RJBE` arrival fly slightly ahead of an overhead `RJBB` arrival should allow for separation to be maintained.

Departures will need to climb to 4000 or higher to clear arrivals at 3000.

### `RJOS` Tokushima Airport

A joint-use civilian airport and JSDF-M base. Training operations with Beech King Airs are conducted by the JSDF-M from this base. Typically in-out operations landing 29 and departing 11 are ideal; unfortunately, this is not possible in Endless ATC.

There is custom traffic for `RJOS`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `JOSIN` (southeast to training areas?)
- `SINGU` -> ... -> `DATIS` (east from Tokyo)
- `KTE` -> `KULUL` -> `TSC` (west from Fukuoka)

Aircraft depart via:

- `KMANO` (east for Tokyo)
- `KTE` -> `WASYU` (west to Fukuoka)
- `TOSAR` (south to training areas?)

Departures may conflict with other aircraft on southwest departures and `RJBB` `CANDY` arrivals. Use caution.

The missed approach hold is TSC/DATIS +3000.

There are two simple runway configurations:

-	Landing and departing 29

The preferred runway configuration. Departures make a climbing left turn to depart to the southeast.

-	Landing and departing 11

This runway configuration is used when winds do not allow straight-in 29. Arrivals circle to land 11, however as Endless ATC does not have circle to land approaches, arrivals make a long downwind to 11.

### `RJOT` Takamatsu Airport

An airport nestled up against mountains to the south serving Takamatsu.

There is custom traffic for `RJOT`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `GINJI` (east)
- (`TAKMA`) -> `KTE` (west/southwest)
- (`YUBAR`) -> `OYE` -> `KTE` (northwest)

Aircraft depart via:

- `SHTLE` (east)
- `WASYU` (west)
- `TAROH` (north)

The missed approach hold is KTE +5000.

There are two simple runway configurations:

-	Landing and departing 26

The preferred runway configuration.

-	Landing and departing 11

This runway configuration is used when winds do not allow straight-in 26. Arrivals circle to land 11, however as Endless ATC does not have circle to land approaches, arrivals make a long downwind to 11.

### `RJOB` Okayama Airport

An airport situated in the mountains serving Okayama.

There is custom traffic for `RJOB`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `GINJI` (east)
- `WAKIT` (northeast)
- (`YUBAR`) -> `OYE`(north)
- (`TAKMA`) -> `INOOK` (west/southwest)

Aircraft depart via:

- `SHTLE` (east)
- `YME` (northeast)
- `YUBAR` (north)
- `WASYU` (west)

The missed approach hold is OYE/BENES +4000.

There are two simple runway configurations:

-	Landing and departing 07

The preferred runway configuration for arrivals from the west. A RNAV AR approach utilizing RF legs to circle to 07 from the east is available in reality but the final leg is too short to be reproducible in Endless ATC. Therefore, east arrivals fly the ILS from OYE.

-	Landing and departing 25

The preferred runway configuration for arrivals from the east. The straight-in to 25 is an RNAV approach as there is no ILS for 25.

## Known Issues

- Circle to land approaches...............*sigh*
- No `RJOY` Yao (how to even go about doing this...)

## Changelog

*	1.0.0 - 2020/10/12 - Initial version.
*	2.0.0 - 2020/11/02
	- Add approaches to both runway ends for all airports.
	- Add approaches to many, many fixes as the approach limit has been lifted.
	- Adjusted eastern ACA extension over Chubu ACA
	- Added previously cut western ACA
	- Added part of previously cut southwestern ACA
	- Added `RJOB` Okayama
	- Arrivals for `RJOO`, `RJBE`, `RJOS`, `RJOT` now fly direct to the a suitable fix inside RJBB ACA on their arrival route instead of a single point for all arrivals.
	- Adjusted entry points
	- Removed `Y53 BECKY` entry point for `RJOO`
	- Removed `YOSAK` departures from `RJBB` (not used in daytime)
	- Removed `CUE`/`POPPY` departures from `RJOO` (not used in standard flight planned routes)
	- Removed `MISAKI1` departure from `RJOS` (use HONMA1.KILAP instead for RNAV-capable)
	- Added `UENOH` departures from `RJBB` (as per standard flight planned route)
	- Adjusted traffic frequencies
	- Changed names of airports for voice purposes
	- Added various minor fixes
	- Added Akeno ACA area
	- Removed training areas as they should be more inactive rather than active...?
*	3.0.0 - 2021/03/xx
	- Rewrite of source
	- Add `RJBB` ARC series STARs and ILS Y approaches
	- `CUE` Otsu VORDME decommissioned
		- `MIDER` established
		- `RJOO` OTSU FIVE DEPARTURE and KOMATSU TRANSITION abolished 
		- `RJOO` PANAS ONE DEPARTURE and KOMAZ TRANSITION established
		- `RJBE` OTSU TRANSITION abolished
		- `RJBE` MIDER TRANSITION established