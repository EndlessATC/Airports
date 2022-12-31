# Singapore TMA

Version 2.0 *by BestBearrr*

This file replicates the Singapore TMA, featuring Singapore Changi Airport (WSSS) and Singapore Seletar Airport (WSSL).

Airspace ceiling is set at FL240.

Transition Altitude is 11000ft, while Transition Level is FL130.
This means that any altitude in between is not to be used (like FL120).

### Features:

* Simulates current operations (year 2022) at WSSS
  * New third runway 02R/20L in use, while runway 02C/20C is closed for Changi East development works
* SIDs and STARs, as well as 'unique' approaches to runways
* Accurate representation of airlines and plane types as much as possible

This file provides a brief overview of the operations at the airports. Check out the sections below for more information about each airport!

The table below shows the skill points at which an airport or runway is unlocked.

| Skill Level | Airport unlocked |                       Runways unlocked                       |
| :---------: | :--------------: | :----------------------------------------------------------: |
|    START    |       WSSS       | Arrivals: Both runways available<br>Departures: Rwy 02R/20L only |
|      8      |       WSSL       |                WSSL Rwy 03/21 becomes active.                |
|     15      |        -         |       WSSS Rwy 02L/20R becomes active for departures.        |

In Endless ATC, STARs are implemented as approach routes. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. 

### Installation

------

For PC,

1. Place WSSS.txt in the folder `Endless ATC/locations`

For Android,

1. Place WSSS.txt in the folder `android/data/com.dirgtrats.endlessatc/files/` 

   *(You may need to use a file explorer app)*



### WSSS - Singapore Changi Airport

------

#### Runway information

Runway 02L/20R: ILS Approach

~~Runway 02C/20C: ILS Approach~~ (Closed for Changi East development works)

Runway 02R/20L: RNP Approach only

Segregated Mode of Operations: Rwy 02L/20R is the main landing runway while Rwy 02R/20L is the main departure runway.

Speed control: 180 knots by 8 NM from touchdown and thereafter 150 knots until 4 NM from touchdown. 
*(Unfortunately due to game limitations, for RWY 02R/20L only a minimum of 160 knots until IF\* is possible)*

#### Departure and Approach Procedures

* **Initial climb is 3000ft.**

* Handoff arrivals to Tower anywhere within ~10nm.

* Departures & Arrivals to/from the North and West: Note minimum altitude restrictions in the area!

  * Also take note of **WIDD (Batam) Control Zone**. Planes must overfly **at or above 4000ft**! 

* **Departures from runway 02R / 20L**

  CHA1C / CHA1D radar departures: Planes climb on runway heading (023 / 203). Vector them as appropriate first, then direct them to their final waypoint.

  * If there is a **simultaneous departure on runway 02L / 20R**, you may wish to turn the departure on runway 02R/20L to a diverging heading of 040 to ensure initial separation.

|  Runway   | SID Suffix |
| :-------: | :--------: |
| 02L / 20R |   E / F    |
| 02C / 20C |   A / B    |
| 02R / 20L |   C / D    |

**STAR Suffix - Runway 02 is 'A', Runway 20 is 'B'**.

Arriving planes converge at four waypoints (known as "entry gates").

* North: `PASPU`
* East: `LAVAX`
* South: `REMES`
* West: `BOBAG`

Holdings are typically used at these waypoints during periods of high traffic.

All STARs end at a waypoint that is near the final approach area (Rwy 02: `SANAT`/`SAMKO` Rwy 20: `BIDUS`/`NYLON`/`BIPOP`). Then, planes are radar vectored to final. 

Feel free to use radar vectors at any time for sequencing / to avoid weather.

More information on the approach procedures:

* **ILS Approach to runway 02L / 20R**

  Usually, planes are cleared to intercept the localizer first, and only when established on the localizer that they are cleared for the ILS approach (localizer + glideslope).

  Most of the time, planes are cleared to descend to **2500ft** to intercept, but other altitudes are alright too.

* **RNP Approach to runway 02R / 20L**

  Vector aircraft as usual, when nearing the extended centerline or as appropriate, direct the aircraft to `LUVUL`/`OBGIS` (IF*) and clear the aircraft for the RNP approach. Remember to descend to 2000ft, then/or **1700ft**, for the aircraft to commence the approach.

  _* IF is the intermediate fix of the approach._

* **Simultaneous (independent/dependent) parallel approaches to both runways**

  * Rare, but possible. Increases landing capacity as both runways are utilised for landings. Challenging however! Ensure planes are separated by at least 3nm or 1000ft until localizer intercept and RNP final approach.

* **Missed Approach/Go Around**

  Continue on runway heading and climb to 3000ft or as appropriate (e.g. 4000ft).

* **Wake Turbulence Separation** 

  ICAO RECAT separation is applied between landing aircraft.



#### Further notes:

