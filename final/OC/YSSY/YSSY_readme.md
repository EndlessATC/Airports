# `YSSY` Sydney International Airport
This is an implementation of `YSSY` Sydney Airport into the [Endless ATC](https://steamcommunity.com/app/666610) game.

## Features
* Valid SID/STARS to current AIRAC 2109
* Parallel Runway operations.
* Real Airlines

## Future Features
* Inclusion of nearby Bankstown (`YSBK`)
* Scenery objects

------------------------------

### `YSSY` Sydney Airport

This is the main airport of the airspace. There is custom traffic, similar to reality. 

Aircraft will use the following STARS:

* `MEPIL3` 
* `MARLN5`
* `RIVET3` 
* `BORE3A` 
* `BORE3P`

##### PLEASE NOTE: When runways 34L/R are active, `MEPIL3` arrivals (inbound `YAKKA`) are not used. Instead direct aircraft to `BOREE` for the `BORE3A`.
There is one more STAR that will not be included due to it being used rarely in real life.

ALL AIRCRAFT are reqiured to follow STAR's until where it stops. When the STAR stops, you need to give vectors to the aircraft to final, apart from the `BORE3P`.

Aircraft will use the following SIDS:

* `KEVIN6`, `ABBEY3`
* `DEENA7`, `KAMPI5`
* `WOL2`, `KADOM1`
* `ENTRA5`
* `MARUB6`
* `RIC5`

Most of these have transitions. If you are confused how the SIDS/STARS work, I suggest taking a look at the [charts](https://www.crc.id.au/xplane/charts/DAPS-2021-JUN-17/Sydney%20Kingsford%20Smith%20(YSSY).pdf) and they will answer most your questions related to them.
 

----------------------------

## Known Issues

I personally have not found any issues. If you have, feel free to tell me. Thanks!

## Changelog

* 1.0.0 - 08/10/2021 - Initial Version
