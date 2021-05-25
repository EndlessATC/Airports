# PVD ATCT/TRACON (Version 1.0)
This is a recreation of the real-world FAA facility PVD for [Endless ATC](https://steamcommunity.com/app/666610). 
The PVD ATCT/TRACON in the real-world covers the Providence International Airport (KPVD) and its surrounding satellites,
New Bedford (KEWB) and Groton-New London (KGON).

All data in this is based on the FAA's data (AIRAC 2102) which it provides to the public for free. Minimum altitudes are based off
the real-world PVD MVA map (also provided to the public by the FAA).

## Airports
### `KPVD` T.F. Green International Airport
T. F. Green International Airport is a public international airport in Warwick, Rhode Island, United States, 6 miles
south of the state's capital and largest city of Providence. Opened in 1931, the airport was named for former Rhode Island 
governor and longtime senator Theodore Francis Green. While KPVD is located underneath Class C airspace in real life, 
this is not implemented.

### `KEWB` New Bedford Regional Airport
New Bedford Regional Airport is a Part 139 Commercial-Service Airport, municipally-owned and available for public use.
The airport is located three nautical miles northwest of the City of New Bedford, a city in Bristol County, 
Massachusetts, United States.

### `KGON` Groton-New London Airport
Groton–New London Airport is a state-owned public-use airport located three nautical miles southeast of the central 
business district of Groton, a town in New London County, Connecticut, United States.


#### STARs
In this version of PVD, all 2 STARs are implemented:
<ul>
<li>WIPOR2 (at ORW)</li>
<li>JORDN2</li>
</ul>
All aircraft will arrive inbound direct their gate. From there, you can click on the `APP` button to put them on the
STAR transition.

##### A note on vector segments
On the JORDN2 arrival, all aircraft leave the final fix (MINNK) on a 015 heading regardless of the runway configuration.
In a land 16/23 config, aircraft will be on a right base for runway 23 on the WIPOR3 arrival. In the land 5/34 config, aircraft
will be put on a 10 mile left base for runway 5.

#### SIDs
There are no SIDs at PVD. All aircraft will leave the PVD airspace via PUT or JUMPR.
