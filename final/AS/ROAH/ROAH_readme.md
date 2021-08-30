**DUE TO NATURE OF TRAFFIC AT THE `ROAH` AERODROME, THIS AIRPORT FILE HAS QUIRKS RELATED TO MILITARY AIRCRAFT TO/FROM `ROAH`.**

# `ROAH` ACA 1.0.0

This is an implementation of the Naha ACA (Approach Control Area) for [Endless ATC](https://steamcommunity.com/app/666610) featuring `ROAH` Naha Airport in Okinawa, Japan, as well as `RODN` Kadena Air Base and `ROTM` MCAS Futenma. The airspace ceiling is FL200.

Based on AIP Japan (Ministry of Land, Infrastructure, Transport and Tourism) (https://aisjapan.mlit.go.jp/html/AIP/html/DomesticAIP.do). The choice of SIDs and STARs may not be 100% accurate to real life but should be reasonably accurate reflecting daytime IMC conditions. All aircraft are assumed to be RNAV capable; no conventional NAVAID-based SIDs or STARs are implemented unless there is no RNAV alternative. Coastline data from naturalearthdata.com. 

The Naha ACA is a mostly circular terminal area typical for an island airport. There is a heavy military presence, and military training areas are scattered around the main island as well between the airways that extend out from the Naha `NHC` VORTAC. Approach and departure paths cross over/under each other just north of Naha, and there are many potential conflict points to the west/east of Okinawa as well. The majority of traffic enters the ACA from the northeast from mainland Japan and southwest from the other Ryukyu islands such as Miyakojima and Ishigaki. USAF training area W-178(A) is depicted as inactive for gameplay purposes. Expect heavy use of vectors, especially as traffic increases.

STARs are implemented as approach transitions. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. Multiple approaches may be available from a fix, to the same airport or even different airports. Pressing the APP button again before issuing the approach clearance (do not long press) will select the next approach available from that fix. If the aircraft is already on an approach from that fix, you will need to cancel the approach clearance first before issuing another approach clearance.

`ROKR` Kerama, `RORA` Aguni, `RORE` Iejima, and `RODE` Ie Shima Auxiliary are not represented due to a lack of traffic to/from outside of the ACA. However, the runways of the former three airports are shown on the map.

## Airports

### `ROAH` Naha

The main airport of this sector. Jointly used by civilian and JSDF traffic, this airport on the southern tip of Okinawa Island has added a new parallel runway in the sea to the west in response to increased traffic including the increases in scrambles of fighter jets. Unlike Chitose in Hokkaido, civilian and military traffic use the same runways, meaning passengers onboard airliners are able to see fighters taking off with afterburners from their window seat.

As a controller, the mix of aircraft may be more exciting than the normal airport, but will need attention when the `F16` zooming along catches up to the `AT46`... STARs are available, however in real life vectors are used heavily.

**SOME MILITARY AIRCRAFT (`F16`, `T4`, `P3`, `E2`) ARE DEPICTED AS AIRCRAFT LANDING AT "`JF`" AERODROME FOR TECHNICAL REASONS. THESE AIRCRAFT SHOULD LAND AT `ROAH`.**

There is custom traffic for `ROAH`. The proportions are very much estimates but shouldn't be too far off from reality.

Major fixes on the map have a defined hold including many fixes along the STARs. The published hold for missed approaches is `OLVAL`.

Aircraft arrive at 3 points:

- `PRIUS` -`Y525`-> `IHEYA` (north/north east from mainland Japan/Korea)
- `GEMNI` -`Y57`-> `VELNO` (southwest from western Ryukyu Islands/Taiwan)
- `BUICK` -`V75`-> `NANJO` (east from Daito Islands/Pacific Ocean)

Aircraft depart via:

- `CHAMP` (north via `Y579` to Korea)
- `AMAMI` (north/northeast via `Y574`/`Y53`/`Y25` etc. northeast for mainland Japan)
- `BUICK` (east via `V75` for Daito Islands/Pacific Ocean)
- `GANJU` or `CANOP` depending on runway (southwest for western Ryukyu Islands/Taiwan)

There are two runways:

- 18L/36R
- 18R/36L (new west parallel runway)

Two landing configurations are in general use:

-	Landing 36L, departing 36R
	
	The west runway is used for arrivals while the east runway is used for departures. In real life, traffic may land 36R for a shorter taxi if traffic allows.

	Approaches to 36L are available from `BLISS`.

	STARs are available using APP mode from `IHEYA`, `VELNO`, `BUICK`, and some intermediate points on the STARs. Military aircraft may only engage app mode from certain outer fixes due to technical reasons; recommend vectors to final if not suitable STAR available.

	Use caution for departures towards `KIZNA` conflicting with 05 arrivals to `RODN`. Vectoring may be required to the west at altitude 1200 to clear `RODN` 05 arrivals descending through 2200 at `JIMMY`.

	Simultaneous approaches to 36L and 36R are NOT authorized.

-	Landing 18R, departing 18L
	
	The west runway is used for arrivals while the east runway is used for departures. In real life, traffic may land 18L for a shorter taxi if traffic allows.

	Approaches to 18R are available from `SALSA`.

	STARs are available using APP mode from `IHEYA`, `VELNO`, `BUICK`, and some intermediate points on the STARs. Military aircraft may only engage app mode from certain outer fixes due to technical reasons, **except for from `VIGER`**. **FOR `JF` AIRCRAFT, TO INITIATE AN APPROACH FROM `VIGER`, USE THE SECOND APPROACH BY SELECTING "APP" TWICE. THE ASSIGNED APPROACH SHOULD BE TO RWY `18LJF` VIA 15 DME ARC CCW. *`JF` aircraft will go around if the runway selected is `18L`.*** Recommend vectors to final if not suitable STAR available.

	Use caution for arrivals conflicting with 05 arrivals to `RODN`. `RODN` arrivals may need to held over `JACKS` for a gap in `ROAH` arrivals.

	Simultaneous approaches to 18L and 18R are NOT authorized.

### `RODN` Kadena Air Base

This is the USAF's home in Okinawa. A variety of aircraft, military or chartered civilian, fly in and out of this aerodrome going to training areas or other USAF bases in Japan/Guam/USA.

There is custom traffic for `RODN`. The proportions and callsigns are very much plain guesses however, no assertions are made regarding accuracy (instead, assertions are made regarding its *inaccuracy*.)

Major fixes on the map have a defined hold. 

Aircraft depart to ATS routes via `BASHO` `BUICK` `DODGE` or `ONC`, or to the North Range and South Range. There are real life SIDs but they are all just two points in a (mostly) straight line after departure to a waypoint not connected to the ATS routes. Therefore no SIDs are implemented, just a heading after departure. Departures should be vectored until direct to exit point can be issued.

There are two runways:

- 05L/23R
- 05R/23L

There are two simple runway configurations:

-	Landing 05L, departing 05R
	
	The north runway is mainly used for arrivals and the south runway is mainly used for departures.

	Approaches to 05L are available from `JACKS` etc.

	No STARs are available, arrivals should be vectored to `JACKS` or other fixes on the approach.

	Use caution for `ROAH` arrivals to 18s or departures from 36s. Arrivals must descend through 2200 at `JIMMY` to remain on GS. Recommend vectors for `ROAH` 36 departures to maintain separation. ~~Recommend holding `RODN` arrivals at `JACKS` until gap can be made in `ROAH` 18 arrivals.~~ **Due to conflicts with `ROAH` 36 departures, 05L has been raised 500ft to displace the glideslope so 05 approaches do not conflict.** However, the `JIMMY` 2200 restriction has been maintained to simulate the original GS.

	The published hold for missed approaches is straight ahead to `IMONO`.

-	Landing 23R, departing 23L
	
	The north runway is mainly used for arrivals and the south runway is mainly used for departures.

	Approaches to 23R are available from `IMONO` etc.

	No STARs are available, arrivals should be vectored to `IMONO` or other fixes on the approach.

	Use caution for `ROAH` arrivals to 18s or departures from 36s. Departures must climb to at least 2200 to clear. **Due to conflicts between 05 arrivals and `ROAH` 36 departures, 05L/23R has been raised 500ft to displace the glideslope.** However, the altitudes for the fixes along the 23R ILS have been maintained to simulate the original GS.

	The published hold for missed approaches is straight ahead to `JACKS`.

### `ROTM` MCAS Futenma

A USN airfield south of Kadena. Most traffic would be helicopters to training areas around Okinawa, but there is some fixed wing traffic to other US military facilities.

There is custom traffic for `ROTM`. The proportions and callsigns are very much plain guesses however, no assertions are made regarding accuracy (instead, assertions are made regarding its *inaccuracy*.)

Aircraft depart to ATS routes via `BASHO` `BUICK` `DODGE` or `ONC`. No SIDs are implemented, just a heading after departure. Departures should be vectored until direct to exit point can be issued.

There is one runway:

- 06/24

There are two simple runway configurations:

-	Landing and departing 06

	No approach fixes are available, and no STARs are available, arrivals should be vectored to final.

	Use caution for `ROAH` traffic under the approach path and parallel `RODN` arrivals to the north.

-	Landing and departing 24

	No approach fixes are available, and no STARs are available, arrivals should be vectored to final.

	Use caution for `ROAH` traffic under the departure path and parallel `RODN` arrivals to the north.

### `ROKJ` Kumejima

A runway with a small apron on this island west of Okinawa. The only scheduled service is to `ROAH` Naha, and a seasonal service to `RJTT` Tokyo Haneda. 

There is custom traffic for `ROKJ`. Unfortunately, traffic to `ROAH` cannot be simulated due to the game not supporting this. Only the seasonal traffic to/from the northeast is simulated.

Aircraft depart and arrive via the `NHC` - `LAVON` - `GURUX` - `DORIS` corridor.

There is one runway:

- 03/21

Only one runway configuration is implemented:

-	Landing and departing 03

	Approaches are available from `DUFFY` and `DORIS`.

	The published hold for missed approaches is a *left* turn to `DORIS`.

## Known Issues

- Have different types of traffic use different entry/exit gateways are not possible in this game, therefore aircraft using civil and military routes are separated by duplicating `ROAH`, which means there are two runways each of 18L/36R and 18R/36L. As the game will allow you to select approaches meant for a different airport if they share a starting fix with an approach for the airport the selected aircraft is landing at, this can lead to military aircraft flying the "civilian" approach and going around due to trying to land at the "wrong" airport. To avoid this issue, civil and military aircraft landing `ROAH` do not have approaches that share fixes.
- Many areas have their ceiling marked as "0" as they are likely not active for all of their hours of operation and interfere with standard flight paths, or because they are shared with traffic to different airports (which is not supported by the game)
- No `ROAH`-`ROKJ` traffic
- No `RODN` SIDs - the SIDs are available on the AIP, but the connecting routes to airways are not published as airways or procedures, or even as direct routes or flight planned routes via AIC. Author is only aware of one - `ADDAN` (`DCT`) `BASHO` (`DCT`) `AMAMI`. In fact, `BASHO` does not appear to be used for any other purpose...

## Disclaimer

This is a best effort work based on air traffic observations and official aeronautical publications. No guarantee is made that the representation of Naha ACA matches real life procedures in any way. Especially, procedures around `RODN` Kadena and `ROTM` Futenma may be grossly inaccurate, and callsigns for military aircraft are very likely to be either incorrect, out of date, or completely fabricated. Any information (that is not classified or secret in any way) regarding inaccuracies is appreciated.

## For Developers

This file is built from `source\ROAH.txt` via `deploy.py`. Make any contributions to `source\ROAH.txt` and NOT to `.\ROAH.txt`.

## Changelog

*	1.0 - 2021/02/08 - Initial version.