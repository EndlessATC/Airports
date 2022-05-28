# KPIT Pittsburgh Approach		v1.0		4/19/22

## Overview

Airspace covers the airspace around Pittsburgh, overlying sections of western Pennsylvania, eastern Ohio, and a small section of northern West Virginia, completely underlying Cleveland Center (ZOB).  PIT adjoins Cleveland Approach (CLE) to the west, Youngstown Approach (YNG) to the North, Johnstown Approach (JST) to the east, Clarksburg Approach (CKB) to the southeast, and ZOB Morgantown Sector (ZOB55) to the southwest. Overlying center sectors are ZOB Clarion Sector (ZOB50) to the north and northeast, ZOB Indianhead Sector (ZOB53) to the east and southeast, ZOB Morgantown Sector (ZOB55) to the south and southwest, and ZOB Briggs Sector (ZOB06) to the west and northwest.

PIT airspace extends up to 14,000 ft in the central 30nm ring, but only up to 4,000ft in the southeast extension for approaches to KHLG.  The boundary between those ceilings is depicted but cannot be effectively implemented in-game.  No other shelves exist in this airspace.

Managing PIT is primarily focused on traffic flows into KPIT itself and the conflicts between that traffic flow and the arrivals to the satellite airports.  KBVI, KAGC and KHLG are implemented as secondary airports as the only other towered airports in the approach.

## Changelog
#### V1.0
	Initial Release

## Pittsburgh International Airport, KPIT

Major international civil/military airport for PIT, majority of traffic flow.  No co-located VOR since decommisioning of MMJ (Montour), but the DME still exists and the fix still exists in GPS FMS.  Mostly air carrier and cargo traffic, with some air charters and military.  Infrequent GA traffic.

4 runways, 10L/28R, 10C/28C, 10R/28L, 14/32.  Two configurations exist, whether landing west or east, allowing for 3 possible landing runways and 2 or 3 departure runways.  No LAHSO is approved for KPIT, and operations on runway 14/32 conflict with operations on 10C/28C and 10R/28L.  Simultaneous departures are possible during both west and east operations.  No RNAV SIDs exist, all departures fly headings on departure.

4 arrival paths exist:
1) From the NW on the JESEY4 descending to 10,000
2) From the SW on the FEWGA7 descending to 10,000
3) From the NE on the HAYNZ7 descending to 10,000
4) From the SE on the DEMME4 descending to 10,000


### Suggested techinques:

#### Landing West

This is the calm wing configuration.

RWY 28R, 28L and 32 are available for landings.  28R should be the primary arrival runway, and then either 28L or 32 should be picked as the secondary runway, with the remaining runway as a prop arrival runway to avoid large overtakes or to handle emergencies; attempting to use both 32 and 28L for heavy flows is _possible_, but requires careful planning to avoid go-arounds and creates congested airspace around KAGC to the SE of KPIT that interferes with departures.

Arriving aircraft will be automatically on the 28R/28C/28L transitions, but can be put on the 32 transition if desired.  Each STAR can be rejoined at any of the downstream fixes, and no STARS include speed or altitude restrictions except the DEMME4 RWY 32 transition (to auto-tie into the approach to 32).

Generally, I find allocating JESEY and HAYNZ arrivals to 28R and FEWGA and DEMME arrivals to 28L/32 to have the most success.  Initial descent on JESEY and FEWGA arrivals to 6,000 (bottom of arrival sector airspace there) and HAYNZ and DEMME to 7,000 (to ensure vertical separation between the flows), with JESEY and HAYNZ arrivals further descended to 4,000 and 5,000 after passing abeam the airport / turning to their downwind leg.  This allows for vertical separation when putting traffic onto 28R and 28L.

Note that FEWGA arrivals _must_ remain AOB 6,000 until a few miles past the 32 approach course to maintain separation from aircraft that are on approach to 32 unless they have been pushed down to 4,000 ft.  FEWGA and DEMME arrivals should not be descended below 4,000 to allow for KAGC departures to climb to 3,000 ft.


#### Landing East

This configuration  is only used when winds require.

