# `RKSI` Seoul TMA 1.0.0

This is an implementation of the Seoul TMA (Terminal Control Area) for [Endless ATC](https://steamcommunity.com/app/666610) featuring `RKSI` Incheon Airport and `RKSS` Gimpo Airport. The airspace ceiling is FL185.

The Seoul TMA is a fairly cramped airspace, with restricted areas to the north over the border with the North Korea and close to Gimpo over the city of Seoul. To the south lies Osan Air Base and the Osan TMA that lies underneath the southern portion of the Seoul TMA.

Based upon AIP Republic of Korea 2021/06/16. All aircraft are assumed to be RNAV capable; no conventional NAVAID-based SIDs or STARs were implemented unless there is no RNAV procedure published. Coastline data from [naturalearthdata.com].

STARs are implemented as approach transitions. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. Multiple approaches may be available from a fix. Pressing the APP button again before issuing the approach clearance (do not long press) will select the next approach available from that fix. If the aircraft is already on an approach from that fix, you will need to cancel the approach clearance first before issuing another approach clearance.

Endless ATC does not support altitude restrictions for departures, or floor restrictions for arrivals. However, procedures in the Seoul TMA often have such restrictions to ensure separation. Notable restrictions are noted in each airport's section below; following these restrictions should result in a better gameplay experience.

The Seoul TMA is extended to the west and to the south, as well as eastwards around airway G597 for gameplay purposes. `RKSM` Seoul Airbase is not implemented.

## Airports

### `RKSI` Incheon International Airport

The main international airport serving Seoul. This airport was built in the ocean west of Seoul by landfilling between two islands. Note an area north of Incheon which is reserved for IFR traffic and is used by certain arrival and departure procedures.

There is custom traffic for `RKSI`. The proportions are very much estimates but shouldn't be too far off from reality.

Certain fixes visible on the map have a defined hold including some key fixes along the STARs.

Aircraft arrive at:

- `OLMEN` (south from Jeju, Taiwan, SE Asia, Shanghai and southern China)
- `GUKDO` (southeast from Gimhae, Japan, Oceania, NA)
- `REBIT` (west from northern/western China, Europe, Russia, ME etc)
- `KARBU` (east from Yangyang, eastern Russia, or northern Japan and NA via CDR)

Aircraft depart via:

- `BOPTA` (south for Jeju, Taiwan, SE Asia, Shanghai and southern China)
- `OSPOT` (southeast for Gimhae, Kyushu, Oceania)
- `BINIL` (west for northern/western China, Europe, Russia, ME etc)
- `KARBU` (east for Yangyang, eastern Russia, Japan and NA)

There are four runways:

- 15L/33R (arrivals only)
- 15R/33L (departures only)
- 16L/34R (departures only)
- 16R/34L (arrivals only)

STARs and approaches are made with simultaneous approaches in mind, and should maintain at least 1000 ft separation until GS intercept.

The preferred runway for cargo flights in 15L/33R due to a significantly shorter taxi distance.

There are two landing configurations:

-	Landing 33R/34L, departing 33L/34R

This is the preferred configuration for `RKSI`. 

Vectors can be used for sequencing, or direct to fix shortcuts can also be issued (or both). Approaches are available from `ENPIL` and `PAMBI`.

Use caution for arrivals via `REBIT`, the point merge to `PAMBI` is only 500ft above Osan TMA, and planes will descend into Osan TMA if cleared to approach 34L.

The published hold for missed approaches is `GC963` +4000-5000 for the 15s, `DH989` +3000-4000 for the 16s.

-	Landing 15L/16R, departing 15R/16L

This is the south wind configuration for `RKSI`. 

Vectors can be used for sequencing, or direct to fix shortcuts can also be issued (or both). Approaches are available from `MUNAN` and `BITIM`.

Use care to separate arrivals from departures. For arrivals via `SEL`, cross `SEL` +13000, `GC036` +9000, `GC026` +6000. The descent profile to meet -4500 at `GC020` generally requires -210kts by `SEL`. The game will start a descent before SEL that will break these restrictions without speed control, so it is recommended to issue speed 210kts upon leaving the point merge to `SEL`. 

Departures will generally fly under arrivals. For `BINIL` departures, maintain -10000 until `HP100` (until clear of `OLMEN` arrivals). For `BOPTA` arrivals, maintain -13000 until `HD130` (until clear of `OLMEN` arrivals). For `EGOBA` arrivals, 10000 until `CK099` (over `R35`) and -11000 until `EGOBA` may be required depending on traffic from `KARBU`.

The published hold for missed approaches is `GE978` +4000-5000 for the 33s, `PY980` +3000-4000 for the 34s.

### `RKSS` Gimpo International Airport

The main domestic airport for Seoul, located closer to Seoul than Incheon. Limited international flights to key close Asian cities also fly in and out of Gimpo.

There is custom traffic for `RKSS`. The proportions are very much estimates but shouldn't be too far off from reality.

Aircraft arrive at:

- `OLMEN` (south from Jeju etc, Taiwan, Shanghai)
- `GUKDO` (southeast from Gimhae, Japan)
- `REBIT` (west from Beijing)
- `KARBU` (east from Yangyang etc)

Aircraft depart via:

- `BOPTA` (south for Jeju etc, Taiwan, Shanghai)
- `OSPOT` (southeast for Gimhae etc)
- `BINIL` (west for northern/western China, Europe, Russia, ME etc)
- `KARBU` (east for Yangyang, eastern Russia, Japan and NA)

There are two runways:

- 14R/32L (arrival only in south wind configuration)
- 14L/32R (departure only in south wind configuration)

There are two simple runway configurations:

-	Landing and departing 32L/32R

The preferred runway configuration. In real life, the departures and arrivals alternate between the 32s every 3 hours. In the game, two configurations are provided, one for departing 32L and arriving 32R, one for departing 32R and arriving 32L.

The missed approach hold is `CAVOI` +4000-6000.

-	Landing and departing 14L/14R

This is the south wind configuration.

`REBIT` arrivals starting auto descent without speed control will descend into `RKSI` 15/16 arrivals. -250kts at `REBIT` is recommended to allow for a steeper descent profile to maintain separation.

Departures should cross `SEL` or `UP050` (the point immediately southwest of `SEL`) -6000. Departures via `NOPIK` should also cross `UP060` (the second fix west of `SEL`) and `UP059` (the third fix west of `SEL` that starts the due west legs) at 6000 if necessary to keep under `RKSI` arrivals. `KARBU` departures should also remain -9000 after passing `SEL` until `EGOBA`, and will climb to cruise under `KARBU` arrivals.

The missed approach hold is `DOKDO` +4000-5000.

## Known Issues

- No mixed configurations...not sure how to implement the alternate SIDs/STARs at `RKSS` that are used during mixed ops...
- Holds on intermediate STAR fixes may not work correctly, it seems to be a bug in the game.

## Changelog

*	1.0.0 - 2021/07/01 - Initial version.