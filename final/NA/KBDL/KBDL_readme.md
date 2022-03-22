#Y90 Yankee Approach		v1.0		3/18/22

##Overview

Airspace covers a large section of central Connecticut and Massachusetts and underlies Boston Center (ZBW).  Y90 adjoins ZBW Gardner Sector (ZBW36) to the north, Boston Approach (A90) to the east, Providence Approach (PVD) to the southeast, New York Approach (N90) to the southwest, and Albany Approach (ALB) to the northwest.  Y90 provides 24/7 approach/departure service to Bradley (KBDL), Westfield-Barnes (KBAF), Westover (KCEF), Worcester (KORH) and Hartford (KHFD), as well as several uncontrolled airports that are not implemented.

Y90 airspace only extends up to 10,000 ft but the "above" and "ceiling" values are set higher to allow arrivals to be descended to the proper 11,000 ft altitude.  Surrounding approach control shelves that are below Y90 airspace are implemented as area restrictions (see ALB area in the northwest and HF area for N90 in the southwest); the eastern A90 shelf that exists 6,000-10,000 ft to the east of KORH is displayed, but cannot currently be implemented in Endless ATC as of this version.

Managing Y90 is primarily about juggling multiple airports with heavily conflicting departure and arrival flows and less about large amounts of volume to a single airport.  5 runway configs are implemented, one for landing in each cardinal direction (roughly) and one that uses a wind calm configuration with more deconflicted approach paths.

IRL, Y90 also provides en-route service for many KBOS satellite arrivals (KBED, KBVY, KMHT, KASH), descending them from ZBW airspace so they can enter A90 airspace well below KBOS arrival traffic, as well as providing departure and en-route services for KOXC, KBDR and KHVN climbing to Center altitudes (being routed north towards RONGE/VEERS before being put on course to climb above NY arrivals)



## Bradley International (Windsor Locks) Airport, KBDL

Major international airport for Y90, majority of traffic flow.  No co-located VOR, but the fix NELIE exists above the airport.  Mostly air carrier and cargo traffic, with some air charters.  Infrequent GA traffic.

2 runways, 6/24 and 15/33.  6/24 is the preferred runway, but all configurations WILL allow multiple runways.  LAHSO is approved and implemented when landing 24 or 33, reducing the incidence of go arounds for any configuration using those runways.  In all configurations, both runways are used for departures and arrivals unless departures would conflict with arrivals to other airports.  No SIDs exist, and all departures fly headings after departure.

5 arrival paths exist:
1) From the NW on the STELLA1 descending to 11,000;		primary arrival route
2) From the SW on the DPK3 over MAD, descending to 11,000;	primary arrival route
3) From the W, direct JUDDS at 9,000
4) From the N over KEYNN, direct NELIE, descending to 10,000
5) From the E over BOS, direct NELIE, descending to 11,000

Suggested techinques:

Landing 6/33

Arrivals over DPK3 and JUDDS land 6, STELLA1 arrivals taken on a long left downwind for 33, arrivals over KEYNN taken merged into the flow near final (in low traffic) or near the airport (with more traffic), arrivals over BOS merged on final.  This gives the most room for sequencing the NW, N and E flows for 33 while keeping clear of KBDL departure traffic.  33 LAHSO in use.

Landing 24/33

Arrivals over STELLA1, and NELIE land 24, DPK3, BOS, JUDDS land 33.  This takes advantage of the unused space south of KBDL in this configuration to merge the DPK3 and JUDDS flows with extra room for the BOS flows.  24 LAHSO in use.

Landing 24/15

Arrivals over STELLA1 and JUDDS land 15, DPK3, BOS and KEYNN land 24.  Same reasoning as above, note that the STELLA1 arrival sets up for a 15 approach but requires prompt descent.  24 LAHSO in use.

Landing 6/15

Arrivals over STELLA1, BOS, KEYNN land 15, DPK3, JUDDS, BOS land 6.  BOS flow should be merged opportunistically.  No LAHSO in use, lower average arrival rate than other configurations.


## Worcester Regional Airport, KORH (implemented as OR)