RWY 10L, 10R and 14 are available for landings.  10L should be the primary arrival runway, and 10R should be picked as the secondary runway.  14 is available for approaches, but is rarely used for landings.  Operations on 14 conflict with 10L, 10C and 10R (due to the approach path and the runway crossings).  Note that there is no 14 transition on any of the STARs, and so landing aircraft there require vectors.  Fewer arrival conflicts with KAGC departures, but greater conflict between KPIT departures and KAGC arrivals.  Far more confilcts between arrival traffic and KBVI/KHLG traffic.

Arriving aircraft will be automatically on the 10L/10C/10R transitions.  Each STAR can be rejoined at any of the downstream fixes, and no STARS include speed or altitude restrictions

I've found that this configuration is best handled as a 180 degree rotation of the west configuration.  Initial descent of DEMME and HAYNZ arrivals to 6,000 and JESEY and FEWGA arrivals to 7,000.  DEMME and FEWGA arrivals can then descend to 4,000 and 5,000 for turns onto final, allowing easier descent of KAGC arrival traffic over the top of them.

Note that HAYNZ arrivals _must_ remain AOB 6,000 until a few miles past the 14 approach course to maintain separation from aircraft that are on approach to 14 unless they have been pushed down to 4,000 ft.

## Beaver County Airport, KBVI (implemented as BV)

Secondary civil airport located northwest of KPIT, primarily air charters and GA.  No co-located VOR, closest is EWC (Elwood City) to the east.  Activates at a score of 8.

1 runway, 10/28.  No SIDs exist, all departures fly runway heading.

3 arrival paths exist:
1) From the NE direct to EWC, descending to 4,000
2) From the SW over WISKE then direct EWC, descending to 10,000
3) From the SE over NESTO then direct EWC, descending to 10,000

Traffic volume at KBVI is relatively low and simple, the main complexity involves arrivals and departures that cross the rest of the airspace and that interact with arrivals to KPIT.  Arrivals from the south should be kept on top of KPIT arrival traffic until there is space to push them down; minimal vectoring should be necessary other than to keep them clear of KPIT departure traffic.

## Alleghany County Airport, KAGC (implemented as AG)

Secondary civil airport located southeast and very nearby KPIT, primarily air charters and GA.  No-colocated VOR, closest is AGC (Alleghany).  Activates at a score of 12.

2 runways, 10/28 and 13/31, 10/28 is the primary runway, used for departures and arrivals, while 13/31 is only used for departures.  No SIDs exist, all departures fly headings, but the headings vary depending on configuration.

4 arrival paths exist:
1) From the NW over CUTTA then direct AGC, descending to 10,000
2) From the NE over GRACE then direct AGC, descending to 10,000
2) From the SW over WISKE then direct AGC, descending to 7,000
4) From the SE direct AGC, descending to 5,000

Difficulty with this airport is its interaction with KPIT:

#### Landing West

KAGC arrivals, while a source of some conflicts, are not the primary issue.  KAGC departures will conflict with either KPIT 32 or KPIT 28L/28R approaches and will either need to be vectored clear or capped at 3,000 until clear.  Departures north will fly a 040 heading and can either be capped under the 28L/28R approaches or vectored east to climb.  Departures south and west will fly a 250 headings and will need to be capped beneath the 32 approach.  3,000 is the highest safe altitude for these departures until clear of the approach course.

#### Landing East

KAGC arrivals from the NW and NE can require some vectoring to get underneath the KPIT arrivals (since the DEMME4 arrival to 10L/10C/10R runes nearly over the approach course.  Overall, a much simpler configuration.

## Wheeling Ohio County Airport, KHLG (implemented as HL)

Secondary civil/military airport located southwest of KPIT, primarily air charter flights, with some GA and civil air patrol.  No-colocated VOR, closest is HLG (Wheeling).  Activates at a score of 16

2 runways, 3/21 and 16/34.  No SIDs exist, all departures fly runway heading.

4 arrival paths exist:
1) From the NW over CUTTA then direct HLG, descending to 10,000
2) From the NE over GRACE then direct HLG, descending to 10,000
2) From the SW direct HLG, descending to 5,000
4) From the SE direct HLG, descending to 5,000

No significant difficulty with this airport besides it being relatively far from the center of the airspace and your center of attention.
