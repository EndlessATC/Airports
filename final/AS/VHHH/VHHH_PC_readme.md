#VHHH TMA 1.0.0

This is an implementation of the Hong Kong TMA (Terminal Maneuvering Area) for [Endless ATC](https://steamcommunity.com/app/666610) featuring `VHHH` Hong Kong International Airport (also known as Chek Lap Kok) and `VMMC` Macau International Airport. The airspace ceiling is FL250. `ZGSZ` Shenzhen Baoan, although not part of the VHHH TMA, has traffic that would transit the airspace at altitudes low enough to be considered for inclusion. However it is not currently implemented.

The maximum controllable area is limited by the spawn point limits in Endless ATC, which is a 100nm circle around the map center. Therefore, the controlled area in this implementation is a heavily reduced portion of the actual VHHH TMA, omitting much of the terminal transition routes. As such, it is recommended to begin a new game at 4x speed until an aircraft reaches an initial approach fix, and play with a high minimum score (be sure to slowly ramp up to the desired value) or a fixed flow of ~30+.

Based upon AIP HONG KONG EFF 2021/02/25 and AIP MACAO AMDT 39 EFF 2020/11/19. The choice of SIDs and STARs may not be 100% accurate to real life but should be reasonably accurate reflecting daytime IMC conditions. All aircraft are assumed to be RNAV capable. Pure RNAV approaches are not implemented in favour of RNAV+ILS or conventional ILS approaches. Coastline data from naturalearthdata.com.

STARs are implemented as approach transitions. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. Multiple approaches may be available from a fix. Press the APP button again  before issuing the approach clearance (do not long press) will select the next approach available from that fix. If the aircraft is already on an approach from that fix, you will need to cancel the approach clearance first before issuing another approach clearance.

## Airports

### `VHHH` Hong Kong International Airport (Chek Lap Kok)

A modern island airport built on reclaimed land north of Lantau Island after Hong Kong outgrew the old airport at Kai Tak, famous for the IGS RWY 13 "Checkboard" approach. Being located on its own island and built from scratch, the approaches to Chek Lap Kok are much more forgiving than at Kai Tak, but the mountaineous terrain of Hong Kong still restricts flight paths. The proximity of the Hong Kong - Guangzhou FIR boundary just north of the airport, and the other airports closely packed into the river delta region also result in a very restricted airspace.

In general, `VHHH` operates in a segregated mode with the north runway used for arrivals and the south runway used for departures.

There is custom traffic for `VHHH`. The proportions are very much estimates but shouldn't be too far off from reality.

Some major fixes on the map have a defined hold including many fixes along the STARs. If playing with a high amount of traffic, significant holding may be required with only one landing runway and lack of room for delay vectors close to the airport. For arrivals from the northeast, traffic may be redirected to the southeast arrival route via MEPUT for additional holding at EATON and beyond.

Note that as the game cannot handle multiple approaches to the same runway from the same fix, `SIERA` 7C/6D STARs from `SIERA` can be activated using direct to `BORDA`.

Aircraft arrive via 4 points:

- `FISHA` (`A1/G581 ELATO V522` from Taipei FIR to the east; `A470 DOTMI V512` or `M503 LELIM V591` from the northeast via Guangzhou FIR)
- `DAKTO` (`A461/M501 NOMAN V532` from Manila FIR the southeast)
- `HOCKY` (`A583 SABNO V542` or `M771/M772 DUMOL Q1 CARSO V551` from the south/southwest)
- `GAMBA` (`A1/P901 IDOSI V561` or `A202/R339 SIKOU V571` from Sanya FIR to the west)
- `SIERA` (`R473 SIERA` from Guangzhou FIR to the north)

Aircraft depart via 10 points:

- `BEKOL` (north via `A461` to China)
- `DOTMI` (northeast via `A470` to southeastern China)
- `LELIM` (northeast via `M503` to Shanghai Pudong, Qingdao, Dalian, Yantai)
- `ENVAR` (east via `M750` to Korea, Japan, Pacific)
- `KAPLI` (east via 'G86' to routes south of Taiwan)
- `NOMAN` (southeast via `M501` and `A461` to Philippines)
- `SABNO` (south via `A583`)
- `EPDOS` (southwest via `L642` to Singapore, Malaysia)
- `IDOSI` (southwest via `A1` to Cambodia, Vietnam, Thailand)
- `SIKOU` (west via `A202` or `R339` to Hainan, Hanoi, India etc.)

There are two runways:

-07L/25R (departures)
-07R/25L (arrivals)

Two landing configurations are in general use:

-	Landing 07L, departing 07R

	The usual configuration. 

	The ILS approach to 07L is available from the FAF `VH710`, but in practice all approaches are made from `LIMES`. It is not recommended to vector aircraft inside `LIMES`, and should be completely avoided inside `VH710`. due to the proximity of the FIR boundary and the high terrain south and northeast of the airport.

	Upon missed approach, aircraft can climb to 5000 and fly the approach again from `DEDEE`, which will simulate a full missed approach back to the IAF `LIMES`. If the aircraft is not ready by `DEDEE`, the approach is also available from `SAMPU` and `TD` etc.

	Speed management can be effective to sequence aircraft by `LIMES`. Use care to normalize speed between aircraft once they reach `LIMES` so as to maintain separation until the runway.

	Note that independent simultaneous approaches to 07L and 07R are not permitted. Note that the RNP Y contingency procedure is not implemented.

	Departures from 07R should fly the STAR to *fly-over* the first waypoint (`PORPA`) -5000 to clear the high terrain of Lantau Island south of the airport and the restricted area VHR12. Afterwards, altitude management should be sufficient to separate from any other traffic.

-	Landing 25R, departing 25L

	The west wind configuration. 

	The ILS approach to 25R is available from the FAF `RIVER`, but in practice all approaches are made from `TD` or `PLOVE`. It is not recommended to vector aircraft inside `TD`, and should be completely avoided inside `RIVER`. due to the proximity of the FIR boundary and the high terrain under the approach path.

	Upon missed approach, aircraft can climb to 5000 and fly the approach again from `MA25R`, which will simulate a full missed approach back to the IAF `TD`. The missed approach path does not actually include point `MA25R`, it is a fictional waypoint placed a distance away from the airport as an aircraft cannot be commanded to proceed direct to a fix close by. The missed approach is also available from `LKC`, but usually the aircraft on missed is too close from `LKC` and the game will not allow direct to `LKC`.

	Speed management can be effective to sequence aircraft by `TD`. Use care to normalize speed between aircraft once they reach `TD` so as to maintain separation until the runway.

	Note that independent simultaneous approaches to 25L and 25R are not permitted. Note that the RNP Y procedure is not implemented.

	Departures from 25R should fly the STAR to *fly-over* the first waypoint (`PRAWN`) -5000 to clear the high terrain of Lantau Island south of the airport. Afterwards, altitude management should be sufficient to separate from any other traffic.

### `VMMC` Macau International Airport

This airport serving the city of Macau has an island runway connected to the apron by two long taxiway bridges. Another peculiarity is how it is located between the Hong Kong and Guangzhou FIRs, with aircraft to the north handled by Guangzhou but aircraft to the south handled by Hong Kong. Due to Zhuhai city north of the RWY 34 departure end, aircraft must stay south of the 231 radial from Jiuzhou VOR (`ZAO`) for noise abatement, resulting in an immediate turn to the right departing 34, and a Kai Tak-style approach with an offset localizer to final visual approach for landing 16.

To faciliate arrivals to 16, a portion of Guangzhou FIR around `ZUH` and south of `NLG` has been included in the airspace, with the low altitudes restricted to `VMMC` traffic.

There is custom traffic for `VMMC`. The proportions are very much estimates but shouldn't be too far off from reality. Note that only traffic departing and arriving via Hong Kong FIR are included.

Some major fixes on the map have a defined hold including many fixes along the STARs.

Aircraft arrive via 4 points:

- `NEDLE` (`J101` from the east via Taipei FIR or from the northeast via Guangzhou FIR)
- `ISBAN` (`J103` from the southeast via Manila FIR or southsouthwest via Sanya FIR)
- `DASON` (`J104` from the south/southwest via Sanya FIR)

Aircraft depart via 9 points:

- `DOTMI` (northeast via `A470` to southeastern China)
- `LELIM` (northeast via `M503` to Shanghai Pudong, Qingdao, Dalian, Yantai)
- `ENVAR` (east via `M750` to Korea, Japan, Pacific)
- `KAPLI` (east via 'G86' to routes south of Taiwan)
- `NOMAN` (southeast via `M501` and `A461` to Philippines)
- `SABNO` (south via `A583`)
- `EPDOS` (southwest via `L642` to Singapore, Malaysia)
- `IDOSI` (southwest via `A1` to Cambodia, Vietnam, Thailand)
- `SIKOU` (west via `A202` or `R339` to Hanoi, India etc.)

There is the one island runway, 16/34. However, to simulate the offset localizer for 16, a fake runway 16C(/34C) is included. Planes will land on 16C instead of 16.

Two landing configurations are in general use:

-	Landing 34, departing 34

	The usual configuration. 

	The ILS approach to 34 is available from the FAF `PAPA`.

	Upon missed approach, aircraft can climb to 6000  (by `MC411`) and fly the approach again from `ZAO`, which will simulate a full missed approach back to the IAF `HAZEL`. If the aircraft is not ready by `ZAO`, the approach is also available from `MC420` and `MC411`. Holding after missed is available at PAPA.

	Speed management can be effective to sequence aircraft.	Arrivals via the established STARs are recommended due to the congestion of airspace around `VHHH`.

	Use care to have 34 departures climb to 6000 (+4000 by `MC420`, +5500 by `MC411`) to cross `LKC` 6000 with further climb subject to traffic conditions (arrivals via `SMT` overhead).

-	Landing 16(C), departing 16

	The south wind configuration. 

	The LLZ/DME approach to 16(C) is available from the IAF `ZUH`. You should not vector aircraft inside `ZUH` as these aircraft would be under control of Guangzhou after `INDUS`.

	Upon missed approach, aircraft can climb to 4000 and fly direct to MC513 where holding is available at +3000. From `MC513`, aircraft can execute the approach via `INDUS`/`ZUH`/`MC513` at +5900 (+1800m). 

	Speed management can be effective to sequence aircraft.	Arrivals via the established STARs are recommended due to the congestion of airspace around `VHHH`.

	Use care to separate 16 departures from `VHHH` arrivals between `CANTO` and `MURRY` and `VHHH` departures near `PECAN`.

## Known Issues

- No `ZGSZ`
- No `ZGSD`
- No RNP Y procedures
- No 25/34 or 07/16 configurations
- The northern boundary is super lazy (I am not going to trace 3nm from the Chinese coastline, sorry)
- `SIERA` C/D arrivals only selectable from `BORDA`
- `UJ` and `MCU` transitions implemented for `VMMC` 34 but would only be used for arrivals from `ZGZU` FIR, leaving them in for the heck of it

## Disclaimer

This is a best effort work based on air traffic observations and official aeronautical publications. No guarantee is made that this representation of VHHH TMA matches real life procedures in any way. Any information regarding inaccuracies is appreciated.

## For Developers

This file is built from `source\VHHH.txt` via `deploy.py`. Make any contributions to `source\VHHH.txt` and NOT to `.\VHHH.txt`.

## Changelog

*	1.0 - 2020/01/09 - Initial version.
