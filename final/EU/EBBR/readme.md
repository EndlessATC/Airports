
# Brussels Airport For Endless ATC

This is a file to add EBBR (Brussels Airport) to the [Endless ATC](https://steamcommunity.com/app/666610) game.

## Installation
### Steam
* Download EBBR.txt
* Put it in `Steam/steamapps/common/endless ATC/locations` 
### Android
* Download EBBR.txt
* Put it in `Android/data/com.dirgtrats.endlessatc/files`
## Features
### Implemented
* Arrivals and departures at EBBR
* (Semi-)Realistic arrival- and departure paths
* Realistic airspace
* Secondary airports: EBCI and EBAW
* Multiple runway configurations
### Planned
* Realistic airline schedules. The variety of airlines is quite limited at this time.
## Issues
Endless ATC is a **simple** game. Compromises were made to make the game as realistic and as playable as possible.
* The airspace boundary is a circle of 38NM and doesn't follow the TMA/CTA boundaries.
* Multiple SIDS aren't modelled. Departures make a straight turn to their first waypoint.
* **EBBR**
	* Arrivals call at FL80 everywhere, instead of FL60 at FLO, FL110 at KERKY, etc depending on ruway config. this is a limitation of the game, that can't be fixed. 
	* Departures need to be climbed FL110 instead of FL70. The lowest level Endless ATC allows departures to be climbed to at the moment is FL110.
	* When reaching higher skill levels, arrivals spawn really close to eachother and clog up the airspace around ANT and FLO. In Endless ATC, there is no "radar controller" that sequences the arrivals before entering your airspace. This is how the game is coded.
* **EBCI**
	* Arrival routings are incorrect. Endless ATC only allows one inbound VOR for secondary airports. [The routing BUB - NIVOR - GSY and the B-Arrivals](https://ops.skeyes.be/html/belgocontrol_static/eaip/eAIP_Main/graphics/eAIP/EBCI_STAR01_v10.pdf) can't be implemented.
	* Arrivals call at FL90. This is again a limitation of Endless ATC that can't be fixed.
* **EBAW**

Notice other bugs or issues? Please open an [issue on github](https://github.com/aap007freak/EndlessATC_EBBR/issues).
## Credits
All coordinates and other information with respect to EBBR where directly taken from the [eAIP](https://ops.skeyes.be/html/belgocontrol_static/eaip/eAIP_Main/html/index-en-GB.html).