- **Potential conflict between climbing departures and descending arrivals**:
  - Particularly east of the airport, near `DOGRA`/`IGNON` waypoints.
  - To prevent the risk of loss of separation, clear departures to climb to a maximum of 6000ft, and descend arrivals to no lower than 7000ft, unless the path is clear of any conflicts.
- You may have noticed that some STARs contain a _fictional_ altitude point. This is to better simulate the *(actual)* descent profile of a plane as it enters the intermediate approach area.
- When WSSS runway 20 is in use,
  - For flights entering via `ARAMA` waypoint, `ARAMA1B` is the default STAR. `LELIB3B` is an alternative **shorter STAR** offered by ATC when traffic permits, in other words, whenever you deem fit :D
    - Direct aircraft to `LELIB` to join `LELIB3B` STAR.
      *(It actually starts at `ARAMA`, but it's not possible to implement it that way due to game limitations. Anyway, it's not a significant difference and doesn't affect gameplay.)*
  - Keep in mind when vectoring planes to Runway 20R: Rwy 20R has a displaced threshold of 740m southwards, so the approach profile for Rwy 20R is in fact similar to that of Rwy 20C and 20L. (i.e.  if you enabled runway extended centerline in the game, the depicted profile is a little different from reality)



### WSSL - Seletar Airport

------

#### Runway information

Runway 03/21: Visual approach only

Rwy 03 glidepath: 3.2°
Rwy 21 glidepath: 3.5°

Seletar is a challenging airport to land at or depart from. With a really tight airspace, runways that have similar orientations located nearby, and noise abatement areas, pilots have to be careful to keep all turns within the Seletar Control Zone while landing at the correct airport and complying with noise abatement procedures.

#### Departure and Approach Procedures

Planes either depart to the North (via `GUMPU` or `OMKOM`) or South (via `SJ-PONJO-RECHI`)

* **Initial climb is 3000ft.**
* In this file, Rwy 03 departures are assigned a heading of 360, while Rwy 21 departures fly on runway heading (213).
  * Vector them to their exit waypoints. Be mindful of traffic from/to other airports and altitude restrictions.
  * Caution prohibited, restricted and danger areas.

**Radar vectoring is mainly used to direct arrivals towards the airport. Planes can join from the North or South to land.**

_(pseudo)_ Visual approaches are available in this file. The approach procedures are outlined below. 

* Runway 03
  * If from the north, join left-hand downwind runway 03. To do so, direct the aircraft to either of the two 'helper points', `VIS03A` or `VIS03B`, **at 1500ft**.
  * If from the south, direct aircraft for a straight-in visual approach via `SJ` (or `PONJO` is fine too), following the `SJ-PONJO-RECHI` joining procedure to runway 03.

* Runway 21
  * If from the north, join straight-in final runway 21. To do so, direct the aircraft to the 'helper point', `VIS21`, **at 2000ft**.
  * If from the south, direct aircraft for a right-hand downwind visual approach via `SJ` (or `PONJO` is fine too), following the `SJ-PONJO-RECHI-SETHI` joining procedure to runway 21.

_**Special note for downwind approaches:** In the game, some aircraft may not be able to make the turn to final to land due to higher speeds. They will make a go around and you can bring them around to the other side to join for a straight-in approach._

_**TIP**: You can temporarily change the rwy config to allow a plane to land on the opposite side of the active flow by using the rwy change button._

Generally, maximum tailwind component of 10 knots is allowed for landings. If planes are unable to land due to weather, you can hold them until the conditions improve.



### Known Issues/Limitations

------

1. Potential conflict between arrivals when they just enter your airspace if the game spawns them too close to one another.
2. WSSL - Occasionally, a plane departing from runway 03 may conflict with another plane that is already on approach to runway 03 via downwind from the north (`VIS03A`/`VIS03B` 'helper points'). Unfortunately, we have no control over when the game decides to spawn a departure. :(
3. For `CHA1C/D` SIDs, final waypoint is set at `SABKA` instead of `MASBO`, and `VENPA` instead of `BAVUS/KADAR/SURGA` to facilitate departing routes and prevent potential conflicts with arrivals. This is due to limitations with the SID function.
4. WSSS Rwy 02C/20C operations not implemented. May implement in a different file at a later date.
5. WIDD not implemented. May implement at a later date.
6. WMKJ not implemented.
7. Some coastlines could be better depicted. May improve at a later date. (It takes a lot of effort...)



### Many thanks to the following resources

------

1. Civil Aviation Authority of Singapore - eAIP
2. Wikipedia
3. Google Maps
4. FlightRadar24
5. FlightAware

### Changelog

------

| Version |  Date Released   | Developed by |           Changelog            |
| :-----: | :--------------: | :----------: | :----------------------------: |
|   2.0   | 31 December 2022 |  BestBearrr  | Initial release of updated TMA |
|   1.3   |  11 August 2021  |    Jacob     |               -                |

_Disclaimer: The information included herein is not meant to be true-to-life. This file is intended for recreational use only._