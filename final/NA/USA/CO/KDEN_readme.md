# D01 TRACON (Version 1.0)
This is a recreation of the real-world FAA facility D01 for [Endless ATC](https://steamcommunity.com/app/666610). 
The D01 TRACON in the real-world covers Denver International Airport (KDEN) and its numerous satellites, which include
Centennial (KAPA), Rocky Mountain Metro (KBJC), Northern Colorado Airport (KFNL), and the Colorado Air and Space Port (KCFO).
These satellite airports are not currently implemented in this rendition of the D01, however, they may be in the future.

D01 also covers Grand Junction (KGJT) and Pueblo (KPUB) as a detached section of the TRACON, however, this is not simulated in
this rendition due to the sheer size the TRACON would have to be.

All data in this is based on the FAA's data (AIRAC 2102) which it provides to the public for free. Minimum altitudes are based off
the real-world D01 MVA map (also provided to the public by the FAA).

## Airports
### `KDEN` Denver International Airport
Denver International (also known as DIA) is the largest airport in the U.S., with 4 north-south parallel runways and 2 
east-west parallel runways. Denver is surrounded by the Rocky Mountains to the west, presenting an interesting challenge
when vectoring aircraft to and from the west. DIA is a hub airport for Frontier Airlines and United Airlines, dominating much of the traffic
at DIA. DIA is also a focus city for Southwest, and is serviced by every major U.S. airline. While KDEN is located underneath
Class B airspace in real life, this is not implemented.

#### STARs
In this version of KDEN, 4 STARs are implemented:
<ul>
<li>SSKII2 (southwest gate)</li>
<li>FLATI2 (northwest gate)</li>
<li>CLASH3 (southwest gate)</li>
<li>AALLE2 (northeast gate)</li>
</ul>
All aircraft will arrive inbound direct their gate. From there, you can click on the `APP` button. In order to select a 
different runway transition, tap on the `APP` button again until the correct runway transition is selected.

##### A note on vector segments
In the real world, many of these STAR segments end on a vector track (airplanes continue to fly a specified heading). 
However, this is not possible to implement in Endless ATC, so it is instead implemented by a 20 mile extension past the
final waypoint. You must vector these planes to final, or they may present a conflict later on if you forget about them!
You can recognize these as the turn-to-final is one greater than 90 degrees.

#### SIDs
In this version of KDEN, all RNAV SIDs are implemented that are RNAV-off-the-ground. Many of the SIDs at KDEN are vector-based
if the aircraft is taking off in the opposite direction of the departure gate (i.e. an EMMYS7 departure off of runway 25). For this reason, departures
in this rendition are a little easier than real life, but are still very interesting!

#### Runway Configurations
All runway configurations used at KDEN are implemented. Besides each runway configuration is a number called the "AAR."
This stands for "Arrival Acceptance Rate," and signifies how much traffic KDEN can accept in any given hour. Denver has the
highest AAR of any airport in the world!

__South Calm (Default Configuration)__  (114 AAR)

Arrive: 16L, 16R, 17R\
Depart: 8, 25, 17L\
Winds: 080-259 degrees, less than 10 kts

__North Calm__ (114 AAR)

Arrive: 34R, 35L, 35R\
Depart: 8, 25, 34L\
Winds: 260-079 degrees, less than 10 kts

__Northwest__ (152 AAR)

Arrive: 26, 34R, 35L, 35R\
Depart: 25, 34L\
Winds: 260-349 degrees, 11-25 kts

__Southwest__ (152 AAR)

Arrive: 26, 16L, 16R, 17R\
Depart: 25, 17L\
Winds: 170-259 degrees, 11-25 kts

__Southeast__ (152 AAR)

Arrive: 7, 16L, 16R, 17R\
Depart: 8, 17L\
Winds: 080-169 degrees, 11-25 kts

__Northeast__ (152 AAR)

Arrive: 7, 34R, 35L, 35R\
Depart: 8, 34L\
Winds: 350-079 degrees, 11-25 kts

__North All__ (114 AAR)

Arrive: 34R, 35L, 35R\
Depart: 34L, 34R\
Winds: 300-049 degrees, greater than 26 kts

__South All__ (114 AAR)

Arrive: 16R, 17L, 17R\
Depart: 16L, 17L\
Winds: 120-219 degrees, greater than 26 kts

__West All__ (48 AAR)

Arrive: 26, 25\
Depart: 25\
Winds: 220-299 degrees, greater than 26 kts

__East All__ (48 AAR)

Arrive: 7, 8\
Depart: 8\
Winds: 050-119 degrees, greater than 26 kts

__Honey Badger (Arrival Priority)__ (152 AAR)

Arrive: 16L, 16R, 35L, 35R\
Depart: 8, 25\
This configuration provides the highest arrival rates

__Honey Badger (Departure Priority)__ (48 AAR)

Arrive: 7, 26\
Depart: 34L, 34R, 17L, 17R\
This configuration provides the highest departure rates
