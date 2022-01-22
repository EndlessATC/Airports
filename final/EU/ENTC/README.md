# Tromso Airport ENTC
Made by PosKi#7463 - please contact me on Discord with any problems or bugs

## Acknowledgements
I would like to thank dunne_boktor#4557 for his tips about the tools and websites to use for making airports - they were very helpful to me as a first time custom-airport maker.  

I would also like to thank Jannik04#9379 for information about Norwegian airspace and aviation charts and I am looking forward to seeing ENTC as a part of his FIR Bodo that is in the works.

## Info
### General
Tromso is a town located in northern Norway, north of the Artic Circle, with a population of about 65000. This makes it the third largest city in the world north of the Arctic Circle, and by far the largest city in this northern part of Norway. The University of Tromso is also the world's northermost university.  

The city resides on the island of Tromsoya, with the city center located on the opposite side of the island from the airport. Other parts of the city are scattered on the surrounding islands and peninsulas, connected by bridges and tunnels. As most of the Norway coastline, the surroundings of the city are highly ragged, characterised by many islands and fjords.

### Practical
As mentioned, the airport is situated on the western side of the Tromsoya island, with a single 2447 meter runway. It handled more than 2.2 million passangers in 2019 (pre-pandemic). It is the main hub in northern Norway for Wideroe, serving many regional airports in the area and also larger Norwegian cities down south. Additionaly, it is served by both SAS and Norwegian, which fly in from the south (usually Oslo or other larger Norwegian cities) and then use the plane to serve the Longyearbyen airport in Svalbard or the Alta airport in Norway, to the east from Tromso. On top of that, it is also occasionally served by Lufthansa, Eurowings, Wizz Air and other European airlines, some of them being just charters.  

The airport is surrounded by mountainous terrain, with some of the peaks in the immediate area going all the way to 3600 feet and even higher. Therefore, the airport operates a 4 degree glideslope in both directions, being steeper than the usual 3 degrees used on most airports, but shallower than the 5.5 degree glideslope at the London City airport. Due to the proximity of the Norwegian Sea and the hilly terrain, it is also prone to relatively strong winds and windshears.

## Future plans
- ~~Finish coastline~~
- Polish bugs should some arise
- Version 2.0, which will include Andoya Airport and Bardufoss Airport
- Polaris FIR Bodo in the works by Jannik04#9379 including all three of these airports and many more


## How to play

### General
- Due to the relatively low amount of traffic in real life, a realistic setting simulating the peak hours traffic would be a skill level of about 5-6, or a flow of about 15/hr (both arrivals and departures) - in this case, I recommend playing on 4x speed to make the gameplay at least a bit challenging
- For further challenge, try playing with winds of 10-20 kn in various directions
- Additionaly, for the realistic (low) level of traffic, feel free to vector the planes manually instead of using the automatic approaches  

- If not following the defined approaches, keep the planes above FL105 outside of the Tromso TMA (the polygon inside the circular airspace boundary)
- In case some of the arrivals start expedite descent when entering the airspace, reduce their speed to 250 kn and cancel the expedite descent (all planes should be able to follow the set altitudes of the approaches when entering the approaches at 250 kn)
- Even though the `floor` is set to 1100 feet, this altitude should not be maintained unless there is an emergency and in that case the plane has to be kept flying above water, away from the hilly terrain in the area

### RWY 18 configuration
- The holding waypoints for this configuration are ATWEG (6000 ft), BAMME (5000 ft), MANKI (11000 ft), PAXLO (8000 ft) and SOXOX (11000 ft)
- If the planes would come too close to each other when coming to the ILS through the automatic approaches, adjust their speed, hold at one of the holding waypoints, or vector the planes away from the ILS before turning back in and/or following the rest of the approach from NORNU/OGBOD/APSIM (and possibly LOMVI)
- In case of a missed approach, climb to at least 5000 ft, hold at BAMME if needed, and then follow the approach from BAMME or vector the plane manually to the ILS  

- For planes following the SIDs with the sharp right turn after takeoff, reduce the speed to 180 kt or lower asap and increase it after the plane finished the turn - that way, the turn stays realistically sharp and true-ish to the charted SID path
- If needed to avoid the traffic following the approach from MANKI, keep the speed of the east-bound departurers initially reduced to 220 kt (200 kt for jets)
- If there is an incoming traffic on the approach between ULNIK and BAMME, let the departures climb to 9000 ft and keep them there until they are clear of the arrivals

### RWY 36 configuration
- The holding waypoints for this configuration are ATWEG (6000 ft), MANKI (11000 ft), OSRAD (5000 ft), AKAKA (6500 ft) and PAXLO (8000 ft)
- If the planes would come too close to each other when coming to the ILS through the automatic approaches, adjust their speed, hold at one of the holding waypoints, or vector the planes away from the ILS before turning back in and/or following the rest of the approach from REBLI/VAMEN/UMSEG (and possibly ROSKO and VEDIG)
- In case of a missed approach, climb to at least 5000 ft, hold at OSRAD/AKAKA if needed, and then follow the approach from OSRAD/AKAKA or vector the plane manually to the ILS  

- If the departures cross paths with a plane following the LOMVI arrival, lower the speed of the departing plane in time to climb over the traffic following the approach