Secondary airport located east of KBDL, primarily air charters and GA, some air carriers.  Pronounced in-game with an extreme Boston accent, as "Wustuh".  I am told that this is the correct way to pronounce it.  No co-located VOR or fix.

2 runways, 11/29 and 15/33.  11/29 is the preferred runway, but landing 29 requires backtracking.  When 11/15 are in use, 11 is used for arrivals and departures, 15 for departures only in this implementation.  When 29/33 are in use, both runways are used for arrivals and departures to allow landing GA traffic when backtracking is occuring on 29.  No LAHSO authorized.  No SIDs exist, all departures fly runway heading.

6 arrival paths exist:
1) From the NW on the STELLA1 descending to 11,000
2) From the SW on V1 over MAD, descending to 11,000
3) From the W, direct JUDDS at 9,000
4) From the N over GDM, direct SPENO, descending to 4,000
5) From the E over BOS, direct GLYDE, at 4,000
6) From the S over ORW, direct GRAYM, descending to 11,000

Traffic volume at ORH doesn't require anything clever, the main difficulties are 1) separating from the arrivals as they overfly the rest of the approach airspace and 2) remembering it exists, due to its relative distance from the other airports.  Diversions due to forgetting about aircraft on downwinds for runway 29 can be common without a proper scan.

ORH sits at a relatively high elevation, allowing for relatively short downwinds and finals despite being surrounded by 3000 ft MVA areas.

## Westfield-Barnes Regional Airport, KBAF (implemented as BA)

Secondary combined military/civil airport located north of KBDL and west of KCEF, primarily military and air charter flights, with some GA.  BAF VORTAC located on the airport field

2 runways, 2/20 and 15/33, though only 2/20 is used in this implementation.  No SIDs exist, all departures fly runway heading.

5 arrival paths exist:
1) From the NW on the STELLA1 descending to 11,000
2) From the SW on the DPK3 over MAD, descending to 11,000
3) From the W, direct JUDDS at 9,000
4) From the N over KEYNN, direct BAF, descending to 6,000
5) From the S over ORW, direct GRAYM, descending to 11,000

Difficulty with this airport heavily depends on the runway in use.  Landing 20 makes arrivals easy as they can be kept far north of all traffic, though the departures quickly enter the airspace where KBDL departures/arrivals are.  Landing 2 has arrivals overflying KBDL, requiring careful selection of altitudes, but departures are kept well north of nearly all conflicts.  Arrival traffic often interacts with CEF arrival traffic.

## Westover ARB/Metro Airport, KCEF (implemented as CE)

Secondary combined military/civil airport located north of KBDL and east of KBAF, primarily military and air charter flights, with some GA.  CEF TACAN located on the airport field

2 runways, 5/23 and 15/33, though only 5/23 is used here.  No SIDs exist, all departures fly runway heading.

5 arrival paths exist:
1) From the NW on the STELLA1 descending to 11,000
2) From the SW on the DPK3 over MAD, descending to 11,000
3) From the W, direct JUDDS at 9,000
4) From the N over KEYNN, direct CEF, descending to 6,000
5) From the S over ORW, direct GRAYM, descending to 11,000

Difficulty with this airport matches that with BAF.  Landing 23 makes arrivals easy but complicates departures; notably departures get very close to the BDL runway 24 approach path.  Landing 5 has arrivals overflying KBDL, with departures clear of most traffic.  Arrival traffic often interacts with BAF arrival traffic.

## Hartford-Brainard Regional Airport, KHFD (implemented as HF)

Secondary civil airport located south of KBDL, entirely GA flights

2 runways, 2/20 and 11/29, though only 2/20 is used here.  No SIDs exist, all departures fly runway heading.  The approach to runway 02 is not a typical ILS or LOC approach, it is an LDA approach that is angled by 21 degrees from the runway approach course.

5 arrival paths exist:
1) From the NW on the STELLA1 descending to 11,000
2) From the SW direct HFD, descending to 5,000
3) From the W, direct JUDDS at 7,000
4) From the N over GDM, direct WITNY, descending to 10,000
5) From the E over BOS, direct HFD, at 6,000

A large number of departures from this airport will be light aircraft that stay in approach airspace until the edge.  The challenge here is due to the flying-roadblock nature of GA arrivals and departures from this airport.