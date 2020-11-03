# RJTT ACA 2.0.2

This is an implementation of the TOKYO ACA (Approach Control Area) for [Endless ATC](https://steamcommunity.com/app/666610) featuring RJTT Tokyo International Airport (commonly referred to as Haneda) and RJAA Narita International Airport.

Based upon AIP Japan 2020/10/08. The choice of SIDs and STARs may not be 100% accurate to real life but should be reasonably accurate reflecting daytime IMC conditions. All aircraft are assumed to be RNAV capable; no conventional NAVAID-based SIDs or STARs are implemented.

To activate a STAR, a plane must be flying direct to an applicable fix, then the APP button can be activated.

JSDF-G bases RJTL Shimofusa, RJTE Tateyama, RJTK Kisarazu are not represented as it appears traffic should mostly be military helicopters, which I don't know how to represent in this game.
RJTO Oshima/RJAN Niijima are not represented as traffic is either helicopters or traffic to RJTF Chofu in RJTY Yokota ACA. Unfortunately traffic to RJTY is difficult to represent as RJTT ACA has airspace on top of most of RJTY ACA, meaning that within the game, it is not possible to get planes to "spawn" from the appropriate region.

## Airports

### RJTT

The main airport of this sector. Previously only handling domestic traffic and very limited international flights to key East Asian cities, Haneda now handles a fair amount of international traffic along with most of Tokyo's domestic traffic. As such, traffic is biased towards the west for departures and southwest for arrivals. 

There is custom traffic for RJTT. The proportions are very much estimates but shouldn't be too far off from reality.

Most fixes visible on the map have a defined hold including many fixes along the STARs. The published hold for missed approaches is UTIBO for 34L/23/16R, KASGA for 34R/22, and SNOKE for 16L.

Aircraft arrive at 6 points:

- SPENS -> XAC (west from western Japan, Korea, Northern China)
- SELNO -> RUNSO -> AKSEL (south west from southwestern Japan, Okinawa, Southeast Asia)
- TOPIT -> LUTNA -> RURER -> AROSA (south from Hachijojima, Indonesia/Australia)
- DOLBA -> AROSA (southeast from oceanic, Australia/NZ/Pacific islands, Guam)
- TEDIX -> GODIN (north from northern Japan, Russia, Europe, east NA)
- LALID -> MILIT -> RUSDA -> ESKEN -> POLIX (east from oceanic, west NA/SA, Hawaii)

Aircraft depart via:

- CLARK (northnorthwest for Russia/Europe)
- AGRIS (north for northern Japan and beyond)
- GULBO (northeastern oceanic)
- BORLO (east oceanic)
- ANSAD (southeastern oceanic)
- NURLI (south)
- KAGNA (southwest and Osaka)
- NINOX (west for southern western Japan and beyond)
- RITLA (west for central western Japan and beyond)
- BEKLA (northwest such as Korea/north China/north side of western Japan)

(VAMOS departures to UTIBO aren't implemented as there are no standard flight planned routes from RJTT that use this transition.)

There are four runways:

- 16R/34L (RWY A) 
- 04/22 (RWY B)
- 16L/34R (RWY C)
- 05/23 (RWY D)

A few different configurations are used in real operations; four are available in this version of RJTT ACA:

-	Landing 34L/34R, departing 34R/05
	
	In general, arrivals from the southwest (XAC, AKSEL, AROSA) land 34L and arrivals from the northeast (GODIN, POLIX) land 34R. Departures to the northeast takeoff from 34R, and departures to the southwest takeoff from 05 in general.

	34L handles the higher amounts of traffic from the southwest, and 05 handles the higher amounts of traffic heading southwest. The lower amounts of traffic to/from the northeast share 34R in mixed operation. 04 is not used in this configuration as it conflicts with landings on 34L (in real life, it may be used for some GA departures?).

	Approaches to 34L (RWY *A*) and 34R (RWY *C*) are available using APP mode from *A*RLON and *C*REAM respectively, with transitions from ARLON or CAMEL depending whether the aircraft is approaching from the south or the east.

	STARS are available using APP mode from XAC, RUNSO, AROSA, GODIN, MILIT, and many other intermediate points on the STARs. STARS to 34L/34R implement a point merge system around WEDGE for 34L and CREAM for 34R. Aircraft fly an arc around a point (WEDGE/CREAM), and you can sequence planes by directing planes to proceed direct WEDGE/CREAM and activate APP mode. By default south arrivals fly STARs and approaches to 34L, but you can engage APP mode from CLONE to have planes swing wide of the WEDGE arc to join the CREAM arc for 34R.

	Note that higher arrivals will conflict with lower arrivals when descending from the point merge arc to meet the =8000 restriction at WEDGE. Either descend the lower arrival (watch out for further lower arrivals) or prioritize the lower arrival over the higher arrival. Also watch for AROSA arrivals conflicting with arrivals to RJAA.

	\***Departures to the west/north/south will need to handed off before they reach the boundary of the ACA**, *as they will likely NOT climb out of the ACA.*\*

	Note that the normal runway operation for 34L/34R arrivals (HIGHWAY VISUAL 34R and ILS X 34L from KAIHO) is not possible to implement due to the lack of visual approaches in the game and the fact that aircraft joining the parallel ILS above RJTK Kisarazu would conflict as they are at the same altitude. Therefore the approaches depicted are illustrative of IMC conditions necessitating the use of parallel ILS approaches.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 34R (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 34L (T1/T3/N area).

-	Landing 22/23 (ILS), departing 16L/16R
	
	In general, arrivals from the southwest (XAC, AKSEL, AROSA) land **\*22\*** and arrivals from the northeast (GODIN, POLIX) land **\*23\***. Departures to the northeast takeoff from 34R, and departures to the southwest takeoff from 05 in general.

	22/16R handles the higher amounts of traffic to/from the southwest as they do not conflict with other runways (16R departures depart before the intersection with 22). As RWY23 arrivals conflict with departures from both 16s, it is used for traffic arriving from the northeast.

	Approaches to 22 and 23 are available using APP mode from NEXUS and SMILE respectively, with transitions from *N*YLON or *S*TEAM depending whether the aircraft is approaching from the *n*orth or the *s*outh.

	STARS are available using APP mode from XAC, RUNSO, AROSA, GODIN, MILIT, and many other intermediate points on the STARs. STARs from the southwest implement a point merge system around SHAFT (STARs from the northeast are traditional). Aircraft fly an arc around a SHAFT, and you can sequence planes by directing planes to proceed direct SHAFT and activate APP mode. By default south arrivals fly STARs and approaches to 22, but you can engage APP mode from LAFIT to have planes descend under the SHAFT arc to BACON for 23.

	\***Departures to the west/north/south will need to handed off before they reach the boundary of the ACA**, *as they will likely NOT climb out of the ACA.*\*

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

-	Landing 22/23 (LDA), departing 16L/16R

	The same as the previous configuration, but instead aircraft approach 22/23 following an offset localizer on a 270 degree course over Tokyo Bay, avoiding overflight of populated areas.

	**Due to a game limitation, runways 22 and 23 are called 22C and 23C in this configuration.**

	Approaches to 22 (RWY *B*) and 23 (RWY *D*) are available using APP mode from *B*ONUS and *D*OYLE respectively, with transitions from *B*ACON or *D*ATUM depending whether the aircraft is approaching from the north or the south.

	STARS are available using APP mode from XAC, RUNSO, AROSA, GODIN, MILIT, and many other intermediate points on the STARs. STARs from the southwest implement a point merge system around SHAFT (STARs from the northeast are traditional). Aircraft fly an arc around a SHAFT, and you can sequence planes by directing planes to proceed direct SHAFT and activate APP mode.  By default south arrivals fly STARs and approaches to 22, but you can engage APP mode from LAFIT to have planes descend under the SHAFT arc to BACON for 23.

	\***Departures to the west/north/south will need to handed off before they reach the boundary of the ACA**, *as they will likely NOT climb out of the ACA.*\*

	Note that the LDA approaches are represented by a runway located where one would be if the LDA approaches were straight-in ILS approaches; this is the best implementation given limitations of the game, but from an approach control perspective it should be a fairly accurate representation.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

-	Landing 16L/16R, departing 16R/04/16L

	A new approach path flying over central Tokyo only applied in the afternoon hours, which was recently developed in response to growing traffic at RJTT. Normally arrivals fly close parallel RNAV tracks to the final approach course with a 3.45 degree glideslope, however, game limitations mean that parallel arrivals would be conflicting with each other all the way to the final approach fix. Therefore, the "backup" ILS approaches that take a dive into the Yokota ACA have been implemented here.

	Approaches to 16L and 16R are available using APP mode from SANDY and NATTY respectively.

	STARS are available using APP mode from XAC, RUNSO, AROSA, GODIN, MILIT, and many other intermediate points on the STARs. STARS to 16L/16R implement a point merge system around SHAFT for 16L and NEURO for 16R. Aircraft fly an arc around a point (SHAFT/NEURO), and you can sequence planes by directing planes to proceed direct SHAFT/NEURO and activate APP mode. By default south arrivals fly STARs and approaches to 16L, but you can engage APP mode from SCOUT to have planes fly over the SHAFT arc to join the NEURO arc for 16R.

	\***Departures to the west/north/south will need to handed off before they reach the boundary of the ACA**, *as they will likely NOT climb out of the ACA.*\*

	Note that the LDA approaches are represented by a runway located where one would be if the LDA approaches were straight-in ILS approaches; this is the best implementation given limitations of the game, but from an approach control perspective it should be a fairly accurate representation.

	For an extra challenge, try routing ANA/SNJ/ADO/VIP flights to 23 (T2/VIP area) and JAL/SFJ/SKY/international/GA flights to 22 (T1/T3/N area).

### RJAA

The secondary, yet also major airport of this sector. Previously handling almost all of Tokyo's international traffic, it has lost some of it to Haneda recently. However, it still handles a large chunk of Tokyo's international flights as well as the many cargo flights from FDX/UPS etc. RWY 34R which was too short when Narita opened to handle heavy aircraft has now been extended and can generally handle most aircraft other than the largest of aircraft such as A388.

There is custom traffic for RJAA. The proportions are very much estimates but shouldn't be too far off from reality.

Most fixes visible on the map have a defined hold including many fixes along the STARs. The published hold for missed approaches is SWIMY for 16R/34L and ABBOT for 16L/34R.

Aircraft arrive at 4 points:

- BAFFY -> MAMAS -> RUTAS (southwest from western and southwestern)
- VAGLA -> LUBLA (northeast oceanic)
- LESPO -> SUPOK (southeast oceanic)
- GURIR -> SWAMP (north from north, northwest and northeast)

Aircraft depart via:

- AGRIS (northwest)
- KIMIN (north)
- GULBO (northeast oceanic)
- BORLO (east oceanic)
- IRNOK (southsoutheast oceanic)
- NORIS (south oceanic)
- SEDRI (southwest)
- MITOP (west)
- TEPEX (northwest)

There are two runways:

- 16R/34L (RWY A) 
- 16L/34R (RWY B)

There are two simple runway configurations:

-	Landing and departing 34L/34R

	Approaches to 34L and 34R are available using APP mode from GIINA and TEMIS respectively, with transitions from TYLER or ELGAR depending whether the aircraft is approaching from the south or the east.

	STARS are available using APP mode from BAFFY, SWAMP, SUPOK, LUBLA, and many other intermediate points on the STARs. STARS to 34L implement a point merge system around PEAKS. Aircraft fly an arc around PEAKS, and you can sequence planes by directing planes to proceed direct PEAKS and activate APP mode. Alternate STARs are available to 34R which do not implement a point merge arc; watch out for potential conflicts with arrivals on STARs to 34L.

	Note that higher altitude arrivals on the arc will conflict with lower altitude arrivals descending from the point merge arc to meet the =6000 restriction at PEAKS. Either descend the lower altitude arrival (watch out for even lower altitude arrivals) or prioritize the lower altitude arrival over the higher altitude arrival.

	For arrivals from RUTAS, watch out for conflicts with AROSA arrivals to RJTT.

	Departures are executed in parallel and maintain horizontal separation until east of RJAA. Recommend not assigning higher than 7000 to 34L departures until clear of RJTT arrivals from GODIN/POLIX.

	For an extra challenge, try routing oneworld/LCC flights to 34R (T2/T3) and other flights to 34L (T1/cargo area).

-	Landing 22/23, departing 16L/16R

	Approaches to 16L and 16R are available using APP mode from MARCH and ACELA respectively, with transitions from TYLER or ELGAR depending whether the aircraft is approaching from the south or the east.

	STARS are available using APP mode from BAFFY, SWAMP, SUPOK, LUBLA, and many other intermediate points on the STARs. STARS to 16R implement a point merge system around CASIO. Aircraft fly an arc around CASIO, and you can sequence planes by directing planes to proceed direct CASIO and activate APP mode.  Alternate STARs are available to 16L which do not implement a point merge arc; watch out for potential conflicts with arrivals on STARs to 16R.

	Note that higher altitude arrivals on the arc will conflict with lower altitude arrivals descending from the point merge arc to meet the =6000 restriction at CASIO. Either descend the lower altitude arrival (watch out for even lower altitude arrivals) or prioritize the lower altitude arrival over the higher altitude arrival.

	Use care not to descend arrivals into RJAH/RJAK airspace.

	For an extra challenge, try routing oneworld/LCC flights to 16L (T2/T3) and other flights to 16R (T1/cargo area).

## Known Issues

- RJTT LDA approaches aren't really LDA approaches with the VPT (visual prescribed track), just a hack ILS approach to a fictional runway.
- No RJTT RNAV 16L/16R due to game limitations (conflicts between parallel arrivals on RNAV track).
- No fair weather 34L/34R approach usage (no visual approaches, conflict on joining parallel ILS at same altitude)
- No RJTO Oshima/RJAN Niijima (not possible to model arrivals from RJTY ACA)
- SELNO arrivals can spawn a bit inside the ACA with no warning.
- Arrival and departure directions can be a bit nonsense (e.g. AHK arriving from the Pacific), unfortunately this is a game limitation.
- South arrivals to RJTT 16L/16R are very close to delayed even strictly following the STAR (game limitation?)

## Changelog

*	1.0 - 2020/10/19 - Initial version.
*	1.1 - 2020/10/19
	- Add RJAA.
	- bug fixes
*	1.2 - 2020/10/23
	- Flesh out airspace (RJTT/RJAA CTR/PCA, airspace over RJAH/RJTY/RJTU ACA, RJTL/RJTE/RJTK CTR)
	- Adjustments to entry points
	- Remove hack as multiple departures on one runway work now
	- Add basic SIDs to show exit fixes
	- Display minor fixes using basic SID exit fixes
	- Correct name of RJTT
	- Correct reading of OLVAN2.SAMUS STAR
	- Correct spelling of BEKLA2B SID
	- Fix approaches from GIINA, TEMIS, ACELA, MARCH to actually work
	- Add case for approach from NOVEL when already south of NOVEL
*	1.3 - 2020/10/24
	- Extend RJTT LAXAS SID to KAGNA
	- Shorten RJTT ROVER SID AKAGI transition to the exit point from the ACA, CLARK
	- Add RJTT VAMOS SID XAC transition to B586
	- Adjusted entry points
	- Adjust label for Shimofusa CTR
	- Add readme
*	1.3.1 - 2020/10/25
	- Correct CCA callsign pronunciation for RJAA
*	2.0.0 - 2020/11/02
	- Add approaches to many, many fixes as the approach limit has been lifted.
	- Add RJTT 16L/16R ILS approaches
	- Add RJTT "LDA" 22/23 approaches
	- RJAA arrivals now fly direct to first point inside RJTT ACA on their arrival route instead of NRE.
	- Adjusted entry points
	- Added missing ALDEN waypoint for some STARs from AROSA
	- Adjusted traffic frequencies
	- Changed name of RJAA airport for voice purposes
*	2.0.1 - 2020/11/02
	- Fix aircraft failing to intercept the localizer for LDA approaches by changing name of runway
*	2.0.2 - 2020/11/02
	- Add CAMEL fix as IF for 34R and appropriate transitions. Now CREAM is no longer both the point merge fix and initial approach fix for 34R, and aircraft can shortcut from 2C arrivals direct to CREAM and fly the 34R approach via CREAM transition.