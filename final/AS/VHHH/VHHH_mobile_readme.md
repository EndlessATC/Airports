
# Hong Kong TMA / VHHH Hong Kong
__Important Notes__	
This is a such simpler version develop for Mobile EATC player.The folder going to store in your phone is: `\\Android\data\com.dirgtrats.endlessatc\files`
 Height Measurement to be used are Feet and  NM, included China Airspace. Otherwise specifically stated.
## Information
This is an implementation of the Hong Kong FIR and TMA for [Endless ATC](https://steamcommunity.com/app/666610) featuring `VHHH` Hong Kong International Airport. The airspace ceiling is FL250.

This Map ONLY include Hong Kong Terminal Control Area and some Extended Section on Zhuhai TCA.

*v1.0* Based upon AIP Hong Kong 11/20 (2020 11th Version) . The SIDs and STARs may not be 100% accurate to real life but should be reasonably accurate reflecting daytime IMC conditions. All traffic are designed to fly RNAV(GNSS) and ILS APCH. The Northern Boundary data between VHHK FIR and ZGZU FIR are from Basic Law Instrument 11.

The border of the map has included VHHH TMA, VMMC ATZ, ZGGG FIR and ZGZUTM04 TCA and playable range only include VHHH TMA and VMMC ATZ due to the size of FIR are too big to play.
Information of Hong Kong TMA, Transition Altitude (TA) shall be 9000ft and Transition Level (TFL) shall be FL110 (QNH980+), FL120 (QNH979-). Do not assign FL100! Live QNH can be retrieved at [ATIS](https://atis.cad.gov.hk/ATIS/ATISweb/atis.php) by CADHK.

STARs are implemented as approach transitions. To activate an approach, an aircraft must be flying direct to an applicable fix, then the APP button can be activated. Multiple approaches may be available from a fix. Press the APP button again before issuing the approach clearance (do not long press) will select the next approach available from that fix. If the aircraft is already on an approach from that fix, you will need to cancel the approach clearance first before issuing another approach clearance.

Inside VHHK FIR have 4 Airports, `VHHH`, `VHHX`, `VHSK` and `VMMC`. Further Information will be included below.

## Airports
### `VHHH` Hong Kong International Airport
The main airport of this sector. HKIA is also the only International Airport had two runway within FIR. All departures and arrivals come from or to Southern, Eastern and Western only due the packed Airspace with nearby Guangzhou FIR and Shenzhen Airport approach route.

There is custom traffic for `VHHH`. Although it is NOT reliable and only designed for the hub airline callsign to show up.

All visible fixes on the map have a defined hold including many fixes along the STARs but excluded SMT. Standard Missed Approach Route included since version 1.5 .

#### Arrival STARS
- `ABBEY`: Eastern route from RCAA (Taipei) FIR, ZGZU (Guanzhou) FIR and ZSHA (Shanghai) FIR
- `BETTY`: Southeast route from RPMR (Manlia) FIR and ZGZA (Sanya) FIR
- `CANTO`: Southwest route from ZGZA (Sanya) FIR, ZGZU (Guangzhou) FIR
- `SIERA`: Northern route from ZGZU (Guangzhou) FIR
#### Departure SID
- `BEKOL`: Northern Route, No TTR, No Handoff below S0690 / F226.
- `LAKES`: Northeast Route, TTR V1/V13, Handoff at F230 (Auto-Handoff)
- `OCEAN`: Eastern Route, TTR V2/V3/V4/V5, Handoff at F250 (Auto-Handoff)
- `PECAN`: Southwest Route: TTR V10/V11/V12, Handoff at F160

#### Standard Missed Approach
- `07L`: Track to `DEDEE`, climb 5000ft
- `07R`: Track to `GUAVA`, climb 5000ft
- `25L`: Track to `PRAWN`, climb 5000ft
- `25R`: Track to `SMT`, climb 5000ft before crossing Localizer


#### Operations
Due to Complication of airspace, all traffic are suggested to follow STAR approach

##### For Runway 07:
- TD VOR is a collision point between Departure SID and Arrival STAR:
- Departure maintain 7000ft or below
- Arrival maintain 9000ft or above
##### Avbl for All Runway
- Northern Runway 07L/25R is the usual Arrival Runway
- Southern Runway 07R/25L is the usual Departure Runway / Cargo Arrival
- Cargo Airlines: CPA w/ B748, HKC, AHK, HKC
### `VMMC` Macau International Airport
> Macau International Airport, built and released at *v1.4*.
#### Info
Macau Int'l Airport, short for `MO`
Single Runway, Runway 16 / 34
It's Hard.
> ISO 3166-2: MO
>For In-game TTS Purpose, Full Name included only have **Macau** instead of **Macau Int'l Airport**
#### Arrival STAR
>Transition Route included Below Sub-Chapter
- Belongs Hong Kong VHHH TMA / FIR
	* `CHALI`: Southern Route from RPHI (Manila FIR Eastern), ZGZU (Guangzhou FIR South-Western), ZSJA (Sanya FIR Southern)
	* `SMT`: Northeastern Route from RCAA (Taipei FIR Eastern), ZGZU (Guangzhou FIR NorthEastern)
- Belongs China ZGZU FIR / ZSJD TCAD
	> Due to Objective Airspace, Limited STAR from China will be provided
	* `GURIN` : Only Southern Route from China
		* Original STAR: `BIRGO`
	* `MC511` / `LATOP`: Only Northern Route from China
		* Original STAR: `CON`,`POU`,`NLG`
		* `MC511`: Operation for Runway 16 Only.
			* Inbound approach: 3000ft, continue join 16LLZ
			* Auto-route RWY34: Climb 7800, Joining LATOP approach
		* `LATOP`: Operation for Runway 34 Only.
			* Inbound approach: 7800ft,
			* Auto-route RWY16: Climb 7800, Route to MCU and ZUH approach
#### Departure SID
> Due to Objective Airspace, Limited SID for both Hong Kong and China will be provided
>
> Runway 34: All Departure Transit Hong Kong will use 2U (cross TD) Departure.
* Departure Handled by Hong Kong
	> For Traffic Crossing Hong Kong, Cross Border at or above 5500'
	* `ALLEY`: End at `ALLEY`/ `PECAN`
	* `CONGA`/ `GRUPA`/`SOUSA`: Ended at `SKATE`/`OCEAN`
* Departure Handled by Guangzhou
	* `BIGRO`: Last point in operating Airspace: `BOKAT`
		* Suggested Handoff Point: `LATOP`
	* `NLG`/`SHL`/`MIPAG`: `LATOP` will be End of Operation (Both Runway)
#### Transition Route
> These TTR are within VHHK TMA for VMMC Approach, which are shortened and Having High chance of Error
* For CHALI Approach
	* `ROBIN`: Route from `SANBO`, 	`SIKOU`, `DUMOL`
	* `PECAN`: Entry Point
* For SMT Approach
	* `NEDLE`: Route from J101: `ELATO`, `DOTMI`
#### Special Operation 
* Runway 16 Runway Extension Line (In-game ILS)
	> Due to Unavbl Offset LLZ, Sepcial Setup for better game experience. But still Ultra Hard.
	* Left Offset 5deg (M163 Sim, M158 Real-life)
	* Angle to Land: 3.5deg (3deg IRL)
* Runway 16 Offect Localiser Unavailable
	> Currently Approach Route can be auto-handoff with Offset LLZ
	* Alternative: Setted up LLZ 16 apch
	* LLZ16 Ops: After Alignment on LLZ (ZAO radian 217), DCT give ILS Clearance.
* Runway 16 Circle to Land
	* PAPA Inbound, Approach Route Reference ONLY
	* Left Holding at MCU (Default) , Speed Max 160kt
* Go Around Speed
	* Default Go Around: 2000', 200kt
	* Suggested Ops: <3000', <180kt 
	* Remains inside VMMC ATZ for Go Around Traffic
### `VHHX` Hong Kong Airport (aka Kai Tak Airport)
> Started Service in v1.5
Kai Tak Airport (Depreciated)  
Name: VX
#### Runway 13 / 31
> Required Manual Check on Final Approach

### `VHSK` Shek Kong Airport
Shek Kong airport, Millitary Airport
Shall Not expect simualtion in EATC
## Known Issues
Everything is still missing ;(
### Kai Tak Airport
Runway 13 Final Approach Required Manual Checking the Conflicts with VHHH Departures
### Macau Airport
All Issues Included inside Macau Airport / Special Operation
## Disclaimer
This is a best effort work based on air traffic observations and official aeronautical publications. No guarantee is made that the representation of Hong Kong FIR / TMA, Macao TMA, Guangzhou FIR and Zhuhai TCA matches real life procedures in any way. Any information regarding inaccuracies is appreciated.
All right reserved
## For Developers
For further infomative version, consider PC version developed by ckwng.
## Resources used
* [eAIP](https://www.ais.gov.hk/) by CADHK
* [ATIS](atis.cad.gov.hk/) by CADHK
* from [IVAO HK](https://xe.ivao.aero) (Currently Sub-division of XE)
* from [Civil Aviation Department Hong Kong](https://www.cad.gov.hk/)
* from [Airport Authority Hong Kong](https://www.hongkongairport.com/)
* from Hong Kong Government
* Special Thanks: README.md template from RJTT_readme.md by [ckwng](https://github.com/AdamJCavanaugh/EndlessATCAirports/commits?author=ckwng)
## Changelog
* 1.0 ( / ) - 2020/12/31 - Initial version.
* 1.1 ( / ) - 2021/01/01 - HotFix: North Border
* 1.2 ( / ) - 2021/01/03 - Included ZGZUTM04 Airspace / VMMC Border line.
* 1.3 (p1.3) - 2021/01/10 - File Name Conflict Update, Extra Information Inc.
* 1.4 (p1.4) - 2021/01/18 - VMMC/MCU Macau Airport Integration (VHHX Reserve Name Update)
	* 1.4 Suppliments: Game File Clean-up Comments, Readme file remove extra lines
* 1.5 (p1.5) - 2021/08/31 - EATC v4.6 Update Support
	* Map Data Update
	* Handoff Frequency
	* Standard Missed Approach Procedure
## License
All Rights Reserved
Copyright (c) 2021 ycohui
Map data for EndlessATC included / retrieved by ycohui
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
