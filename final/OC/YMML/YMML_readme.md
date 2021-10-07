# `YMML` Melbourne International Airport
This is an implementation of `YMML` Melbourne Airport into the [Endless ATC](https://steamcommunity.com/app/666610) game.

## Features
* Valid SID/STARS to current AIRAC 2106
* Rwy 16 landing, Rwy 27 takeoff
* Real Airlines

## Future Features
* Inclusion of nearby Avalon (`YMAV`) and Essendon (`YMEN`) airports
* Different runways
* Scenery objects
* RWY16 unlock for takeoffs

------------------------------

### `YMML` Melbourne Airport

This is the main airport of the airspace. There is custom traffic, similar to reality. It may get a bit challanging as the airport in real life can only hold up to 55 aircraft inbound.

Aircraft will use the following STARS:

* `ARBEY6A` (north, north-west)
* `LIZZI8A` (north-east, east)
* `WAREN7A` (south, south-east)
* `WENDY9A` (west, south-west)

There are more STARS, however due to limitations to the game at the moment, they will not be included. This includes some RNAV approaches and non-jet STARS. 

ALL aircraft must follow the STAR until `BELTA`. The only execption is the `LIZZI8A`, where aircraft may fly direct to `BELTA` after `LIZZI`.

Aircraft will use the following SIDS:

* `DOSEL1`, `NONIX3`, `MNG3` (these all follow the same routing up until `PEART`; north, north-east)
* `KEPPA2` (north)
* `SUNTI3` (south)
* `CRENA1`, `ESDIG3` (west, south-west)
* `CORRS9` (east)
* `NEVIS7` (north-west)

Aircraft may travel direct to the last waypoint on the SID, but only for seperation purposes.

----------------------------

## Known Issues

I personally have not found any issues. If you have, feel free to tell me. Thanks!

## Changelog

* 1.0.0 - 11/07/2021 - Initial Version
* 1.1.0 - 07/10/2021 - Added ATC handoff callsigns, changed flow rate, added Virgin Australia A320