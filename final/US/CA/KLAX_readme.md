# Los Angeles (Socal Area) For Endless ATC

This implements Los Angeles International Airport (KLAX), Bob Hope Airport (KBUR), Long Beach (Daugherty Field) Airport (KLGB), and Hawthorne Municipal Airport (KHHR) into the [Endless ATC](https://steamcommunity.com/app/666610) game.

## Features

### Implemented

* Arrivals and departures at KLAX, KBUR, KLGB and KHHR.
* Departures thats (somewhat) mirror the actual SID's.
* Custom traffic to match GA and Airlines at KBUR and KLGB.
* Custom SIDS that match the departure path perfectly.

### Planned

* Airspace boundries and regions.
* KLAX Custom Traffic (only 2 or 3 airlines serve KBUR and KLGB so they where much easier to implement).
* Multiple runway configs (not implemented yet since Socal is extremly rarely in east ops).

## Issues

Due to the limitations of [Endless ATC](https://steamcommunity.com/app/666610) there are many aspects that are not particuarly accurate.

* Only around 50% of SIDS are included for KBUR and KLGB, and only around 20% are included for KLAX (Los Angeles has 23 SID's).
* No STARS since there is currently no way to model this.

## Credits

Thanks to Startgrid for this amazing game! Without him this wouldn't be happening. I used Jeppson charts from [Navigraph Charts](https://navigraph.com/products/charts). You can get the exact same charts from many other places online for free, eg. [Airnav](https://www.airnav.com/airport/KLAX). All fix and navaids data and coodinates was provided by [Airnav](https://www.airnav.com). All airport and runway data was provided by [OurAirports](https://ourairports.com/).

## Changelog

* 1.3 - 10/31/2020 - Custom SIDS, updated entrypoints.
* 1.2 - 7/31/2020 - Added KHHR support for increased GA traffic.
* 1.1 - 7/28/2020 - Initial Release. Includes KLAX, KBUR, and KLGB.
