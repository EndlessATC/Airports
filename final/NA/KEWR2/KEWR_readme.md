# `EWR TRACON` - Newark Area of the New York (N90) Tracon
This is my take on Newark Liberty International Airport (KEWR) in Newark, NJ.
#It's got four configurations - two standard ones, landing 4R/22L and departing 4L/22R, and two special ones 
#normally used during high crosswinds, where you land planes via the RNAV to 29! For these, rather than vectoring 
#planes into the ils, you should send them direct to the waypoint TETER when in a northern flow, and KILMA when
#in a southern flow. Clear them for the APP from there, and they will automatically follow the RNAV in to the runway!
#Aside from that, the three major reliver airports, Teterboro, Caldwell, and Morristown, are all represented as well. 
#There are a few minor sticking points. Occasionally, departures out of TEB may interfere with arrivals on the ILS to 22L at Newark,
#and departures from Caldwell's 22 may interfere with arrivals on the ILS to Morristown's 23. I've tried to reduce them as much as possible
#but I couldn't do everything.

## Configurations
There are six different configurations avalible, listed below in the table. When referenced later in the file, I will only use the letters (A-F) to describe them.
| Configuration | KEWR | KTEB | KCDW | KMMU |
| --- | --- | --- | --- | --- |
| Alpha (A) | Land 22R, Dep 22L | Land 19, Dep 24 | Land/Dep 22  | Land/Dep 23 |
| Bravo (B) | Land 4L, Dep 4R | Land 6, Dep 1 | Land/Dep 4 | Land/Dep 5 |
| Charlie (C) | Land 22R, Dep 22L | Land/Dep 24 | Land/Dep 22 | Land/Dep 23 | 
| Delta (D) | Land 29, Dep 22L | Land 19, Dep 24 | Land/Dep 22 | Land/Dep 23 |  
| Echo (E) | Land 29, Dep 22L | Land/Dep 24 | Land/Dep 22 | Land/Dep 23 |  
| Foxtrot (F) | Land 29, Dep 4R | Land 6, Dep 1 | Land/Dep 4 | Land/Dep 5 | 


## Airports
### `KEWR` Newark Liberty International Airport
The main airport of this sector. Being one of three major airports serving New York City, and the largest airport in New Jersey, Newark is a very busy airport. It is a major hub for United Airlines, so expect to see a lot of UAL, and of its various regional partners, but also sees a fair amount of international traffic, alongside a decent amount of cargo traffic, particularly FedEx. As EWR is the primary airport, it does not have airport-specific airspace

### `KTEB` Teterboro Airport
The busiest of the secondaries, and located north of EWR, directly under the 22L ILS approach, Teterboro is primarily a hub for buisness jets, and is the airport of choice for the rich and famous when they travel to New York. While it can see traffic levels comparable to that of a medium-sized international airport, a 100,000lb weight limit keeps the airlines out. Teterboro tower controls all airspace within 4 nm of the field up to 1800 ft, and flights to other airports should NOT be allowed to enter its airspace. 

Teterboro has three major runway configurations

Land 19, Dep 24 (A,D)
Land/Dep 24 (C,E)
Land 6, Dep 1 (B,F)

### `KCDW` Essex County Airport
Located to the west of EWR and TEB, Essex County Airport, more often known as Caldwell, is chiefly a flight training hub, with multiple fight schools on the field and its pattern nigh always full of VFR traffic, although it will occasionally see the odd larger bizjet as well. Caldwell is the least busy of the four, and you can expect to see mostly just light GA traffic here. Caldwell tower controls all airspace within 4 nm of the field below 2700 ft, except for a small cutout in the SW due to MMU. Flights to other airports should NOT be allowed to enter its airspace
Caldwell has two major runway configurations

Land/Dep 22 (A,C,D,E) 
Land/Dep 4 (B,F)

### `KMMU` Morristown Municipal Airport
Located to the south of CDW, Morristown sits somewhat inbetween Caldwell and Teterboro in scale, as it is busier than CDW, and sees a decent bit more bizjet traffic as well but still has some flight schools, and as such, sees plenty of light GA traffic as well, unlike Teterboro. Morristown tower controls all airspace within 4 nm of the field below 2700 ft, and flights to other airports should NOT be allowed to enter its airspace

Caldwell has two major runway configurations

Land/Dep 23 (A,C,D,E) 
Land/Dep 5 (B,F)
