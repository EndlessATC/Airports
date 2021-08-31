# `RJCC` ACA 1.0.0

This is an implementation of the Chitose ACA (Approach Control Area) for [Endless ATC](https://steamcommunity.com/app/666610) featuring `RJCC` New Chitose Airport (Shin-Chitose) and JASDF `RJCJ` Chitose Air Base. The airspace ceiling is FL200.

Based upon AIP Japan 2021/01/28. The choice of SIDs and STARs may not be 100% accurate to real life but should be reasonably accurate reflecting daytime IMC conditions. All aircraft are assumed to be RNAV capable; conventional NAVAID-based SIDs or STARs were only implemented where there was no clear RNAV alternative. All aircraft are TACAN capable due to how the game works; conversely, military aircraft are all also VOR/DME capable. Coastline data from naturalearthdata.com.

The Chitose ACA is centered around the four runways at Chitose, two civilian and two military. The SIDs and STARs will provide standard patterns towards the runways, however note that they were designed with real life traffic in mind. Therefore, some paths may overlap and climb/descend through each other. Use care around aircraft to/from the north and east as the traffic volumes are low, so departures and arrivals are not segregated and may conflict with each other. Published procedures are lacking for military traffic; they will need to be guided around civilian traffic and will test your vectoring skills.

STARs are implemented as approach transitions. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. Multiple approaches may be available from a fix. Press the APP button again  before issuing the approach clearance (do not long press) will select the next approach available from that fix. If the aircraft is already on an approach from that fix, you will need to cancel the approach clearance first before issuing another approach clearance.

## Airports

### `RJCC` New Chitose Airport (Shin-Chitose)

The main airport of this sector, serving Sapporo as its main gateway to the rest of Japan and the world. As traffic outgrew joint-use facilities at Chitose Air Base, this airport was constructed with two parallel runways located east of the airbase dedicated to civilian use. The outer runway is used for arrivals, while the inner parallel is used for departures. In the winter, the two runways are used in rotation to allow for snow removal.

There is custom traffic for `RJCC`. The proportions are very much estimates but shouldn't be too far off from reality.

Major fixes on the map have a defined hold including many fixes along the STARs. The published hold for missed approaches is `MKE`.

Aircraft arrive at 4 points:

- `BEEBA` -`Y10`/`V1`/`V8`-> `KURIS` (north/north east from northern Hokkaido/Russia)
- `BISEI` -`V5`-> `BOKSO` (east from eastern Hokkaido)
- `OBE` -`V6`-> `RAKNO` (east from Obihiro and Pacific via `OTR1`)
- `SIRAO` -`Y139`-> `NAVER` (south from the rest of Japan, Asia and beyond)

Aircraft depart via:

- `ZALAR` (southwest for western Tohoku and Japan west of Tokyo)
- `TOBBY` (south for eastern Tohoku, Tokyo)
- `BOKSO` (east for eastern Hokkaido)
- `RAKNO` (east for Obihiro, Pacific)
- `KURIS` (north for northern Hokkaido, Russia)

There are two runways:

- 01L/19R (RWY A)
- 01R/19L (RWY B)

Two landing configurations are in general use:

-	Landing 01R, departing 01L
	
	The outer runway is used for arrivals while the inner runway is used for departures.

	Approaches to 01R are available for `YOSEI` and `YODAI`, the closer an approach from 2000 and the further an approach from 3000.

	STARs are available using APP mode from `NAVER`, `KURIS`, `MKE`, and some intermediate points on the STARs. 

	Use caution for `KURIS` arrivals conflicting with departures climbing and turning right from 01L.

	Simultaneous approaches to 01R and either `RJCJ` runway 36L/36R are allowed.

-	Landing 19L, departing 19R
	
	The outer runway is used for arrivals while the inner runway is used for departures.

	Approaches to 19L are available from `KAORY` and `YUNEY`; there are transitions from the west and straight in but there will generally not be an opportunity to use these.

	STARs are available using APP mode from `NAVER`, `KURIS`, `MKE`, and some intermediate points on the STARs. 

	Use caution for `KURIS` arrivals conflicting with departures climbing and turning right from 01L.

	Simultaneous approaches to 01R and either `RJCJ` runway 36L/36R are allowed.

### `RJCJ` Chitose Air Base

The JASDF's main base in Hokkaido. The home base of the Japanese Air Force One is here, and the Japanese Coast Guard also bases a few aircraft here. Fighter jets will be the majority of the traffic in and out of this aerodrome bound for the training areas over the ocean around Hokkaido.

There is custom traffic for `RJCJ`. The proportions are very much estimates however, no assertions are made regarding accuracy.

Major fixes on the map have a defined hold including many fixes along the STARs. The published hold for missed approaches is `ABIRA`.

Aircraft arrive from the northwest from `C`, northeast from `A`, southeast from `B`, and southwest from `SIRAO` to `NAVER`.

Aircraft depart northwest to `C`, northeast to `A`, southeast to `B`, or south to `TOBBY`.

There are two runways:

- 18L/36R
- 18R/36L

There are two simple runway configurations:

-	Landing 36L, departing 36R
	
	The outer runway is generally used for arrivals while the inner runway is used for departures, but the inner runway may also be used for arrivals.

	Approaches to 36R are available from `ABIRA`, `JOMMY` via TACAN arcs from the east, or straight in the ILS.

	STARs are available using APP mode from `NAVER` and `MKE`.

	Use caution for R-138 west of the aerodrome.

	Simultaneous approaches to either 36L/36R and `RJCC` runway 01R are allowed.

-	Landing 19L, departing 19R
	
	The outer runway is used for arrivals while the inner runway is used for departures.

	Approaches to 19L are available from `WAKSA`, or via TACAN arcs from `ABIRA` or `JOMMY`.

	STARs are available using APP mode from `NAVER` and `CHE`.

	Use caution for R-138 west of the aerodrome.

	Simultaneous approaches to either 18L/18R and `RJCC` runway 19L are allowed.

## Known Issues

- No touch and go traffic at `RJCJ`
- No corkscrew approaches at `RJCJ`
- 18R/36L should not have an ILS
- Possible conflicts between `RJCC` and `RJCJ` simultaneous departures

## Disclaimer

This is a best effort work based on air traffic observations and official aeronautical publications. No guarantee is made that this representation of Chitose ACA matches real life procedures in any way. Any information regarding inaccuracies is appreciated.

## For Developers

This file is built from `source\RJCC.txt` via `deploy.py`. Make any contributions to `source\RJCC.txt` and NOT to `.\RJCC.txt`.

## Changelog

*	1.0 - 2020/12/28 - Initial version.