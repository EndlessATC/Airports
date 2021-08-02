# `RJTT` ACA 3.3.0

This is an implementation of the Tokyo ACA (Approach Control Area) for [Endless ATC](https://steamcommunity.com/app/666610) featuring `RJTT` Tokyo International Airport (commonly referred to as Haneda) and `RJAA` Narita International Airport. JSDF-M base `RJTL` Shimofusa is also represented at very high scores (difficulties). The airspace ceiling is FL240.

Based upon AIP Japan 2021/08/12 (Ministry of Land, Infrastructure, Transport and Tourism) (https://aisjapan.mlit.go.jp/). The choice of SIDs and STARs may not be 100% accurate to real life but should be reasonably accurate reflecting daytime IMC conditions. All aircraft are assumed to be RNAV capable; no conventional NAVAID-based SIDs or STARs are implemented unless there is no RNAV alternative. Coastline data from naturalearthdata.com.

The Tokyo ACA is a very large terminal area containing two of Japan's largest airports. The traffic that can flow in and out of these two airports can be immense, but the terminal procedures published for these two airports are robust and can provide you the ability to handle the immense deluge of traffic that can pour into the area. Most of the controller's work should be sequencing arrivals and monitoring a few key merge points for conflicts. Scores of 40 or higher should be possible to maintain with minimal delay vectoring.

STARs are implemented as approach transitions. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. Multiple approaches may be available from a fix. Pressing the APP button again before issuing the approach clearance (do not long press) will select the next approach available from that fix. If the aircraft is already on an approach from that fix, you will need to cancel the approach clearance first before issuing another approach clearance.

JSDF-M base `RJTE` Tateyama and JSDF-G bases `RJTK` Kisarazu, `RJAK` Kasumigaura are not represented as it appears traffic should mostly be military helicopters, which are difficult to represent in this game. 
`RJTO` Oshima/`RJAN` Niijima are not represented as traffic is either helicopters or traffic to `RJTF` Chofu in `RJTY` Yokota ACA. Unfortunately traffic to `RJTY` is difficult to represent as `RJTT` ACA has airspace on top of most of `RJTY` ACA, meaning that within the game, it is not possible to get planes to "spawn" from the appropriate region. However, the runways for `RJTO`, `RJAN`, `RJTF`, `RJTE`, and `RJTK` are shown on the radar map.

## Airports

### `RJTT` Tokyo 'Haneda' International Airport

The main airport of this sector. Previously only handling domestic traffic and very limited international flights to key East Asian cities, Haneda now handles a fair amount of international traffic along with most of Tokyo's domestic traffic. As such, traffic is biased towards the west for departures and southwest for arrivals. 

There is custom traffic for `RJTT`. The proportions are very much estimates but shouldn't be too far off from reality.

Most fixes visible on the map have a defined hold including many fixes along the STARs. The published hold for missed approaches is `UTIBO` for 34L/23/16R, `KASGA` for 34R/22, and `SNOKE` for 16L.

Aircraft arrive at 6 points:

- `SPENS` -`Y71`-> `XAC` (west from western Japan, Korea, Northern China)
- `SELNO` -`Y21`-> `RUNSO` -`Y21`-> `AKSEL` (south west from southwestern Japan, Okinawa, Southeast Asia)
- `TOPIT` -`Y875`-> `RURER` -`Y875`-> `AROSA` (south from Hachijojima, Indonesia/Australia)
- `DOLBA` -`Y824`-> `AROSA` (southeast from oceanic, Australia/NZ/Pacific islands, Guam)
- `TEDIX` -`Y10`-> `GODIN` (north from northern Japan, Russia, Europe, east NA)
- `LALID` -`Y807`-> `POLIX` (east from oceanic, west NA/SA, Hawaii)

Aircraft depart via:

- `CLARK` (northnorthwest for Russia/Europe)
- `AGRIS` (north for northern Japan and beyond)
- `GULBO` (northeastern oceanic)
- `BORLO` (east oceanic)
- `ANSAD` (southeastern oceanic)
- `NURLI` (south)
- `KAGNA` (southwest and Osaka)
- `NINOX` (west for southern western Japan and beyond)
- `RITLA` (west for central western Japan and beyond)
- `BEKLA` (northwest such as Korea/north China/north side of western Japan)

(`VAMOS` departures to `UTIBO` aren't implemented as there are no standard flight planned routes from `RJTT` that use this transition.)

There are four runways:

- 16R/34L (RWY A) 
- 04/22 (RWY B)
- 16L/34R (RWY C)
- 05/23 (RWY D)

A few different configurations are used in real operations; four are available in this version of `RJTT` ACA:

-	Landing 34L/34R, departing 34R/05
	
	In general, arrivals from the southwest (`XAC`, `AKSEL`, `AROSA`) land 34L and arrivals from the northeast (`GODIN`, `POLIX`) land 34R. Departures to the northeast takeoff from 34R, and departures to the southwest takeoff from 05 in general.

	34L handles the higher amounts of traffic from the southwest, and 05 handles the higher amounts of traffic heading southwest. The lower amounts of traffic to/from the northeast share 34R in mixed operation. 04 is not used in this configuration as it conflicts with landings on 34L (in real life, it may be used for some GA departures?).

	Approaches to 34L (RWY *A*) and 34R (RWY *C*) are available using APP mode from *A*RLON and *C*REAM respectively, with transitions from `ARLON` or `CAMEL` depending whether the aircraft is approaching from the south or the east.

	STARs are available using APP mode from `XAC`, `RUNSO`, `AROSA`, `GODIN`, `MILIT`, and many other intermediate points on the STARs. `STARS` to 34L/34R implement a point merge system around `WEDGE` for 34L and `CREAM` for 34R. Aircraft fly an arc around a point (`WEDGE`/`CREAM`), and you can sequence planes by directing planes to proceed direct `WEDGE`/`CREAM` and activate APP mode. By default south arrivals fly STARs and approaches to 34L, but you can engage APP mode twice to have planes swing wide of the `WEDGE` arc to join the `CREAM` arc for 34R.

	Note that higher arrivals will conflict with lower arrivals when descending from the point merge arc to meet the =8000 restriction at `WEDGE`. Either descend the lower arrival (watch out for further lower arrivals) or prioritize the lower arrival over the higher arrival. Also watch for `AROSA` arrivals conflicting with arrivals to `RJAA`.

	Note that the normal runway operation for 34L/34R arrivals (`HIGHW`AY `VISUA`L 34R and ILS X 34L from `KAIHO`) is not possible to implement due to the lack of visual approaches in the game and the fact that aircraft joining the parallel ILS above `RJTK` Kisarazu would conflict as they are at the same altitude. Therefore the approaches depicted are illustrative of IMC conditions necessitating the use of parallel ILS approaches.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 34R (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 34L (T1/T3/N area).

-	Landing 22/23 (ILS), departing 16L/16R
	
	In general, arrivals from the southwest (`XAC`, `AKSEL`, `AROSA`) land **\*22\*** and arrivals from the northeast (`GODIN`, `POLIX`) land **\*23\***. Departures to the northeast takeoff from 34R, and departures to the southwest takeoff from 05 in general.

	22/16R handles the higher amounts of traffic to/from the southwest as they do not conflict with other runways (16R departures depart before the intersection with 22). As RWY23 arrivals conflict with departures from both 16s, it is used for traffic arriving from the northeast.

	Approaches to 22 and 23 are available using APP mode from `NEXUS` and `SMILE` respectively, with transitions from *N*YLON or *S*TEAM depending whether the aircraft is approaching from the *n*orth or the *s*outh.

	`STARS` are available using APP mode from `XAC`, `RUNSO`, `AROSA`, `GODIN`, `MILIT`, and many other intermediate points on the STARs. STARs from the southwest implement a point merge system around `SHAFT` (STARs from the northeast are traditional). Aircraft fly an arc around a `SHAFT`, and you can sequence planes by directing planes to proceed direct `SHAFT` and activate APP mode. By default south arrivals fly STARs and approaches to 22, but you can engage APP mode twice to have planes descend under the `SHAFT` arc to `BACON` for 23. Be careful of conflicts with traffic from the north inbound 23.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

-	Landing 22/23 (LDA), departing 16L/16R

	The same as the previous configuration, but instead aircraft approach 22/23 following an offset localizer on a 270 degree course over Tokyo Bay, avoiding overflight of populated areas.

	**Due to a game limitation, runways 22 and 23 are called 22C and 23C in this configuration.**

	Approaches to 22 (RWY *B*) and 23 (RWY *D*) are available using APP mode from *B*ONUS and *D*OYLE respectively, with transitions from *B*ACON or *D*ATUM depending whether the aircraft is approaching from the north or the south.

	`STARS` are available using APP mode from `XAC`, `RUNSO`, `AROSA`, `GODIN`, `MILIT`, and many other intermediate points on the STARs. STARs from the southwest implement a point merge system around `SHAFT` (STARs from the northeast are traditional). Aircraft fly an arc around a `SHAFT`, and you can sequence planes by directing planes to proceed direct `SHAFT` and activate APP mode.  By default south arrivals fly STARs and approaches to 22, but you can engage APP mode twice to have planes descend under the `SHAFT` arc to `BACON` for 23. Be careful of conflicts with traffic from the north inbound 23.

	Note that the LDA approaches are represented by a runway located where one would be if the LDA approaches were straight-in ILS approaches; this is the best implementation given limitations of the game, but from an approach control perspective it should be a fairly accurate representation.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

-	Landing 16L/16R, departing 16R/04/16L

	A new approach path flying over central Tokyo only applied in the afternoon hours, which was recently developed in response to growing traffic at `RJTT`. Normally arrivals fly close parallel RNAV tracks to the final approach course with a 3.45 degree glideslope, however, game limitations mean that parallel arrivals would be conflicting with each other all the way to the final approach fix. Therefore, the "backup" ILS approaches that take a dive into the Yokota ACA have been implemented here.

	Approaches to 16L and 16R are available using APP mode from `SANDY` and `NATTY` respectively.

	`STARS` are available using APP mode from `XAC`, `RUNSO`, `AROSA`, `GODIN`, `MILIT`, and many other intermediate points on the STARs. `STARS` to 16L/16R implement a point merge system around `SHAFT` for 16L and `NEURO` for 16R. Aircraft fly an arc around a point (`SHAFT`/`NEURO`), and you can sequence planes by directing planes to proceed direct `SHAFT`/`NEURO` and activate APP mode. By default south arrivals fly STARs and approaches to 16L, but you can engage APP mode twice to have planes fly over the `SHAFT` arc to join the `NEURO` arc for 16R.

	Note that the LDA approaches are represented by a runway located where one would be if the LDA approaches were straight-in ILS approaches; this is the best implementation given limitations of the game, but from an approach control perspective it should be a fairly accurate representation.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

### `RJAA` Narita International Airport

The secondary, yet also major airport of this sector. Previously handling almost all of Tokyo's international traffic, it has lost some of it to Haneda recently. However, it still handles a large chunk of Tokyo's international flights as well as the many cargo flights from FDX/UPS etc. RWY 34R which was too short when Narita opened to handle heavy aircraft has now been extended and can generally handle most aircraft other than the largest of aircraft such as A388.

There is custom traffic for `RJAA`. The proportions are very much estimates but shouldn't be too far off from reality.

Most fixes visible on the map have a defined hold including many fixes along the STARs. The published hold for missed approaches is `BINKS` for 16R/34L and `BOSPA` for 16L/34R.

Aircraft arrive at 4 points:

- `MOE` -`Y81`-> `BAFFY` -`Y81`-> `RUTAS` (southwest from western and southwestern)
- `TOPIT` -`Y87`-> `BAFFY` -`Y81`-> `RUTAS` (south)
- `VAGLA` -`Y813`-> `LUBLA` (northeast oceanic)
- `LESPO` -`Y809`-> `SUPOK` (southeast oceanic)
- `GURIR` -`Y30`-> `SWAMP` (north from north, northwest and northeast)

Aircraft depart via:

- `AGRIS` (northwest via `TETRA8` departure `AGRIS` transition to `Y37`)
- `KIMIN` (north via `TETRA8` departure `KIMIN` transition to `Y117`)
- `GULBO` (northeast oceanic via `GULBO2` departure to `Y808`)
- `BORLO` (east oceanic via `BORLO2` departure to `Y830`)
- `IRNOK` (southsoutheast oceanic via `OLVAN2` departure to `Y823`)
- `NORIS` (south oceanic via `OLVAN2` departure `SAMUS` transition to `Y84`)
- `SEDRI` (southwest via `PIGOK2` departure to `Y50`)
- `MITOP` (west via `REDEK2` departure to `Y60`)
- `TEPEX` (northwest via `TETRA8` departure `ENPAR` transition to `Y16`)

There are two runways:

- 16R/34L (RWY A) 
- 16L/34R (RWY B)

There are two simple runway configurations:

-	Landing and departing 34L/34R

	Approaches to 34L and 34R are available using APP mode from `GIINA` and `TEMIS` respectively, with transitions from `TYLER` or `ELGAR` depending whether the aircraft is approaching from the south or the east.

	`STARS` are available using APP mode from `BAFFY`, `SWAMP`, `SUPOK`, `LUBLA`, and many other intermediate points on the STARs. STARs to 34L implement a point merge system around `PEAKS`. Aircraft fly an arc around `PEAKS`, and you can sequence planes by directing planes to proceed direct `PEAKS` and activate APP mode. Alternate STARs are available to 34R which do not implement a point merge arc; watch out for potential conflicts with arrivals on STARs to 34L.

	Note that higher altitude arrivals on the arc will conflict with lower altitude arrivals descending from the point merge arc to meet the =6000 restriction at `PEAKS`. Either descend the lower altitude arrival (watch out for even lower altitude arrivals) or prioritize the lower altitude arrival over the higher altitude arrival.

	For arrivals from `RUTAS`, watch out for conflicts with `AROSA` arrivals to `RJTT`.

	Departures are executed in parallel and maintain horizontal separation until east of `RJAA`. Recommend not assigning higher than 7000 to 34L departures until clear of `RJTT` arrivals from `GODIN`/`POLIX`.

	For an extra challenge, try routing oneworld/LCC flights to 34R (T2/T3) and other flights to 34L (T1/cargo area).

-	Landing and departing 16L/16R

	Approaches to 16L and 16R are available using APP mode from `MARCH` and `ACELA` respectively, with transitions from `TYLER` or `ELGAR` depending whether the aircraft is approaching from the south or the east.

	`STARS` are available using APP mode from `BAFFY`, `SWAMP`, `SUPOK`, `LUBLA`, and many other intermediate points on the STARs. `STARS` to 16R implement a point merge system around `CASIO`. Aircraft fly an arc around `CASIO`, and you can sequence planes by directing planes to proceed direct `CASIO` and activate APP mode.  Alternate STARs are available to 16L which do not implement a point merge arc; watch out for potential conflicts with arrivals on STARs to 16R.

	Note that higher altitude arrivals on the arc will conflict with lower altitude arrivals descending from the point merge arc to meet the =6000 restriction at `CASIO`. Either descend the lower altitude arrival (watch out for even lower altitude arrivals) or prioritize the lower altitude arrival over the higher altitude arrival.

	Use care not to descend arrivals into `RJAH`/`RJAK` airspace.

	For an extra challenge, try routing oneworld/LCC flights to 16L (T2/T3) and other flights to 16R (T1/cargo area).

### `RJTL` Shimofusa Air Base
	
This JSDF-M base is located under the ILS to runway 22/23 at `RJTT`. There is one runway 01/19, with an ILS approach to RWY 19 only. Use care to maintain separation of traffic from `RJTT` arrivals. When landing RWY 01, aircraft will fly the ILS 19 and circle to land RWY 01. Due to the complexity of the airspace, in Endless ATC this airport is set to open when score > 45, to allow for beginning players to understand the `RJTT` and `RJAA` routes first.

Aircraft arrive at 4 points:

- `XAC` (southwest)
- `KAMOG` (southeast)
- `KIDOR` (north)
- `LEMUM` (northwest)

Aircraft depart via:

- `DALMA` via `OMIYA`, `EDARR`, `KOSKA` (southwest)
- `KAMOG` via `TSUGA`, `OJT` (southeast)
- `OMIYA` (northwest)
- `JD` (north)

Approaches are available using APP mode from `TOHNE` and `ASEKI`. Arrival routes are available using APP mode from `XAC`, `KAMOG`, `LEMUM`, and `KIDOR`, as well as any intermediate points.

## Known Issues

- `RJTT` LDA approaches aren't really LDA approaches with the VPT (visual prescribed track), just a hack ILS approach to a fictional runway.
- No `RJTT` RNAV 16L/16R due to game limitations (conflicts between parallel arrivals on RNAV track).
- No fair weather 34L/34R approach usage (no visual approaches, conflict on joining parallel ILS at same altitude)
- No `RJTO` Oshima/`RJAN` Niijima (not possible to model arrivals from `RJTY` ACA)
- Arrival and departure directions can be a bit nonsense (e.g. AHK arriving from the Pacific), unfortunately this is a game limitation.
- South arrivals to `RJTT` 16L/16R are very close to delayed even strictly following the STAR (game limitation?)
- No `RJAA` simultaneous parallel independent departures as the game does not support this.

## Disclaimer

This is a best effort work based on air traffic observations and official aeronautical publications. No guarantee is made that the representation of Tokyo ACA matches real life procedures in any way. Any information regarding inaccuracies is appreciated.

## For Developers

Note that traffic data (`airlines = `) is expanded by a python script `expand_airlines.py` from the shorter `source/RJTT.txt` according to the definitions in '`#!`' comments. If submitting a proposed change, please submit your changes in the source file.

## Changelog

*	1.0 - 2020/10/19 - Initial version.
*	1.1 - 2020/10/19
	- Add `RJAA`.
	- bug fixes
*	1.2 - 2020/10/23
	- Flesh out airspace (`RJTT`/`RJAA` CTR/PCA, airspace over `RJAH`/`RJTY`/`RJTU` ACA, `RJTL`/`RJTE`/`RJTK` CTR)
	- Adjustments to entry points
	- Remove hack as multiple departures on one runway work now
	- Add basic SIDs to show exit fixes
	- Display minor fixes using basic SID exit fixes
	- Correct name of `RJTT`
	- Correct reading of `OLVAN2.SAMUS` STAR
	- Correct spelling of `BEKLA2B` SID
	- Fix approaches from `GIINA`, `TEMIS`, `ACELA`, `MARCH` to actually work
	- Add case for approach from `NOVEL` when already south of `NOVEL`
*	1.3 - 2020/10/24
	- Extend `RJTT` `LAXAS` SID to `KAGNA`
	- Shorten `RJTT` `ROVER` SID `AKAGI` transition to the exit point from the ACA, `CLARK`
	- Add `RJTT` `VAMOS` SID `XAC` transition to `B586`
	- Adjusted entry points
	- Adjust label for Shimofusa CTR
	- Add readme
*	1.3.1 - 2020/10/25
	- Correct CCA callsign pronunciation for `RJAA`
*	2.0.0 - 2020/11/02
	- Add approaches to many, many fixes as the approach limit has been lifted.
	- Add `RJTT` 16L/16R ILS approaches
	- Add `RJTT` "LDA" 22/23 approaches
	- `RJAA` arrivals now fly direct to first point inside `RJTT` ACA on their arrival route instead of `NRE`.
	- Adjusted entry points
	- Added missing `ALDEN` waypoint for some STARs from `AROSA`
	- Adjusted traffic frequencies
	- Changed name of `RJAA` airport for voice purposes
*	2.0.1 - 2020/11/02
	- Fix aircraft failing to intercept the localizer for LDA approaches by changing name of runway
*	2.0.2 - 2020/11/02
	- Add `CAMEL` fix as IF for 34R and appropriate transitions. Now `CREAM` is no longer both the point merge fix and initial approach fix for 34R, and aircraft can shortcut from 2C arrivals direct to `CREAM` and fly the 34R approach via `CREAM` transition.
*	2.1.0 - 2020/11/12
	- Fix 34R approach from `ARLON`
	- Fix erroneous coordinates for `POLIX` in `POLIX1S` arrival
	- Prioritize 16L/34R at `RJAA` instead of 16R/34L for approaches. PMS STARs now lead to 16L/34R via `GEMIN` and `TYLER`, the alternative STARs now lead to 16R/34L via `NORMA` and `ELGAR`. This should be more reflective of actual runway use.
	- Add full length "`2C`", "`2B`", "`2N`" approaches for `RJTT`
	- Correct a duplicated [area]
	- Add static transitions to `RJTT` and `RJAA` IAFs
*	2.2.0 - 2020/12/02
	- Add `RJTL` JSDF-M Shimofusa Air Base
	- Add `RJTF` Chofu, `RJTO` Oshima, `RJAN` Niijima as inactive airports
	- Reposition label for `[area]` "TOKYO ACA FL240/3000 (EXC 3000)"
	- Fix erroneous coordinates for `POLIX` in `POLIX1D` arrival
	- Internal runway identifiers revised
	- Remove static transitions to 34L/22/22(LDA) and 34L/16R from `CREAM`/`DATUM`/`STEAM` and `ELGAR`/`NORMA` respectively for gameplay reasons. These transitions are still available dynamically from IFs `CAMEL`/`NEXUS`/`BONUS` and `METIS`/`TEMIS` respectively.
	- Increased the scheduled airline to GA/bizjet traffic ratio (less GA traffic).
	- Minor adjustments/updates to airline traffic.
	- Added 'rare' traffic (head of state, navaid check)
*	2.2.1 - 2020/12/19
	- Adjusted the distribution of traffic for each departure point
*	2.2.2 - 2020/12/29
	- Fixed bug where `JCG` would not spawn at `RJTT`
*	3.0.0 - 2021/02/20
	- Almost complete rewrite of source
	- Fixed WTC category of `KC2`.
	- `HKE` Hokuso VORDME decommissioned as of 2021/03/25.
		- abolish fixes `SWIMY`, `ABBOT`
		- establish fix `BOSPA`
		- revised holding at `TEMIS`
	- Add MLIT attribution to readme as per MLIT Standard Terms of Use.
	- Additional rare traffic.
	- Update magnetic variation to -8 (2020)
	- Correct expected inbound headings to some STARs (should have no effect on gameplay)
	- Added approaches from the end of the point merge arcs to facilitate vectoring when arc capacity exceeded
	- Added approaches from the FAF to allow clearing for the approach via the IF
	- Improve point merge arc visualization
	- Change format of SID names
		- Correct names and pronunciations of some departures
	- Corrected runway priority for `RJTT` 16L/R (16L is now prioritized)
	- Departures from 16R now start past the intersection with 22 as per real life
	- Reduced frequency of traffic at `RJTL` to 1/3 of previous.
	- Implement ILS Y 16L/16R approaches at `RJAA`
	- Implement ILS X 34L/ILS Y 34R approaches at `RJTT`
*	3.1.0 - 2021/05/31
	- Corrected definition of `TEMIS`, shouldn't affect gameplay
	- Revised ILS Z 34L at `RJTT`
		- removed -5000 altitude restriction at `ARLON`
		- ILS intercept changed to 15.5nmi from runway (D15.7 `IHA`/0.6nmi from `APOLO`)
			- previously, the ILS intercept was at `ARLON`
		- In reality, there was no restriction at `ARLON` in the first place (rather, there was a +5000 restriction at `CREAM`
	- Corrected coordinates of `RJTL` runway, shouldn't affect gameplay
	- Implemented tower frequencies
*	3.2.0 - 2021/07/06
	- Add handoff callsign / frequency support for departures
	- Additions/corrections to rare traffic.
*	3.3.0 - 2021/07/18
	- Implement different entry altitudes for each entrypoint
	- Implement different initial climb altitudes for each departure
	- Arrival entrypoints changed for most arrival routes to waypoints along the ACA boundary
	- Arrivals are automatically cleared for a relevant STAR
		- This is a temporary measure until  4.5.1 releases
		- this will be changed so that　aircraft will only be cleared to the first fix of the STAR and hold there
		- Clearing aircraft via the STAR will then be the responsibility of approach control (you)
	- Correct pronunciation for `TETRA` departures from `RJAA`
	- Add 200kts restriction at `ARLON` for ILS Z 34L at `RJTT` to prevent certain aircraft such as `B772` from overshooting the GS
	- Add inactive `RJTK` Kisarazu and `RJTE` Tateyama
		- Add `KZT` Kisarazu and `TET` Tateyama TACANs
	- ANA `B737`s retired
	- Made some rare traffic unique (no more than one will appear at any one time)
*	3.4.0 - pending release of 4.5.1
	- Upon entering the ACA, planes will fly along any airways to the beginning of the STAR and hold
		- Approach (you) will be responsible for clearing for the STAR