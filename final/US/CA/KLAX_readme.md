# Los Angeles (Socal Area) For Endless ATC

This implements Los Angeles International Airport (KLAX), Bob Hope Airport (KBUR), Long Beach (Daugherty Field) Airport (KLGB), and Hawthorne Municipal Airport (KHHR) into the [Endless ATC](https://steamcommunity.com/app/666610) game.

## Features

### Implemented

* Arrivals and departures at KLAX, KBUR, KLGB and KHHR.
* Departures thats (somewhat) mirror the actual SID's.
* Custom traffic to match GA and Airlines at KBUR and KLGB.

### Planned

* Airspace boundries and regions.
* KLAX Custom Traffic (only 2 or 3 airlines serve KBUR and KLGB so they where much easier to implement).
* Multiple runway configs (not implemented yet since Socal is extremly rarely in east ops).

## Issues

Due to the limitations of [Endless ATC](https://steamcommunity.com/app/666610) there are many aspects that are not particuarly accurate.

* SID's only head directly to their first waypoints. There is no way to model a complex path for a SID, like on the actual SID's.
* Only around 50% of SIDS are included for KBUR and KLGB, and only around 20% are included for KLAX (Los Angeles has 23 SID's).
* No STARS since there is currently no way to model this.

## Changelog

* 1.2 - 7/31/2020 - Added KHHR support for increased GA traffic.
* 1.1 - 7/28/2020 - Initial Release. Includes KLAX, KBUR, and KLGB.