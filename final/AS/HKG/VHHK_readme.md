
# VHHK FIR 1.0

This is an implementation of the Hong Kong FIR and TMA for [Endless ATC](https://steamcommunity.com/app/666610) featuring `VHHH` Hong Kong International Airport . The airspace ceiling is FL250.

Based upon AIP Hong Kong 11/20 (2020 11th Version) . The SIDs and STARs may not be 100% accurate to real life but should be reasonably accurate reflecting daytime IMC conditions. All traffic are designed to fly RNAV(GNSS) and ILS APCH. The Northern Boundary data between VHHK FIR and ZGZU FIR are from Basic Law Instrument 11.

The border of the map has included VHHK FIR and playable range only include VHHH TMA due to the size of FIR are too big to play.
Information of Hong Kong TMA, Transition Altitude (TA) shall be 9000ft and Transition Level (TFL) shall be FL110 (QNH980+), FL120 (QNH979-). Do not assign FL100! Live QNH can be retrieved at [ATIS](https://atis.cad.gov.hk/ATIS/ATISweb/atis.php) by CADHK.

STARs are implemented as approach transitions. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. Multiple approaches may be available from a fix. Press the APP button again  before issuing the approach clearance (do not long press) will select the next approach available from that fix. If the aircraft is already on an approach from that fix, you will need to cancel the approach clearance first before issuing another approach clearance.

Inside VHHK FIR have 4 Airports, `VHHH`, `VHHX`, `VHSK` and `VMMC`. Further Information will be included below.

## Airports

### `VHHH` Hong Kong International Airport
The main airport of this sector. Which is alson only airport included in current verison *v1.0*. HKIA is also the only International Airport had two runway within FIR. All departures and arrivals come from or to Southern, Eastern and Western only due the packed Airspace with nearby Guangzhou FIR and Shenzhen Airport approach route. 

There is custom traffic for `VHHH`. Although it is NOT reliable and only designed for the hub airline callsign to show up. *For Government / HKG, are usually operating Helicopters and Small Planes, I had included C172 for its slow purpose. Please be alert with it as it can't follow the speed with airliner.

All visible fixes on the map have a defined hold including many fixes along the STARs but excluded LKC and SMT. Standard Missed Approach Route will be included in later versions.

#### Arrival STARS
- `ABBEY`: Eastern route from RCAA (Taipei) FIR, ZGZU (Guanzhou) FIR and ZSHA (Shanghai) FIR
- `BETTY`: Southeast route from RPMR (Manlia) FIR and ZGZA (Sanya) FIR
- `CANTO`: Southwest route from ZGZA (Sanya) FIR, ZGZU (Guangzhou) FIR
- `SIERA`: Northern route from ZGZU (Guangzhou) FIR

#### Departure SID
-`BEKOL`: Northern Route, No TTR, No Handoff below S0690 / F226.
-`LAKES`: Northeast Route, TTR V1/V13, Handoff at F230
-`OCEAN`: Eastern Route, TTR V2/V3/V4/V5, Handoff at F250
-`PECAN`: Southwest Route: TTR V10/V11/V12, Handoff at F160

#### Runway (Suffix for SID/STAR)
- 07R (A)
- 25L (B)
- 07L (C) *Use (A) for STAR
- 25R (D) *Use (B) for STAR

#### Operations
Due to Complication of airspace, all traffic are suggested to follow STAR approach and Do not assign holding at / under 15+ inbound within 30 minutes.
**For Runway 07:**

 - TD VOR is a collision point between Departure SID and Arrival STAR:
	 - Departure maintain 5000ft or below
	 - Arrival maintain 7000ft or above 

**Operations:**

 - Northern Runway 07L/25R is the usual Arrival Runway
- Southern Runway 07R/25L is the usual Departure Runway / Cargo Arrival 
	- Cargo Airlines: CPA w/ B748, HKC, AHK, HKC
	


### `VMMC` Macau International Airport
Macau International Airport, To be built.
ISO 3166-2: MO
Runway 16/34

### `VHHX` Hong Kong Airport (aka Kai Tak Airport)
Kai Tak Airport (Depreciated)
Name: KT
Runway 13/31 (Special Operation on 13)
KT ATZ has included in *v1.0*

### `VHSK` Shek Kong Airport
Shek Kong airport, Millitary Airport
Shall Not expect simualtion in EATC


## Known Issues
Everything is still missing ;(

## Disclaimer

This is a best effort work based on air traffic observations and official aeronautical publications. No guarantee is made that the representation of Hong Kong FIR and TMA matches real life procedures in any way. Any information regarding inaccuracies is appreciated.

## For Developers
This version was designated for phone play, awaitng a larger version for PC.

## Resources
* [eAIP](https://www.ais.gov.hk/) by CADHK
* [ATIS](atis.cad.gov.hk/) by CADHK
* from [IVAO HK](https://xe.ivao.aero) (Currently Sub-division of XE)
* from [Civil Aviation Department Hong Kong](https://www.cad.gov.hk/)
* from [Airport Authority Hong Kong](https://www.hongkongairport.com/)
* from Hong Kong Government
* Special Thanks: README.md template from RJTT_readme.md by [ckwng](https://github.com/AdamJCavanaugh/EndlessATCAirports/commits?author=ckwng)

## Changelog

*	1.0 - 2020/12/31 - Initial version.
	* 1.1 - 2021/01/01 - HotFix: North Border